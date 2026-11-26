
class App:
    def __init__(self):
        self.current_page = "welcome"

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
        pass

    def page_deck_selector(self):
        pass

    def page_deck_editor(self):
        pass

    def page_deck_content_editor(self):
        pass

    def page_deck_review(self):
        pass
