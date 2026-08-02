import random
from colorama import init, Fore

init(autoreset=True)

print("------------------------------------")
print("Welcome to the number guessing game!")
print("------------------------------------")

# Building outer loop to continue the game
while True:

    attempts = 0
    secret_number = random.randint(1, 100)

    # Checking for the correct input type
    while True:

        try:
            guess = int(input("Guess the number (1...100): "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess == secret_number:
            print(Fore.GREEN + "Correct! You won!")
            break

        if attempts == 5:
            print(Fore.RED + f"Oops! You lost. The secret number was {secret_number}")
            break

        if guess > secret_number:
            print(f"Try a smaller number. (only {5 - attempts} chance left!)")

        else:
            print(f"Try a bigger number. (only {5 - attempts} chance left!)")

    # Question to continue the game by removing spaces and making the letters smaller
    again = input("Do you want to play again? (y/n): ").strip().lower()

    if again != "y":
        break
