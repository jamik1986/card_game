import random


def create_deck():
    suits = ["♥", "♦", "♣", "♠"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append((suit, rank))

    random.shuffle(deck)
    return deck

def draw_card(deck, num_cards):
    # hand_x = [deck.pop() for _ in range(num_cards) if deck] - easy way
    hand_x = []
    for _ in range(num_cards):
        if deck:
            y = deck.pop()
            hand_x.append(y)
    return hand_x


deck_of_cards = create_deck()


def show_card(card):
    print(",".join([f"{rank}{suit}" for suit, rank in card]))


while len(deck_of_cards) > 0:
    choice  = int(input("How many cards? "))
    hand = draw_card(deck_of_cards, choice)
    print(hand)
    show_card(hand)

print("We are out of cards")
