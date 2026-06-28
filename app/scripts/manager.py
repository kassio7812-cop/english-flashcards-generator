"""
manager.py

Coordena toda a execução do programa.
"""

from __future__ import annotations

from scripts.audio import AudioGenerator
from scripts.anki import AnkiGenerator
from scripts.console import Console
from scripts.lesson_loader import LessonLoader
from scripts.settings import Settings
from scripts.stats import Stats
from scripts.utils import elapsed
from scripts.version import (
    APP_NAME,
    VERSION,
)


class FlashcardManager:

    def __init__(self):

        self.settings = Settings()

        self.stats = Stats()

        self.loader = LessonLoader()

        self.audio = AudioGenerator(
            self.settings,
            self.stats,
        )

        self.anki = AnkiGenerator(
            self.stats,
        )

    def run(
        self,
        generate_audio: bool = True,
        generate_anki: bool = True,
        lesson_name: str | None = None,
    ):

        self.stats.start()

        Console.title(APP_NAME)

        Console.info(f"Version : {VERSION}")

        lessons = self.loader.load()

        if lesson_name:

            lessons = [
                lesson
                for lesson in lessons
                if lesson.name == lesson_name
            ]

        if not lessons:

            Console.warning(
                "Nenhuma lição encontrada."
            )

            return

        Console.separator()

        Console.info(
            f"Lições encontradas: {len(lessons)}"
        )

        if lesson_name:
            Console.info(
                f"Lição selecionada: {lesson_name}"
            )

        Console.separator()

        if generate_audio:

            Console.info("Gerando áudios...\n")

            self.audio.generate(
                lessons
            )

            Console.separator()

        if generate_anki:

            Console.info("Gerando arquivos do Anki...\n")

            self.anki.generate(
                lessons
            )

            Console.separator()

        self.stats.stop()

        self.summary()

    def summary(self):

        Console.title("RESUMO")

        Console.info(
            f"Lições.............: {self.stats.lessons}"
        )

        Console.info(
            f"Frases.............: {self.stats.phrases}"
        )

        Console.info(
            f"Áudios gerados.....: {self.stats.generated}"
        )

        Console.info(
            f"Áudios ignorados...: {self.stats.skipped}"
        )

        Console.info(
            f"Arquivos Anki......: {self.stats.anki_files}"
        )

        Console.info(
            f"Erros..............: {self.stats.errors}"
        )

        Console.info(
            f"Tempo..............: {elapsed(self.stats.elapsed)}"
        )

        Console.separator()

        Console.success(
            "Processamento concluído."
        )