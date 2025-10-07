"""
NUMBER GUESSING GAME 
-------------------------------------
Language: Python

Problem Statement:
Create a simple number guessing game where the computer randomly selects a number 
between a given range (say 1 to 100), and the player tries to guess it.

After each guess, the program tells the player whether their guess was too high, 
too low, or correct. The game continues until the player guesses the number.

-------------------------------------
FEATURES:
1. Random number generation using the 'random' module.
2. Looping until the player guesses correctly.
3. Feedback on each guess (too high / too low).
4. Keeps track of the number of attempts.
5. Option to play again after one round.

-------------------------------------
TIME COMPLEXITY:
- Each guess is O(1) operation.
- In the worst case, if the number range is N and you guess sequentially, 
  the complexity is O(N).
- Average case (binary-like guessing strategy) ≈ O(log N).

SPACE COMPLEXITY:
- O(1), since we only use a few variables.
"""

# Import random module to generate random numbers
import random

def play_game():
    # Computer selects a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize attempt counter
    attempts = 0

    print("\n Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it? Let's see how many tries it takes!\n")

    # Infinite loop until player guesses correctly
    while True:
        try:
            # Take user input
            guess = int(input(" Enter your guess: "))
            attempts += 1  # Count each attempt
            
            # Compare guess with secret number
            if guess < secret_number:
                print(" Too low! Try again.\n")
            elif guess > secret_number:
                print(" Too high! Try again.\n")
            else:
                # If correct guess
                print(f" Congratulations! You guessed it in {attempts} tries.")
                break

        except ValueError:
            # Handle non-integer input
            print(" Please enter a valid number!\n")

    # Ask if the user wants to play again
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    else:
        print("\n Thanks for playing! Goodbye!")

# Run the game
if __name__ == "__main__":
    play_game()
