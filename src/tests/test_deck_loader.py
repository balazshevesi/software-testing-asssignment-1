from pathlib import Path

from deck import Deck
from deck_loader import DeckLoader
from flashcard import Flashcard


# tests for "create_deck"

def test_create_deck():
    loader = DeckLoader()
    loader.create_deck("software_testing")

    assert Path("decks/software_testing.csv").is_file()

def test_headers_are_present():
    loader = DeckLoader()
    loader.create_deck("software_testing")

    # will need to be refactored
    assert Path("decks/software_testing.csv").read_text().startswith("question,answer\n")


# tests for "list_decks"
# tmp_path, monkeypatch are both provided by Pytest
def test_list_decks_when_empty(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    Path("decks").mkdir()
    loader = DeckLoader()
    assert loader.list_decks() == []

def test_list_decks_returns_deck_names(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    Path("decks").mkdir()
    Path("decks/biology.csv").touch()
    loader = DeckLoader()

    assert loader.list_decks() == ["biology"]

# tests for "load_deck"

def test_load_empty_deck(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    Path("decks").mkdir()
    Path("decks/biology.csv").write_text("question,answer\n")
    loader = DeckLoader()

    deck = loader.load_deck("biology")

    assert isinstance(deck, Deck)
    assert deck.name == "biology"
    assert deck.cards == []

def test_load_deck_with_one_flashcard(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    Path("decks").mkdir()
    Path("decks/biology.csv").write_text("question,answer\nWhat is DNA?,Genetic material\n")
    loader = DeckLoader()

    deck = loader.load_deck("biology")

    assert isinstance(deck, Deck)
    assert len(deck.cards) == 1
    assert deck.cards[0].question == "What is DNA?"
    assert deck.cards[0].answer == "Genetic material"

# tests for "save_deck"

def test_save_empty_deck(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    Path("decks").mkdir()
    loader = DeckLoader()
    deck = Deck("biology")

    loader.save_deck(deck)

    path = Path("decks/biology.csv")
    assert path.is_file()
    assert path.read_text() == "question,answer\n"

def test_save_deck_with_one_flashcard(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    Path("decks").mkdir()
    loader = DeckLoader()
    deck = Deck("biology")
    deck.cards.append(Flashcard("What is DNA?", "Genetic material"))

    loader.save_deck(deck)

    path = Path("decks/biology.csv")
    assert path.is_file()
    assert path.read_text() == "question,answer\nWhat is DNA?,Genetic material\n"
