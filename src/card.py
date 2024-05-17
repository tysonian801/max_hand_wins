from enum import IntEnum

# define the priority/rank of each suit, higher number = higher value
class Suit(IntEnum):
    clubs = 1
    diamonds = 2
    hearts = 3
    spades = 4

# define the priority/rank of each card rank, higher number = higher value
class Rank(IntEnum):
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13
    ace = 14

# define a playing card class which contains rank and suit attributes
class PlayingCard:
    def __init__(self, rank: Rank, suit: Suit):
        if type(suit) == Suit:
            self._suit = suit
        else:
            raise ValueError('Invalid suit type. Ensure type Suit is used for suit argument')
        
        if type(rank) == Rank:
            self._rank = rank
        else:
            raise ValueError('Invalid card rank. Ensure type Rank is used for rank argument')
    
    def get_rank_name(self):
        return self._rank.name
    
    def get_suit_name(self):
        return self._suit.name
    
    def get_rank_value(self):
        return self._rank.value
    
    def get_suit_value(self):
        return self._suit.value
    
    def get_full_name(self):
        return self._rank.name + self._suit.name

    def get_owner(self):
        return self._owner