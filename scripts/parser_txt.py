"""
parser_txt.py

Converte um texto bilíngue para pares
(inglês / português).
"""

from __future__ import annotations

from pathlib import Path


class TextParser:
    """
    Lê um arquivo TXT contendo:

    English
    Português

    English
    Português

    ...

    e retorna uma lista de pares.
    """

    def parse(self, filepath: Path) -> list[tuple[str, str]]:

        with open(
            filepath,
            "r",
            encoding="utf-8",
        ) as file:

            lines = [
                line.strip()
                for line in file
                if line.strip()
            ]

        if len(lines) % 2 != 0:

            raise ValueError(
                "O arquivo possui uma quantidade ímpar de linhas."
            )

        phrases = []

        for i in range(0, len(lines), 2):

            english = lines[i]
            portuguese = lines[i + 1]

            phrases.append(
                (
                    english,
                    portuguese,
                )
            )

        return phrases