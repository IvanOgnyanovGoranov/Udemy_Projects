import random
from art import logo


CARD_VALUES = {
    'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
    'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10
}

BLACKJACK_SCORE = 21
DEALER_HIT_THRESHOLD = 17
ACE_ADJUSTMENT = 10


def current_scores(player_cards, player_score, dealer_cards):
    return f"Your cards: {player_cards}, current score: {player_score}\n" +\
           f"Dealer's first card is: {dealer_cards[0]}"


def deal_card():
    cards = list(CARD_VALUES.keys())
    return random.choice(cards)


def check_for_ace(cards, score):
    if 'Ace' in cards and score > BLACKJACK_SCORE:
        return ACE_ADJUSTMENT
    return 0


# Dealing the first two cards to the Player and Dealer
def deal_initial_cards():
    p_cards = [deal_card() for _ in range(2)]
    d_cards = [deal_card() for _ in range(2)]
    p_score = sum(CARD_VALUES[card] for card in p_cards)
    d_score = sum(CARD_VALUES[card] for card in d_cards)
    p_score -= check_for_ace(p_cards, p_score)
    d_score -= check_for_ace(d_cards, d_score)
    return p_cards, d_cards, p_score, d_score


def player_turn(player_cards, player_score, dealer_cards):
    # Handling the case where we have 2 initial Aces in the cards.
    aces_in_deque = player_cards.count('Ace')
    aces_checked = 0
    if aces_in_deque == 2:
        aces_checked = 1

    while True:
        player_input = input("Type 'y' to get another card, type 'n' to pass:\n").lower()

        if player_input == 'n':
            return player_cards, player_score

        elif player_input == 'y':
            current_card = deal_card()
            player_cards.append(current_card)
            player_score += CARD_VALUES[current_card]
            aces_number = player_cards.count('Ace')
            if aces_checked < aces_number:
                result = check_for_ace(player_cards, player_score)
                if result == 10:
                    player_score -= result
                    aces_checked += 1

            print(current_scores(player_cards, player_score, dealer_cards))

            if player_score > BLACKJACK_SCORE:
                return player_cards, player_score

        else:
            print("Invalid input. Please type 'y' or 'n'.")


def dealer_turn(dealer_score, dealer_cards):
    # Handling the case where we have 2 initial Aces in the cards.
    aces_in_deque = dealer_cards.count('Ace')
    aces_checked = 0
    if aces_in_deque == 2:
        aces_checked = 1

    while dealer_score < DEALER_HIT_THRESHOLD:
        current_card = deal_card()
        dealer_cards.append(current_card)
        dealer_score += CARD_VALUES[current_card]

        aces_number = dealer_cards.count('Ace')
        if aces_checked < aces_number:
            result = check_for_ace(dealer_cards, dealer_score)
            if result == 10:
                dealer_score -= result
                aces_checked += 1

        if dealer_score > BLACKJACK_SCORE:
            return dealer_cards, dealer_score
    return dealer_cards, dealer_score


def determine_final_result(player_cards, player_score, dealer_cards, dealer_score):
    if dealer_score < player_score:
        return f"You win! You have: {player_cards} and a score of {player_score}\n"\
              f"The Dealer has: {dealer_cards} and a score of {dealer_score}"
    elif player_score == dealer_score:
        return f"It's a draw. You have: {player_cards} and a score of {player_score}\n"\
              f"The Dealer has: {dealer_cards} and a score of {dealer_score}"
    else:
        return f"You lose. You have: {player_cards} and a score of {player_score}\n"\
              f"The Dealer has: {dealer_cards} and a score of {dealer_score}"


def play_blackjack():
    print(logo)
    player_cards, dealer_cards, player_score, dealer_score = deal_initial_cards()
    print(current_scores(player_cards, player_score, dealer_cards))

    if dealer_score == BLACKJACK_SCORE:
        return "You lose. The Dealer wins with a BlackJack!" \
               f"His cards: {dealer_cards}. His score is {dealer_score}"

    if player_score == BLACKJACK_SCORE:
        return f"You win with a BlackJack!\n" \
               f"The Dealer has: {dealer_cards} and a score of {dealer_score}"

    # Player's turn. Returns result and determines if went over 21 in which case game ends.
    player_cards, player_score = player_turn(player_cards, player_score, dealer_cards)
    if player_score > 21:
        return f"You lose! You went over.\n" \
               f"The Dealer has: {dealer_cards} and a score of {dealer_score}"

    # Dealer's turn. Returns result and determines if went over 21 in which case game ends.
    if dealer_score < 17:
        dealer_cards, dealer_score = dealer_turn(dealer_score, dealer_cards)
    if dealer_score > 21:
        return f"You win! The Dealer went over.\n" \
               f"The Dealer has: {dealer_cards} and a score of {dealer_score}"

    # If there is no winner yet this function determines who is it.
    return determine_final_result(player_cards, player_score, dealer_cards, dealer_score)


while True:
    user_input = input("Do you want to play a game of Black Jack? Type 'y' or 'n'\n").lower()
    if user_input == "y":
        print(play_blackjack())

    elif user_input == 'n':
        print("See you soon!")
        break

    else:
        print("You need to type 'y' or 'n'")
