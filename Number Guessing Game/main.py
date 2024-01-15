from art import logo
import random

number = random.randint(1, 100)

DIFFICULTY = {"hard": 5, "easy": 10}


def guess_number(attempts):
    """Returns a string whether it's too low or too high and exits if the correct number is guessed."""
    number_guess = int(input(f"You have {attempts} remaining attempts to guess the number.\nMake a guess:"))
    if number_guess < number:
        print("Too low.\nGuess again.")
    elif number_guess > number:
        print("Too high.\nGuess again.")
    else:
        print(f"You got it! The answer was {number}")
        exit()


def play_game():
    """The main game logic inside the function."""
    choose_difficulty = input("Choose a difficulty: type 'easy' or 'hard'\n")
    attempts = DIFFICULTY[choose_difficulty]
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(number)
    while attempts:
        guess_number(attempts)
        attempts -= 1
    else:
        print("You've run out of guesses. You lose.")


play_game()

