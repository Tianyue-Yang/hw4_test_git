import unittest
import hw4_cards as cards

# SI 507 Winter 2020
# Homework 4 - Code

#########################################
##### Name: Tianyue Yang       #####
##### Uniqname: tianyuey       #####
#########################################

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)

    # Add methods below to test main assignments. 
    def test_1_queen(self):
        """Test that if you create a card with rank 12, its rank_name will be "Queen"
        """
        card = cards.Card(rank=12)
        self.assertEqual(card.rank_name, "Queen")

    def test_2_clubs(self):
        """Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        """
        c2 = cards.Card(suit=1)
        self.assertEqual(c2.suit_name, "Clubs")

    def test_3_str(self):
        """Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"
        """
        c3 = cards.Card(3, 13)
        self.assertEqual(c3.__str__(), "King of Spades")

    def test_4_deck(self):
        """Test that if you create a deck instance, it will have 52 cards in its cards instance variable
        """
        d4 = cards.Deck()
        self.assertEqual(len(d4.cards), 52)

    def test_5_deal(self):
        """Test that if you invoke the deal_card method on a deck, it will return a card instance.
        """
        deck = cards.Deck()
        self.assertIsInstance(deck.deal_card(), cards.Card)

    def test_6_fewer(self):
        """Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.
        """
        d6 = cards.Deck()
        num_ori = len(d6.cards)
        d6.deal_card()
        num_after = len(d6.cards)
        self.assertEqual(num_ori-1, num_after)

    def test_7_more(self):
        """Test that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)
        """
        d7 = cards.Deck()
        poped_card = d7.deal_card()
        num_before = len(d7.cards)
        d7.replace_card(poped_card)
        num_new = len(d7.cards)
        self.assertEqual(num_new-1, num_before)

    def test_8_replace(self):
        """Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)
        """
        c8 = cards.Card()
        d8 = cards.Deck()
        num_deck = len(d8.cards)
        if c8 in d8.cards:
            d8.replace_card(c8)
            num_not_affected = len(d8.cards)
            self.assertEqual(num_deck, num_not_affected)


############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()
