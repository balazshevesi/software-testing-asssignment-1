import csv
from pathlib import Path

from deck import Deck
from flashcard import Flashcard


DECKS_DIRECTORY = "decks"
CSV_HEADER = "question,answer\n"
ENCODING = "utf-8"

class DeckLoader:
    def __init__(self):
        pass

    def create_deck(self, name):
        deck = Path(DECKS_DIRECTORY) / f"{name}.csv"
        if not deck.exists():
            deck.write_text(CSV_HEADER)

    def list_decks(self):
        decks = []
        for deck in Path(DECKS_DIRECTORY).glob("*.csv"):
            if deck.is_file():
                decks.append(deck.stem) #`.stem` gives the filename without its extension
        return decks

    def load_deck(self, name):
        deck = Deck(name)
        path = Path(DECKS_DIRECTORY) / f"{name}.csv"
        with path.open(encoding=ENCODING, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                card = Flashcard(row["question"], row["answer"])
                deck.cards.append(card)
        return deck

    def save_deck(self, deck: Deck):
        with Path(f"{DECKS_DIRECTORY}/{deck.name}.csv").open("w", encoding=ENCODING, newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["question", "answer"])
            for card in deck.cards:
                writer.writerow([card.question, card.answer])
