"""
utils.py

Funções auxiliares do projeto.
"""

from __future__ import annotations

from pathlib import Path


def elapsed(seconds: float) -> str:
    """
    Formata tempo de execução.
    """

    return f"{seconds:.2f} s"


def ensure_directory(path: Path):

    path.mkdir(
        parents=True,
        exist_ok=True
    )


def clean_text(text: str) -> str:
    """
    Remove espaços extras.
    """

    return text.strip()


def mp3_filename(number: int) -> str:
    """
    Retorna nome padronizado do MP3.
    """

    return f"{number:03}.mp3"


def csv_import_filename(lesson_name: str) -> str:
    """
    Nome do CSV do Anki.
    """

    return f"{lesson_name}_import.csv"