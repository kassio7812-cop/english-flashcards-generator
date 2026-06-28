"""
stats.py
Controle das estatísticas da execução.
"""

from dataclasses import dataclass
import time


@dataclass
class Stats:

    lessons: int = 0

    phrases: int = 0

    generated: int = 0

    skipped: int = 0

    anki_files: int = 0

    errors: int = 0

    warnings: int = 0

    start_time: float = 0

    end_time: float = 0

    def start(self):

        self.start_time = time.perf_counter()

    def stop(self):

        self.end_time = time.perf_counter()

    @property
    def elapsed(self):

        return self.end_time - self.start_time

    def summary(self):

        return {

            "lessons": self.lessons,

            "phrases": self.phrases,

            "generated": self.generated,

            "skipped": self.skipped,

            "anki_files": self.anki_files,

            "errors": self.errors,

            "warnings": self.warnings,

            "elapsed": self.elapsed

        }