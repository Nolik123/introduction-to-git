import random

def number_guesser():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)

    print("Guess a number between 1 and 100:")

    # Keep asking the user for a guess until they get it right
    while True:
        guess = int(input())

        if guess < number:
            print("Too low. Try again:")
        elif guess > number:
            print("Too high. Try again:")
        else:
            print("You got it! The number was", number)
            break

number_guesser()
