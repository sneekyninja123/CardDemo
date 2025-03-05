import unittest
from playing_card import Deck
from playing_card import PlayingCard

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_generate_deck(self):
        self.assertEqual(len(self.deck.cards), 52)
        ranks = [card.rank for card in self.deck.cards]
        suits = [card.suit for card in self.deck.cards]
        for rank in PlayingCard.RANKS:
            self.assertIn(rank, ranks)
        for suit in PlayingCard.SUITS:
            self.assertIn(suit, suits)

    def test_shuffle(self):
        original_deck = self.deck.cards.copy()
        self.deck.shuffle()
        self.assertNotEqual(original_deck, self.deck.cards)

    def test_draw_card(self):
        card = self.deck.draw_card()
        self.assertIsInstance(card, PlayingCard)
        self.assertEqual(len(self.deck.cards), 51)

    def test_draw_card_empty_deck(self):
        for _ in range(52):
            self.deck.draw_card()
        with self.assertRaises(ValueError):
            self.deck.draw_card()

if __name__ == '__main__':
    unittest.main()