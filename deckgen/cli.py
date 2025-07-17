import argparse
from deckgen.decks.generator import DeckGen
from deckgen.pipelines.qa_pipeline import QAToolKit
from deckgen.text_processor.reader import Reader
from prompteng.prompts.parser import QAParser
import os
from typing import Optional
from dotenv import load_dotenv


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        prog="deckgen", description="Generate decks from text files."
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: generate
    generate_parser = subparsers.add_parser(
        "generate", help="Generate a deck from an input file."
    )
    generate_parser.add_argument(
        "--input-file",
        "-i",
        required=True,
        help="Path to the input file (e.g., .txt, .md). Defaults to input.txt",
    )
    generate_parser.add_argument(
        "--output",
        "-o",
        required=False,
        default="output.apkg",
        help='Directory to save the generated deck, by default "output.apkg"',
    )
    generate_parser.add_argument("--name", "-n", required=True, help="Name of the deck")

    # subcommand: auth
    auth_parser = subparsers.add_parser(
        "auth", help="Validate or set authentication with OpenAI API using an API key."
    )
    auth_parser.add_argument(
        "--api-key",
        "-k",
        required=False,
        help="OpenAI API key. If not provided, it will be read from the environment variable OPENAI_API_KEY.",
    )
    auth_parser.add_argument(
        "--openai-project-id",
        "-p",
        required=False,
        help="Validate OpenAI project ID. If not provided, it will be read from the environment variable OPENAI_API_PROJECT.",
    )
    auth_parser.add_argument(
        "--openai-organization-id",
        "-o",
        required=False,
        help="Validate OpenAI organization ID. If not provided, it will be read from the environment variable OPENAI_API_ORGANIZATION.",
    )

    args = parser.parse_args()

    if args.command == "generate":
        print(f"Generating deck from {args.input_file} with name {args.name}")
        generate_deck_from_file(
            input_file=args.input_file,
            deck_name=args.name,
            dst=args.output,
            deck_description=None,  # Optional description can be added later
        )
    elif args.command == "auth":

        os.environ["OPENAI_API_KEY"] = (
            args.api_key if args.api_key else os.getenv("OPENAI_API_KEY")
        )
        os.environ["OPENAI_API_PROJECT"] = (
            args.openai_project_id
            if args.openai_project_id
            else os.getenv("OPENAI_API_PROJECT", None)
        )
        os.environ["OPENAI_API_ORGANIZATION"] = (
            args.openai_organization_id
            if args.openai_organization_id
            else os.getenv("OPENAI_API_ORGANIZATION", None)
        )


def generate_deck_from_file(
    input_file: str,
    deck_name: str,
    dst: Optional[str] = None,
    deck_description: Optional[str] = None,
) -> None:
    """
    Generates a deck from the specified input file.

    :param input_file: Path to the input file.
    :param deck_name: Name of the deck to be generated.
    :param dst: Optional destination directory for the generated deck file.
        If not provided, the deck will be saved in the current directory.
    :param deck_description: Optional description for the deck.
    """

    reader = Reader(input_file)
    content = reader.read()
    print("Content read from file:", content)

    deck_gen = DeckGen(input_text=content)
    deck = deck_gen.generate_deck(
        deck_name=deck_name, deck_description=deck_description
    )

    print("Generated Deck:", deck.name)
    if not dst:
        dst = "output.apkg"
    deck.generate_anki_deck(dst)
