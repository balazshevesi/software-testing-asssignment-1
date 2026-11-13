from pathlib import Path


class DeckLoader:
    def __init__(self):
        pass

    def create_deck(self, name):
        Path(f"decks/{name}.csv").touch()

    def list_decks(self):
        pass

    def load_deck(self):
        pass

    def add_flash_card_to_deck(self):
        pass

    def remove_flash_card_from_deck(self):
        pass
