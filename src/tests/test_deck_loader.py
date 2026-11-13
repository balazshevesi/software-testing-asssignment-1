from pathlib import Path

from deck_loader import DeckLoader


def test_create_deck():
    loader = DeckLoader()
    loader.create_deck("software_testing")

    assert Path("decks/software_testing.csv").is_file()
