"""
lesson_loader.py

Carrega todas as lições do projeto.
"""

from __future__ import annotations

import csv
from pathlib import Path

from scripts.lesson import Lesson, Phrase
from scripts.config import LESSONS_DIR


class LessonLoader:
    """
    Carrega todos os arquivos CSV da pasta lessons.
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

        files = sorted(LESSONS_DIR.glob("*.csv"))

        for csv_file in files:

            try:

                lesson = self.load_file(csv_file)

                if lesson.total > 0:
                    lessons.append(lesson)

            except Exception as e:

                print(f"⚠ Erro em {csv_file.name}: {e}")

        return lessons

    def load_file(self, file: Path):

        lesson = Lesson(
            name=file.stem,
            filename=file.name,
        )

        with open(
            file,
            mode="r",
            encoding="utf-8-sig",
            newline="",
        ) as csvfile:

            sample = csvfile.read(1024)
            csvfile.seek(0)

            try:
                dialect = csv.Sniffer().sniff(
                    sample,
                    delimiters=",;"
                )
            except csv.Error:
                dialect = csv.excel

            reader = csv.DictReader(
                csvfile,
                dialect=dialect,
            )

            self.validate_columns(reader.fieldnames)

            for row in reader:

                if not row:
                    continue

                try:

                    phrase = Phrase(
                        id=int(row["id"]),
                        english=row["english"].strip(),
                        portuguese=row["portuguese"].strip(),
                        level=row.get("level", "").strip(),
                        category=row.get("category", "").strip(),
                        notes=row.get("notes", "").strip(),
                    )

                    lesson.add(phrase)

                except Exception as e:

                    print(
                        f"⚠ Linha inválida em {file.name}: {e}"
                    )

        return lesson

    def validate_columns(self, columns):

        if columns is None:

            raise ValueError("CSV vazio.")

        columns = [c.strip() for c in columns]

        for required in self.REQUIRED_COLUMNS:

            if required not in columns:

                raise ValueError(
                    f"Coluna obrigatória ausente: {required}"
                )