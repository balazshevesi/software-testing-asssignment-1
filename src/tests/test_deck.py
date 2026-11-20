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


def test_get_due_cards_returns_only_due_cards():
    now = datetime(2026, 11, 20, tzinfo=timezone.utc)
    due_card = Mock(spec=Flashcard)
    due_card.is_due.return_value = True
    future_card = Mock(spec=Flashcard)
    future_card.is_due.return_value = False

    deck = Deck("comp sci")
    deck.add_card(due_card)
    deck.add_card(future_card)

    assert deck.get_due_cards(now) == [due_card]
    due_card.is_due.assert_called_once_with(now)
    future_card.is_due.assert_called_once_with(now)

def test_remove_card():
    deck = Deck("Advance DSA")
    card = Flashcard("What is the height of a binary tree?", "How many levels there are to the tree")
    deck.add_card(card)
    assert deck.cards == [card]
    deck.remove_card(card)
    assert deck.cards == []
