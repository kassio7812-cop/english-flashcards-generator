"""
lesson.py
Representa uma lição do projeto.
"""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class Lesson:
    """
    Representa uma lição.
    """

    name: str
    csv_file: Path
    audio_folder: Path

    total_phrases: int = 0

    generated: int = 0
    skipped: int = 0

    def __str__(self):

        return self.name

    @property
    def csv_exists(self):

        return self.csv_file.exists()

    @property
    def audio_exists(self):

        return self.audio_folder.exists()

    def ensure_audio_folder(self):

        self.audio_folder.mkdir(
            parents=True,
            exist_ok=True
        )