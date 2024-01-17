import random
from art import logo
from art import vs
from game_data import data
from collections import deque


def check_result(celebrities, answer):
    """Returns True if answer is correct and False if it's wrong."""
    a, b = celebrities[0]['follower_count'], celebrities[1]['follower_count']
    if a > b:
        right_answer = "a"
    else:
        right_answer = "b"
    if right_answer == answer:
        return True
    return False


def ask_user_to_compare(celebrities):
    """Prints a string and asks user to compare. Returns the answer"""
    user_answer = input(f"Compare A: {celebrities[0]['name']}, {celebrities[0]['description']} "
                        f"from {celebrities[0]['country']}."
                        f"{vs}"
                        f"Against B: {celebrities[1]['name']}, {celebrities[1]['description']} "
                        f"from {celebrities[1]['country']}.\nType 'A' or 'B':")
    return user_answer.lower()


def find_celebrity():
    """Returns a random celebrity from the game_data file"""
    celebrity = random.choice(data)
    return celebrity

def play_game():
    print(logo)
    celebrities = deque(find_celebrity() for _ in range(2))
    score = 0

    while True:
        # Answer will be 'a' or 'b'
        answer = ask_user_to_compare(celebrities)
        # Result is True or False
        result = check_result(celebrities, answer)
        if result == False:
            return f"Sorry that's wrong. Final score: {score}"
        score += 1
        print(f"You are right! Current score: {score}")

        celebrities.popleft()
        celebrities.append(find_celebrity())

print(play_game())


