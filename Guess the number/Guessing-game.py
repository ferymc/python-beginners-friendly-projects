import random
from colorama import init, Fore

init(autoreset=True)

print("------------------------------------")
print("Welcome to the number guessing game!")
print("------------------------------------")

# ساخت حلقه بیرونی برای ادامه بازی
# Building outer loop to continue the game
while True:

    attempts = 0
    secret_number = random.randint(1, 100)

    # چک کردن برای نوع ورودی صحیح
    # Checking for the correct input type
    while True:

        try:
            guess = int(input("Guess the number (1...100): "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        # انجام عملیات حدس‌ها
        # Guessing operations
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess == secret_number:
            print(Fore.GREEN + "Correct! you won.")
            break

        if attempts == 5:
            print(Fore.RED + f"Oops! you lose... the secret number was {secret_number}")
            break

        if guess > secret_number:
            print(f"It's smaller (only {5 - attempts} chance left!)")

        else:
            print(f"It's bigger (only {5 - attempts} chance left!)")
    # پرسش برای ادامه بازی با حذف فاصله‌ها و کوچک کردن حروف
    again = input("Do you want to play again? (y/n): ").strip().lower()

    if again != "y":
        break
