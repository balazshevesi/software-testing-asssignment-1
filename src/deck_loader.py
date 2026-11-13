from pathlib import Path


class DeckLoader:
    def __init__(self):
        pass

    def create_deck(self, name):
        deck = Path(f"decks/{name}.csv")
        if not deck.exists():
            deck.write_text("question,answer\n")

    def list_decks(self):
        pass

    def load_deck(self, name):
        pass

    def save_deck(self, deck):
        pass
