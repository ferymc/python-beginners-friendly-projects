import random
from colorama import init, Fore

init(autoreset=True)

print("------------------------------------")
print("Welcome to the number guessing game!")
print("------------------------------------")


while True:

    attempts = 0
    secret_number = random.randint(1, 100)

    while True:

        try:
            guess = int(input("Guess the number (1..100): "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1
        