"""
anki.py

Geração dos CSV para importação no Anki.
"""

from __future__ import annotations

import csv

from scripts.config import ANKI_DIR
from scripts.logger import Logger
from scripts.utils import (
    csv_import_filename,
    mp3_filename,
)


class AnkiGenerator:

    def __init__(self, stats):

        self.stats = stats

    # -------------------------------------------------

    def generate(self, lessons):

        ANKI_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        Logger.info("Gerando arquivos do Anki.")

        for lesson in lessons:
            self.generate_lesson(lesson)

    # -------------------------------------------------

    def generate_lesson(self, lesson):

        filename = csv_import_filename(lesson.name)

        filepath = ANKI_DIR / filename

        with open(
            filepath,
            "w",
            newline="",
            encoding="utf-8",
        ) as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow([
                "English",
                "Portuguese",
                "Audio",
                "Lesson",
            ])

            for phrase in lesson:

                writer.writerow([
                    phrase.english,
                    phrase.portuguese,
                    f"[sound:{mp3_filename(phrase.id)}]",
                    lesson.name,
                ])

        self.stats.anki_files += 1

        Logger.info(f"CSV criado: {filename}")