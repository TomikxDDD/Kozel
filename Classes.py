import itertools
import math
import random

class Game:
    def __init__(self, num_of_players):
        self.num_of_players = num_of_players
        self.moves_in_round = math.floor(32/num_of_players)
        self.deck = []
        self.players = []
        self.num_of_rounds = 0

    def create_deck_of_cards(self):
        # make a deck of cards
        self.deck = list(itertools.product(range(7, 14), ['Srdce', 'Listy', 'Kule', 'Zaludy']))

        # get rid of spare cards if there are 3 or 5 players
        if self.num_of_players != 4:
            self.deck.remove((7, 'Zaludy')) # Deletes Zaludy 7
            self.deck.remove((8, 'Zaludy')) # Deletes Zaludy 8
        return self.deck

    def create_players(self):
        for i in range(self.num_of_players):
            player_name = input(f"Insert a name of the {i+1} player: ")
            self.players.append(Player(player_name))

class Round:
    def __init__(self):
        self.first_player = None
        self.isDoubled = False
        self.played_cards = []
        self.cards_to_player = None

    def choose_first_player(self, game):
        random.shuffle(game.players)
        return game.players[0]

    def deal_cards(self, game):
        random.shuffle(game.deck) # First of all, shuffle the deck of cards
        i = 0
        cards_for_one_player = math.floor(len(game.deck)/game.num_of_players)
        for player in game.players:
            player.cards_in_hand = game.deck[i:(i+1)*cards_for_one_player]
            i += 1



class Player:
    def __init__(self, name, score=0, balance=0):
        self.name = name
        self.score = score
        self.balance = balance
        self.cards_in_hand = []
        self.cards_on_table = []

    def choose_card(self):
        pass

    def count_points(self):
        pass


class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value