from src.deck import Deck
from src.player import Player, Cheater

class Game:
    def __init__(self, player_count: int, hand_size: int):
        # initialize list of players
        self._players = []
        # prompt user for 'player_count' number of player names
        for i in range(player_count):
            player_name = input(f'What is the name of player {i + 1}?: ')
            while len(player_name) > 20:
                print('Invalid name. Maximum of 20 characters, please choose another name.')
                player_name = input(f'What is the name of player {i + 1}?: ')
            # ensure each player name is unique
            while player_name in self.get_players_names():
                print(f'Invalid name. {player_name} already taken, please choose another name.')
                player_name = input(f'What is the name of player {i + 1}?: ')

            # prompts if player is a cheater
            is_cheater = input(f'Is this player an honest player?: (yes/no) ')

            # validates the is_cheater response is a valid response
            while type(is_cheater) != str or is_cheater.lower().strip() not in ['yes', 'no']:
                print('Response must be "yes" or "no", please enter a new value')
                is_cheater = input(f'Is this player an honest player?: (yes/no) ')
            
            # if this player is a cheater, create a player under the Cheater subclass
            if is_cheater.lower().strip() == 'no':
                self._players.append(Cheater(name=player_name))
            # if this player is not a cheater, create player under the standard Player class
            elif is_cheater.lower().strip() == 'yes':
                self._players.append(Player(name=player_name))

        # initialize a deck for the game
        self._deck = Deck()

        self._hand_size = hand_size
    
    def get_deck(self):
        return self._deck
    
    def get_players(self):
        return self._players
    
    def show_score(self):
        # add some whitespace for readability
        print()
        print('End of round score is: ')
        for player in self.get_players():
            print(f'  {player.get_name()} - {player.get_score()}')
    
    def get_players_names(self):
        players_names = []
        for player in self._players:
            players_names.append(player.get_name())
        
        return players_names
    
    def get_hand_size(self):
        return self._hand_size
    
    def show_player_cards(self):
        for player in self.get_players():
            player.print_cards_in_hand()
    
    def next_round(self):
        for player in self.get_players():
            player.set_hand(
                self.get_deck().draw_cards(
                    quantity=self.get_hand_size(), 
                    owner=player
                )
            )
    
    def end_round(self):
        strongest_cards_list = []
        
        for player in self.get_players():
            strongest_cards_list.append(player.strongest_hand())

        # sort the list of highest rank cards to find the winning card for the round
        strongest_cards_list.sort(
            key=lambda card: (card.get_rank_value(), card.get_suit_value()), reverse=True
        )

        # add a point for the player who won the round
        strongest_cards_list[0].get_owner().increment_score()

        # add some whitespace for readability
        print()
        # print a message for which card won the round and which player it belongs to
        print(
            f'Congratulations {strongest_cards_list[0].get_owner().get_name()}!',
            f'You win the round with "{strongest_cards_list[0].get_rank_name()}',
            f'of {strongest_cards_list[0].get_suit_name()}".'
        )

        # print cards in hand for each player
        self.show_player_cards()

        # print the end of round score
        self.show_score()

        # end the round and deal the next round
        self.next_round()
    
    def print_final_score(self):
        winning_players = []
        highest_score = 0
        
        for player in self.get_players():
            # if this player has a higher score than current highest_score, set them as the winner
            if player.get_score() > highest_score:
                winning_players = [player.get_name()]
                highest_score = player.get_score()
            # accounts for games where final score is tied
            elif player.get_score() == highest_score:
                winning_players.append(player.get_name())
            else:
                continue
        
        # add some whitespace for readability
        print()

        # initilaize declare_winner which will be overwritten based on number of winners
        declare_winner = ''
        # create string to append to winner declaration message
        if len(winning_players) > 1:
            print('GAME OVER: There was a tie! The winners are:')
            for player in winning_players:
                declare_winner += f'  {player}'
        else:
            declare_winner = f'GAME OVER: Congratulations {winning_players[0]}! You won the game!'
        
        print(declare_winner)
    
    @classmethod
    def play_game(cls):
        player_count = input('How many players would you like?: ')
        hand_size = input('How many cards would you like per hand? (default is 2): ')
        # start a new game with the input player count and hand size
        game = cls(int(player_count), int(hand_size))
        # deal the first round of cards
        game.next_round()
        # score the round and continue dealing more until the deck is gone
        while game.get_deck().get_cards_remaining() > 0:
            game.end_round()
            
            # add some whitespace for readability
            print()
            input('Press enter to continue.')
        
        # after all cards have been dealt, declare a winner
        game.print_final_score()