import random

class PokerCard:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [PokerCard(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num):
        return [self.cards.pop() for _ in range(num)]

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_cards(self, cards):
        self.hand.extend(cards)

    def show_hand(self):
        for card in self.hand:
            print(card)

class LandlordGame:
    def __init__(self, players):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = [Player(player) for player in players]

    def deal_cards(self):
        for _ in range(17):
            for player in self.players:
                player.add_cards(self.deck.deal(1))

    def play(self):
        for player in self.players:
            print(f"\n{player.name}'s Hand:")
            player.show_hand()

if __name__ == "__main__":
    players = ['Player 1', 'Player 2', 'Player 3']
    game = LandlordGame(players)
    game.deal_cards()
    game.play()
