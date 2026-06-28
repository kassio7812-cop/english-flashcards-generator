"""
anki.py

Gera o CSV de importação para o Anki.
"""

from __future__ import annotations

import csv
from pathlib import Path

from scripts.config import ANKI_DIR
from scripts.console import Console
from scripts.csv_reader import CsvReader
from scripts.stats import Stats


class AnkiGenerator:

    def __init__(self, stats: Stats):

        self.stats = stats
        self.reader = CsvReader()

    def generate(self, lessons):

        ANKI_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        for lesson in lessons:

            self.generate_lesson(lesson)

    def generate_lesson(self, lesson):

        phrases = self.reader.read(
            lesson.csv_file
        )

        output = (
            ANKI_DIR /
            f"{lesson.name}_import.csv"
        )

        with open(
            output,
            "w",
            newline="",
            encoding="utf-8-sig",
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "English",
                    "Portuguese",
                    "Audio",
                ]
            )

            for phrase in phrases:

                filename = (
                    f"{phrase['id']:03}.mp3"
                )

                writer.writerow(
                    [
                        phrase["english"],
                        phrase["portuguese"],
                        f"[sound:{filename}]",
                    ]
                )

        self.stats.anki_files += 1

        Console.success(
            f"{output.name} criado"
        )