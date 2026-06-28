"""
lesson_loader.py

Localiza automaticamente todas as lições.
"""

from pathlib import Path

from scripts.lesson import Lesson

from scripts.config import (
    FRASES_DIR,
    AUDIOS_DIR
)


class LessonLoader:

    def load(self):

        lessons = []

        arquivos = sorted(
            FRASES_DIR.glob("*.csv")
        )

        for csv_file in arquivos:

            nome = csv_file.stem

            lesson = Lesson(

                name=nome,

                csv_file=csv_file,

                audio_folder=AUDIOS_DIR / nome

            )

            lesson.ensure_audio_folder()

            lesson.total_phrases = self.count_phrases(
                csv_file
            )

            lessons.append(
                lesson
            )

        return lessons

    def count_phrases(self, csv_file: Path):

        with open(
            csv_file,
            encoding="utf-8"
        ) as file:

            linhas = file.readlines()

        if len(linhas) <= 1:
            return 0

        return len(linhas) - 1