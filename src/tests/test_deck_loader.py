from pathlib import Path

from deck_loader import DeckLoader


def test_create_deck():
    loader = DeckLoader()
    loader.create_deck("software_testing")

    assert Path("decks/software_testing.csv").is_file()


def test_headers_are_present():
    loader = DeckLoader()
    loader.create_deck("software_testing")

    # will need to be refactored
    assert Path("decks/software_testing.csv").read_text().startswith("question,answer\n")
