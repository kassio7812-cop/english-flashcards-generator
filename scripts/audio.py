"""
audio.py

Gera os áudios das lições.
"""
from tqdm import tqdm
from __future__ import annotations

from pathlib import Path

from scripts.console import Console
from scripts.csv_reader import CsvReader
from scripts.settings import Settings
from scripts.stats import Stats
from scripts.tts import TTS


class AudioGenerator:

    def __init__(
        self,
        settings: Settings,
        stats: Stats,
    ) -> None:

        self.settings = settings
        self.stats = stats

        self.reader = CsvReader()

        self.tts = TTS(
            voice=settings.voice,
            rate=settings.rate,
            volume=settings.volume,
        )

    def generate(self, lessons):

        for lesson in lessons:

            Console.lesson(lesson.name)

            self.process_lesson(lesson)

    def process_lesson(self, lesson):

        lesson.ensure_audio_folder()

        phrases = self.reader.read(
            lesson.csv_file
        )

        lesson.total_phrases = len(phrases)

        self.stats.lessons += 1

        self.stats.phrases += lesson.total_phrases

        for phrase in tqdm(

    phrases,

    desc=f"🎧 {lesson.name}",

    unit="frase",

    ncols=80,

    colour="green",

):

    self.process_phrase(

        lesson,

        phrase,

    )

    def process_phrase(
        self,
        lesson,
        phrase,
    ):

        filename = (
            f"{phrase['id']:03}.mp3"
        )

        output = (
            lesson.audio_folder /
            filename
        )

        if (
            output.exists()
            and self.settings.skip_existing
        ):

            lesson.skipped += 1

            self.stats.skipped += 1

            Console.skipped(filename)

            return

        try:

            self.tts.generate(
                phrase["english"],
                output,
            )

            lesson.generated += 1

            self.stats.generated += 1

            Console.generated(filename)

        except Exception as error:

            self.stats.errors += 1

            Console.error(
                f"{filename} -> {error}"
            )