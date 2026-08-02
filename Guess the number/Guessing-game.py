import random
from colorama import init, Fore

init(autoreset=True)

print("------------------------------------")
print("Welcome to the number guessing game!")
print("------------------------------------")


while True:

    attempts = 0
    secret_number = random.randint(1, 100)

    