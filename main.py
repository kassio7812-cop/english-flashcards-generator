"""
main.py

Ponto de entrada do English Flashcards Generator.
"""

from __future__ import annotations

import argparse

from scripts.config import IMPORTS_DIR
from scripts.importer import LessonImporter
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
        help="Gerar apenas os áudios.",
    )

    parser.add_argument(
        "--anki",
        action="store_true",
        help="Gerar apenas os arquivos do Anki.",
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
        help="Processar apenas uma lição.",
    )

    parser.add_argument(
        "--new",
        type=str,
        metavar="NOME",
        help="Criar uma nova lição.",
    )

    parser.add_argument(
        "--import",
        dest="import_txt",
        action="store_true",
        help="Importar arquivos TXT da pasta imports.",
    )

    return parser


def main() -> None:
    """
    Executa o programa.
    """

    parser = create_parser()

    args = parser.parse_args()

    # --------------------------------------
    # Criar nova lição
    # --------------------------------------

    if args.new:

        creator = LessonCreator()

        creator.create(args.new)

        return

    # --------------------------------------
    # Importar arquivos TXT
    # --------------------------------------

    if args.import_txt:

        importer = LessonImporter()

        importer.import_folder(
            IMPORTS_DIR
        )

    # --------------------------------------
    # Executar o gerador
    # --------------------------------------

    manager = FlashcardManager()

    manager.run()


if __name__ == "__main__":
    main()