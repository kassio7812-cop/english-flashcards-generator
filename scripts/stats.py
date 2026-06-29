"""
stats.py

Estatísticas da execução.
"""

from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter


@dataclass(slots=True)
class Stats:

    lessons: int = 0

    phrases: int = 0

    generated: int = 0

    skipped: int = 0

    anki_files: int = 0

    errors: int = 0

    _start: float = 0

    elapsed: float = 0

    def start(self):

        self._start = perf_counter()

    def stop(self):

        self.elapsed = perf_counter() - self._start

    def reset(self):

        self.lessons = 0

        self.phrases = 0

        self.generated = 0

        self.skipped = 0

        self.anki_files = 0

        self.errors = 0

        self.elapsed = 0