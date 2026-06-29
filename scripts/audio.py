"""
audio.py

Geração de arquivos MP3.
"""

from __future__ import annotations

from pathlib import Path

from gtts import gTTS
from tqdm import tqdm

from scripts.config import AUDIO_DIR
from scripts.logger import Logger
from scripts.utils import mp3_filename


class AudioGenerator:

    def __init__(self, settings, stats):

        self.settings = settings
        self.stats = stats

    # -------------------------------------------------

    def generate(self, lessons):

        
        AUDIO_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        for lesson in lessons:
            self.generate_lesson(lesson)

        Logger.info("Geração de áudio concluída.")

    # -------------------------------------------------

    def generate_lesson(self, lesson):

        folder = AUDIO_DIR / lesson.name

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        iterator = lesson.phrases

        if self.settings.show_progress:

            iterator = tqdm(
                lesson.phrases,
                desc=lesson.name,
                unit="frase",
                colour="green",
            )

        for phrase in iterator:

            self.generate_phrase(
                phrase,
                folder,
            )

    # -------------------------------------------------

    def generate_phrase(
        self,
        phrase,
        folder: Path,
    ):

        if not phrase.english.strip():

            self.stats.errors += 1
            return

        filename = mp3_filename(
            phrase.id
        )

        filepath = folder / filename

        if (
            self.settings.skip_existing_audio
            and filepath.exists()
        ):

            self.stats.skipped += 1
            return

        try:

            tts = gTTS(
                text=phrase.english,
                lang=self.settings.voice_lang,
                slow=self.settings.voice_slow,
            )

            tts.save(str(filepath))

            self.stats.generated += 1

        except Exception as e:

            self.stats.errors += 1

            Logger.exception(str(e))