# Number Guessing Game

import random

def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")
    
    while attempts < max_attempts:
        try:
            # Get the player's guess
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue
                
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\nCongratulations! You've guessed the number in {attempts} attempts!")
                return True
                
            # Show remaining attempts
            if attempts < max_attempts:
                print(f"You have {max_attempts - attempts} attempts left.\n")
            
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"\nGame Over! The number was {secret_number}.")
    return False

def main():
    while True:
        play_game()
        
        # Ask if player wants to play again
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break
        print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    main()
