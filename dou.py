import random

# 初始化牌
def init_cards():
    suits = ['♠', '♥', '♣', '♦']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    cards = [suit + rank for suit in suits for rank in ranks]
    cards.append('小王')
    cards.append('大王')
    return cards

# 洗牌
def shuffle_cards(cards):
    random.shuffle(cards)

# 发牌
def deal_cards(cards):
    players = [[], [], []]
    for i in range(len(cards)):
        players[i % 3].append(cards[i])
    return players

# 显示手牌
def show_hand(player, hand):
    print(f"玩家{player + 1}的手牌：{' '.join(hand)}")

# 主函数
def main():
    cards = init_cards()
    shuffle_cards(cards)
    players = deal_cards(cards)
    for i in range(3):
        players[i].sort(key=lambda x: (x[1:], x[0]))
        show_hand(i, players[i])

if __name__ == "__main__":
    main()
