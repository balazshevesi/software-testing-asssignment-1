from datetime import datetime, timezone
from unittest.mock import Mock

import pytest

from deck import Deck
from flashcard import Flashcard


def test_new_deck_has_name_and_no_cards():
    deck = Deck("biology")

    assert deck.name == "biology"
    assert deck.cards == []


def test_decks_have_separate_card_lists():
    biology = Deck("biology")
    chemistry = Deck("chemistry")
    biology.cards.append(Flashcard("What is DNA?", "Genetic material"))

    assert chemistry.cards == []


def test_add_card_to_empty_deck():
    deck = Deck("biology")
    card = Flashcard("What is DNA?", "Genetic material")

    deck.add_card(card)

    assert deck.cards == [card]
