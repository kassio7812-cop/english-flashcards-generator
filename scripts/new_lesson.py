from pathlib import Path
import csv

from scripts.config import LESSONS_DIR


class LessonCreator:

    def create(self, lesson_name: str):

        LESSONS_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        filename = lesson_name.strip()

        if not filename.endswith(".csv"):
            filename += ".csv"

        filepath = LESSONS_DIR / filename

        if filepath.exists():
            print(f"A lição já existe: {filename}")
            return

        with open(
            filepath,
            "w",
            newline="",
            encoding="utf-8",
        ) as f:

            writer = csv.writer(f)

            writer.writerow([
                "id",
                "english",
                "portuguese",
            ])

        print(f"Lição criada com sucesso:\n{filepath}")