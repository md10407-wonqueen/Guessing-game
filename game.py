import random

number = random.randint(1, 10)
attempts = 0

while attempts < 5:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if guess == number:
        print("You guessed it!")
        break
    elif guess < number:
        print("Too small!")
    else:
        print("Too large!")

if guess != number:
    print(f"Sorry, the number was {number}.")
