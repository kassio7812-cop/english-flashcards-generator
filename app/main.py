import argparse

from scripts.manager import FlashcardManager


def create_parser():

    parser = argparse.ArgumentParser(
        prog="English Flashcards Generator",
        description="Gerador de Flashcards"
    )

    parser.add_argument(
        "--audio",
        action="store_true",
        help="Gerar apenas os áudios"
    )

    parser.add_argument(
        "--anki",
        action="store_true",
        help="Gerar apenas os arquivos Anki"
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Gerar tudo"
    )

    parser.add_argument(
        "--lesson",
        type=str,
        help="Executar apenas uma lição"
    )

    return parser


def main():

    parser = create_parser()

    args = parser.parse_args()

    manager = FlashcardManager()

    # padrão: gerar tudo
    if not (
        args.audio
        or args.anki
        or args.all
    ):
        manager.run(
            generate_audio=True,
            generate_anki=True,
            lesson_name=args.lesson,
        )
        return

    if args.audio:

        manager.run(
            generate_audio=True,
            generate_anki=False,
            lesson_name=args.lesson,
        )

    elif args.anki:

        manager.run(
            generate_audio=False,
            generate_anki=True,
            lesson_name=args.lesson,
        )

    else:

        manager.run(
            generate_audio=True,
            generate_anki=True,
            lesson_name=args.lesson,
        )


if __name__ == "__main__":
    main()