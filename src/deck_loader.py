from pathlib import Path


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
        pass

    def save_deck(self, deck):
        pass
