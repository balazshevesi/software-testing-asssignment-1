from deck_loader import DeckLoader


class App:
    def __init__(self, loader=None):
        self.current_page = "welcome"
        self.current_deck = None
        self.loader = DeckLoader() if loader is None else loader

    def loop(self):
        keep_going = True
        while keep_going:
            self.router()

    def router(self):
        pages = {
            "welcome": self.page_welcome,
            "deck_selector": self.page_deck_selector,
            "deck_editor": self.page_deck_editor,
            "deck_content_editor": self.page_deck_content_editor,
            "deck_review": self.page_deck_review,
        }
        if self.current_page in pages: pages[self.current_page]()
        else: self.page_not_found()

    def page_not_found(self):
        # print("404: Page not found")
        # self.current_page = "welcome"
        pass

    def page_welcome(self):
        choice = input("Welcome!\n1. Select a deck\nEnter your choice: ")
        if choice == "1":
            self.current_page = "deck_selector"

    def page_deck_selector(self):
        decks = self.loader.list_decks()
        for number, name in enumerate(decks, start=1):
            print(f"{number}. {name}")
        choice = input("Select a deck by number: ").strip()
        for number, name in enumerate(decks, start=1):
            if choice == str(number):
                self.current_deck = self.loader.load_deck(name)
                self.current_page = "deck_review"
                break

    def page_deck_editor(self):
        pass

    def page_deck_content_editor(self):
        pass

    def page_deck_review(self):
        print(f"Reviewing {self.current_deck.name}")

if __name__ == "__main__":
    app = App()
    app.loop()
