from card import PlayingCard, CardRank, Suit
from random import shuffle
from player import Player

class Deck:
    def __init__(self):
        # initialize cards list attribute
        self._cards = []

        # fill the cards attribute with all 52 unique cards
        self.shuffle()
    
    def get_cards_remaining(self):
        return len(self._cards)
    
    def shuffle(self):
        all_ranks = list(CardRank)
        all_suits = list(Suit)

        # fill the cards attribute with all 52 unique cards
        for card_rank in all_ranks:
            for card_suit in all_suits:
                self._cards.append(PlayingCard(card_rank, card_suit))

        # randomize the order of the cards attribute
        shuffle(self._cards)
    
    def draw_cards(self, quantity: int, owner: Player):     
        # initialize hand list
        hand_drawn = []

        if type(quantity) == int:
            for i in range(quantity):
                if self.get_cards_remaining() <= 0:
                    return None
                else:
                    # return the first card in the deck and remove it from the list
                    card_drawn = self._cards.pop(0)

                    if type(owner) == Player:
                        # assign ownership of this card to the player it was dealt to
                        card_drawn._owner = owner

                        # only add the card to the hand_drawn list if all logic passes
                        hand_drawn.append(card_drawn)
                    else:
                        raise ValueError('Attempting to assign card ownerhip to an invalid object. Must be type Player.')
            return hand_drawn
        else:
            raise ValueError('draw_hand quantity must be an integer')
