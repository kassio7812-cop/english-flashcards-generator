"""
lesson.py

Modelos de dados do English Flashcards Generator.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Phrase:
    """
    Representa uma frase.
    """

    id: int

    english: str

    portuguese: str

    level: str = ""

    category: str = ""

    notes: str = ""

    def __post_init__(self):

        self.english = self.english.strip()

        self.portuguese = self.portuguese.strip()

        self.level = self.level.strip()

        self.category = self.category.strip()

        self.notes = self.notes.strip()


@dataclass(slots=True)
class Lesson:
    """
    Representa uma lição.
    """

    name: str

    filename: str

    phrases: list[Phrase] = field(default_factory=list)

    @property
    def total(self):

        return len(self.phrases)

    def add(self, phrase: Phrase):

        self.phrases.append(phrase)

    def __iter__(self):

        return iter(self.phrases)