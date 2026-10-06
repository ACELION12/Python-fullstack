import random

secret_number = random.randint(1, 10)
attempts = 3

print("guess the number You have 3 attempts.")

for attempt in range(1, attempts + 1):
    try:
        guess = int(input(f"Attempt {attempt}: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    if guess == secret_number:
        print("You guessed it!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Out of attempts! The number was {secret_number}.")