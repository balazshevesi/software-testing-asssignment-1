from unittest.mock import Mock, patch

import pytest

from deck_loader import DeckLoader
from main import App


# asks user to select deck
#   call loader

def test_welcome_selects_deck_selector_when_user_enters_one():
    app = App()

    with patch("builtins.input", return_value="1"):
        app.page_welcome()

    assert app.current_page == "deck_selector"


def test_loop_keeps_calling_router():
    class StopLoop(Exception): # exceptions interrupts python's loops
        pass

    app = App()
    with patch.object(app, "router", side_effect=[None, None, StopLoop]) as router: #replaces `app.router` with a mock
        with pytest.raises(StopLoop):
            app.loop()

    assert router.call_count == 3

def test_router_opens_welcome_page_on_startup():
    app = App()

    with patch.object(app, "page_welcome") as welcome:
        app.router()

    welcome.assert_called_once_with()

# capsys is a built-in pytest thing that captures text printed to the console
def test_deck_selector_displays_available_decks(capsys):
    loader = Mock(spec=DeckLoader)
    loader.list_decks.return_value = ["Biology", "Swedish"]
    app = App(loader=loader)

    app.page_deck_selector()

    output = capsys.readouterr().out
    assert "Biology" in output
    assert "Swedish" in output


def test_deck_selector_numbers_choices_starting_at_one(capsys):
    loader = Mock(spec=DeckLoader)
    loader.list_decks.return_value = ["Biology", "Swedish"]
    app = App(loader=loader)

    app.page_deck_selector()

    lines = capsys.readouterr().out.splitlines()
    assert "1. Biology" in lines
    assert "2. Swedish" in lines
