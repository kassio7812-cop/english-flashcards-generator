"""
manager.py

Coordenador principal do English Flashcards Generator.
"""

from __future__ import annotations

from scripts.audio import AudioGenerator
from scripts.anki import AnkiGenerator
from scripts.backup import BackupManager
from scripts.console import Console
from scripts.lesson_loader import LessonLoader
from scripts.logger import Logger
from scripts.settings import Settings
from scripts.stats import Stats
from scripts.utils import elapsed
from scripts.version import (
    APP_NAME,
    VERSION,
)


class FlashcardManager:

    def __init__(self):

        Logger.setup()

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

        self.backup = BackupManager()

    # --------------------------------------------------

    def run(self):

        Console.title(APP_NAME)

        Console.info(
            f"Version: {VERSION}"
        )

        self.stats.start()

        lessons = self.loader.load()

        if not lessons:

            Console.warning(
                "Nenhuma lição encontrada."
            )

            return

        self.stats.lessons = len(lessons)

        self.stats.phrases = sum(
            lesson.total
            for lesson in lessons
        )

        Console.separator()

        Console.info(
            f"Lições encontradas: {self.stats.lessons}"
        )

        Console.separator()

        if self.settings.create_backup:

            backup = self.backup.create()

            if backup:

                Console.success(
                    f"Backup criado: {backup.name}"
                )

        Logger.info(
            "Iniciando geração dos áudios."
        )

        self.audio.generate(
            lessons
        )

        Logger.info(
            "Áudios finalizados."
        )

        Console.separator()

        self.anki.generate(
        lessons

        )

        Logger.info(
            "Arquivos do Anki finalizados."
            
        )

        self.stats.stop()

        self.summary()

    # --------------------------------------------------

    def summary(self):

     if (
        self.stats.generated == 0
        and self.stats.skipped > 0

     ):
            
        Console.success(
             "Todos os áudios já existem."
        )

        Console.line()

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

        Console.line()