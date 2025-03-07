import art
import game_data
import random

# Function to randomly choose a dictionary from game_data
def choose():
    return random.choice(game_data.data)

# Function to choose a new competitor that is different from the current one
def choose_against(compare):
    new_against = choose()
    while compare == new_against:   # Ensure the two choices are not the same
        new_against = choose()
    return new_against

# Function to compare follower counts between two competitors
def compare_followers(a, b):
    return a > b

# Display game logo
print(art.logo)

# Initialize game variables
score = 0
play = True
compare = choose()
against = choose_against(compare)

# Main game loop
while play:
    # Display the two competitors without revealing follower counts
    print(f"Compare A: {compare['name']}, {compare['description']}, {compare['country']}")
    print(art.vs)
    print(f"Against B: {against['name']}, {against['description']}, {against['country']}")

    # Get user input and clear the console for better readability
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Determine if the user's guess is correct
    correct = compare_followers(compare['follower_count'], against['follower_count'])

    if (guess == "a" and correct) or (guess == "b" and not correct):
        # User is correct, update score
        score += 1

        # If B was the correct answer, B becomes the new A
        if not correct:
            compare = against   # The previous 'against' becomes the new 'compare'

        against = choose_against(compare)   # Choose a new 'against'

        print("\n" * 20)
        print(art.logo)
        print(f"You're right! Current score: {score}")
    else:
        # User is wrong, end the game
        print("\n" * 20)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break