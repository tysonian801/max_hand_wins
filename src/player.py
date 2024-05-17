from random import randint
from src.card import PlayingCard, CardRank, Suit

class Player:
    def __init__(self, name: str):
        self._name = name
        # initialize blank list attribute for cards in the player's hand
        self._hand = []
        # initialize player score attribute
        self._score = 0
    
    def set_hand(self, cards):
        # validates the cards argument to ensure its a list
        if type(cards) == list:
            # updates player hand to new cards argument
            self._hand = cards
            # assign ownership of the drawn cards to the player who drew them
            for card in self.get_hand():
                self.claim_card_ownership(card)
        else:
            return ValueError('cards list invalid argument for set_hand, must be a list of cards')
    
    def get_hand(self):
        return self._hand
    
    def print_cards_in_hand(self):
        hand_string = ''

        # for each card in hand, generate string to print it's proper name
        for i in range(len(self.get_hand())):
            hand_string += (
                self.get_hand()[i].get_rank_name() 
                + ' of ' 
                + self.get_hand()[i].get_suit_name()
            ).ljust(20)
        
        # print the player name and the cards in their hand, with indentation to help readability
        print(f'  {self.get_name()} hand contained: ')
        print(f'    {hand_string}')
    
    def get_name(self):
        return self._name
    
    def strongest_hand(self):
        # sort the hand based on rank (descending), then suit (descending) if a tie exists
        self._hand.sort(
            key=lambda card: (card.get_rank_value(), card.get_suit_value()), reverse=True
        )
        # return the first card in the hand, which will be the highest point value card
        return self._hand[0]
    
    def get_score(self):
        return self._score
    
    def increment_score(self):
        self._score += 1

    def claim_card_ownership(self, card: PlayingCard):
        PlayingCard._owner = self

class Cheater(Player):
    def __init__(self, name: str):
        super().__init__(name)

    def strongest_hand(self):
        # give 20% chance for cheater to add ace of spades to their hand
        if randint(0, 10) <= 2:
            print(f'\n{self.get_name()} snuck a card in their hand without anyone noticing.')
            self._hand.append(PlayingCard(rank=CardRank.ace, suit=Suit.spades))
            # assign ownership of the Ace of Spades to this player
            self.claim_card_ownership(self.get_hand()[-1])
        return super().strongest_hand()