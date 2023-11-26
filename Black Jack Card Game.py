import random

# Function to calculate the value of a hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        if card in ["jack", "queen", "king"]:
            value += 10
        elif card == "ace":
            value += 11
            num_aces += 1
        else:
            value += int(card)

    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1

    return value

# Deck of cards
deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"] * 4

# Initialize player and dealer hands
player_hand = []
dealer_hand = []

# Deal initial cards
for _ in range(2):
    player_hand.append(random.choice(deck))
    dealer_hand.append(random.choice(deck))

print("Welcome to Blackjack!")

while True:
    print("Player's hand:", player_hand)
    print("Dealer's hand:", [dealer_hand[0], "unknown"])

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if player_value == 21:
        print("Blackjack! You win!")
        break

    if player_value > 21:
        print("Bust! Dealer wins.")
        break

    action = input("Do you want to 'hit' or 'stand'? ").lower()

    if action == "hit":
        player_hand.append(random.choice(deck))
    elif action == "stand":
        while dealer_value < 17:
            dealer_hand.append(random.choice(deck))
            dealer_value = calculate_hand_value(dealer_hand)

        print("Dealer's hand:", dealer_hand)

        if dealer_value > 21:
            print("Dealer busts! You win!")
        elif dealer_value > player_value:
            print("Dealer wins.")
        elif player_value > dealer_value:
            print("You win!")
        else:
            print("It's a tie!")

        break
    else:
        print("Invalid action. Please enter 'hit' or 'stand'.")
