from pathlib import Path
import re

from scripts.config import LESSONS_DIR


class LessonCreator:

    def create(self, name: str):

        LESSONS_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        files = sorted(
            LESSONS_DIR.glob("*.csv")
        )

        number = len(files) + 1

        slug = (
            name.lower()
            .strip()
            .replace(" ", "_")
        )

        slug = re.sub(
            r"[^a-z0-9_]",
            "",
            slug,
        )

        filename = f"{number:03d}_{slug}.csv"

        filepath = LESSONS_DIR / filename

        if filepath.exists():
            print("❌ A lição já existe.")
            return

        with open(
            filepath,
            "w",
            encoding="utf-8",
            newline="",
        ) as f:

            f.write(
                "id,english,portuguese\n"
            )

            f.write("1,,\n")

        print()

        print(f"✅ Lição criada: {filename}")

        print(filepath)