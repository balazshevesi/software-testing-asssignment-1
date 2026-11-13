import csv
from pathlib import Path

from deck import Deck
from flashcard import Flashcard


class DeckLoader:
    def __init__(self):
        pass

    def create_deck(self, name):
        deck = Path(f"decks/{name}.csv")
        if not deck.exists():
            deck.write_text("question,answer\n")

    def list_decks(self):
        decks = []
        for deck in Path("decks").glob("*.csv"):
            if deck.is_file():
                decks.append(deck.stem) #`.stem` gives the filename without its extension
        return decks

    def load_deck(self, name):
        deck = Deck(name)
        with Path(f"decks/{name}.csv").open(encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                card = Flashcard(row["question"], row["answer"])
                deck.cards.append(card)
        return deck

    def save_deck(self, deck):
        with Path(f"decks/{deck.name}.csv").open("w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["question", "answer"])
            for card in deck.cards:
                writer.writerow([card.question, card.answer])
