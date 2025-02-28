import art
import random

def compare_number(guess, number, attempt):
    if guess > number:
        print("Too high.\nGuess again.")
        return attempt - 1
    elif guess < number:
        print("Too low.\nGuess again.")
        return attempt - 1
    else:
        print(f"You got it! The answer was {number}")
        return 0

number = random.randint(1, 100)

print(art.logo)
print("Welcome to Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

attempt = 10 if difficulty == "easy" else 5

while attempt > 0:
    print(f"You have {attempt} attempts remaining to guess the number.")

    guess_number = int(input("Make a guess: "))
    attempt = compare_number(guess_number, number, attempt)

    if guess_number == number:
        break

    if attempt == 0:
        print(f"You've run out of guesses. The number was {number}.")