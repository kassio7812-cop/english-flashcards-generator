"""
lesson_loader.py

Carrega todas as lições do projeto.
"""

from __future__ import annotations

import csv

from pathlib import Path

from scripts.lesson import (
    Lesson,
    Phrase,
)

from scripts.config import LESSONS_DIR


class LessonLoader:

    """
    Carrega todos os CSV da pasta lessons.
    """

    REQUIRED_COLUMNS = (

        "id",

        "english",

        "portuguese",

    )

    def load(self):

        lessons = []

        if not LESSONS_DIR.exists():

            return lessons

        files = sorted(

            LESSONS_DIR.glob("*.csv")

        )

        for csv_file in files:

            lesson = self.load_file(csv_file)

            lessons.append(lesson)

        return lessons

    def load_file(self, file: Path):

        lesson = Lesson(

            name=file.stem,

            filename=file.name,

        )

        with open(

            file,

            newline="",

            encoding="utf-8",

        ) as csvfile:

            reader = csv.DictReader(csvfile)

            self.validate_columns(reader.fieldnames)

            for row in reader:

                phrase = Phrase(

                    id=int(row["id"]),

                    english=row["english"],

                    portuguese=row["portuguese"],

                    level=row.get(

                        "level",

                        "",

                    ),

                    category=row.get(

                        "category",

                        "",

                    ),

                    notes=row.get(

                        "notes",

                        "",

                    ),

                )

                lesson.add(phrase)

        return lesson

    def validate_columns(self, columns):

        if columns is None:

            raise ValueError(

                "CSV vazio."

            )

        for required in self.REQUIRED_COLUMNS:

            if required not in columns:

                raise ValueError(

                    f"Coluna obrigatória ausente: {required}"

                )