"""
importer.py

Importa arquivos TXT para lições CSV.
"""

from __future__ import annotations

import csv
import shutil
from pathlib import Path

from scripts.config import (
    IMPORTS_DIR,
    LESSONS_DIR,
)
from scripts.logger import Logger
from scripts.parser_txt import TextParser


class LessonImporter:

    def __init__(self):

        self.parser = TextParser()

    # -------------------------------------------------

    def import_folder(
        self,
        folder: Path,
    ):

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        txt_files = sorted(
            folder.glob("*.txt")
        )

        if not txt_files:

            Logger.info(
                "Nenhum TXT encontrado."
            )

            return

        for file in txt_files:

            self.import_file(
                file
            )

    # -------------------------------------------------

    def import_file(
        self,
        filepath: Path,
    ):

        Logger.info(
            f"Importando {filepath.name}"
        )

        phrases = self.parser.parse(
            filepath
        )

        csv_name = (
            filepath.stem + ".csv"
        )

        csv_path = (
            LESSONS_DIR / csv_name
        )

        with open(
            csv_path,
            "w",
            newline="",
            encoding="utf-8-sig",
        ) as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow([
                "id",
                "english",
                "portuguese",
            ])

            for index, (
                english,
                portuguese,
            ) in enumerate(
                phrases,
                start=1,
            ):

                writer.writerow([
                    index,
                    english,
                    portuguese,
                ])

        Logger.info(
            f"Lição criada: {csv_name}"
        )

        processed = IMPORTS_DIR / "processed"

        processed.mkdir(
            parents=True,
            exist_ok=True,
        )

        shutil.move(
            str(filepath),
            str(processed / filepath.name),
        )

        Logger.info(
            f"Arquivo movido para {processed.name}"
        )