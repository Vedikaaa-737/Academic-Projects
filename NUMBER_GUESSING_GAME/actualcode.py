import random

def number_guessing_game():
    # Step 1: Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Step 2: Set up the number of guesses counter
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Try to guess it.")
    
    # Step 3: Loop until the player guesses correctly
    while True:
        try:
            # Step 4: Ask the player for their guess
            guess = int(input("Enter your guess: "))
            attempts += 1  # Increment attempts
            
            # Step 5: Check if the guess is correct, too high, or too low
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break  # Exit the loop when the guess is correct
        except ValueError:
            print("Please enter a valid number.")
    
# Call the function to start the game
number_guessing_game()
