from random import *

SUITS = {
    "Diamonds": 1,
    "Hearts": 2,
    "Spades": 3,
    "Clubs": 4
}

RANKS = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14
}


class PlayingCard:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.face_up = False
    
    def name(self):
        return " ".join([self.rank, "of", self.suit])
    
    def is_better_than(self, other_card):
        other_rank = RANKS[other_card.rank]
        our_rank = RANKS[self.rank]
        if our_rank > other_rank:
            return True
        if our_rank < other_rank:
            return False
        
        other_suit = RANKS[other_card.suit]
        our_suit = RANKS[self.suit]
        return (our_suit > other_suit)


class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(PlayingCard(rank, suit))
        self.shuffle()
    
    def add_card(self, card):
        self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def remove_top_card(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def card_by_index(self, index):
        try:
            return self.cards[index]
        except Exception:
            return None
    
    def remove_card(self):
        if not self.cards:
            return None
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()


class View:
    def prompt_for_new_player(self):
        new_player = input("Type name of player: ")
        if new_player == "":
            return None

        return new_player

    def show_player_and_hand(self, player_name, hand):
        print("[" + player_name + "]")
        for card in hand.cards:
            if card.face_up:
                print(card.name())
            else:
                print("(hidden card)")

    def prompt_for_flip_cards(self):
        print("")
        prompt = input("Ready to see who won?")
        return True

    def show_winner(self, winner_name):
        print("")
        print("Congratulations", winner_name, "!")

    def prompt_for_new_game(self):
        print("")
        while True:
            prompt = input("Play again? Y/N")
            if prompt == "Y":
                return True
            else:
                return False


class Controller:
    def __init__(self, deck, view):
        # Model
        self.players = []
        self.deck = deck
        # View
        self.view = view

    def start_game(self):
        self.deck.shuffle()
        for player in self.players:
            next_card = self.deck.remove_top_card()
            if next_card is not None:
                player.hand.add_card(next_card)

    def evaluate_game(self):
        best_candidate = None

        for player in self.players:
            if best_candidate is None:
                best_candidate = player
                continue

            if player.hand.card_by_index(0).is_better_than(best_candidate.hand.card_by_index(0)):
                best_candidate = player

        return best_candidate.name

    def run(self):
        while len(self.players) < 5:
            new_player = self.view.prompt_for_new_player()
            if new_player is None:
                break
            self.add_player(new_player)

        while True:
            self.start_game()
            for player in self.players:
                self.view.show_player_and_hand(player.name, player.hand)

            self.view.prompt_for_flip_cards()
            for player in self.players:
                for card in player.hand.cards:
                    card.face_up = True
                self.view.show_player_and_hand(player.name, player.hand)

            self.view.show_winner(self.evaluate_game())

            if not self.view.prompt_for_new_game():
                break

            self.rebuild_deck()