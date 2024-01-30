import random

class PokerCard:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        suits = ['H', 'D', 'C', 'S']
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
        return [str(card) for card in self.hand]

class LandlordGame:
    def __init__(self, players):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = [Player(player) for player in players]
        self.landlord = None

    def deal_cards(self):
        for _ in range(3):
            for player in self.players:
                player.add_cards(self.deck.deal(1))

    def bid_landlord(self):
        for player in self.players:
            print(f"{player.name}, do you want to be the landlord? (y/n)")
            choice = input().lower()
            if choice == 'y':
                self.landlord = player
                break

    def play_round(self):
        for player in self.players:
            print(f"\n{player.name}'s Hand: {player.show_hand()}")
            print(f"{player.name}, it's your turn. Enter the cards you want to play (e.g., '3H 4D AH'): ")
            cards_to_play = input().split()
            # 在实际游戏中需要添加出牌的合法性检查和规则判断的逻辑
            # 简化版中假设玩家输入合法的牌，不做检查
            cards_to_play = [PokerCard(card[1], card[0]) for card in cards_to_play]
            player.hand = [card for card in player.hand if card not in cards_to_play]

    def play(self):
        self.deal_cards()
        self.bid_landlord()

        for _ in range(2):  # 简化版，只模拟两轮出牌
            self.play_round()

if __name__ == "__main__":
    players = ['Player 1', 'Player 2', 'Player 3']
    game = LandlordGame(players)
    game.play()
