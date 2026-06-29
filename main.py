"""
main.py

Ponto de entrada do English Flashcards Generator.
"""

from __future__ import annotations

import argparse

from scripts.logger import Logger
from scripts.manager import FlashcardManager
from scripts.new_lesson import LessonCreator


Logger.setup()


def create_parser() -> argparse.ArgumentParser:
    """
    Cria o parser da linha de comando.
    """

    parser = argparse.ArgumentParser(
        prog="English Flashcards Generator",
        description="Gerador de Flashcards de Inglês",
    )

    parser.add_argument(
        "--audio",
        action="store_true",
        help="(Em desenvolvimento) Gerar apenas os áudios.",
    )

    parser.add_argument(
        "--anki",
        action="store_true",
        help="(Em desenvolvimento) Gerar apenas os arquivos do Anki.",
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Gerar todos os arquivos.",
    )

    parser.add_argument(
        "--lesson",
        type=str,
        metavar="NOME",
        help="(Em desenvolvimento) Processar apenas uma lição.",
    )

    parser.add_argument(
        "--new",
        metavar="NOME",
        type=str,
        help="Criar uma nova lição.",
    )

    return parser


def main() -> None:
    """
    Executa o programa.
    """

    parser = create_parser()

    args = parser.parse_args()

    # --------------------------------------------------
    # Criar nova lição
    # --------------------------------------------------

    if args.new:

        LessonCreator().create(args.new)

        return

    # --------------------------------------------------
    # Executar geração
    # --------------------------------------------------

    manager = FlashcardManager()

    manager.run()


if __name__ == "__main__":
    main()