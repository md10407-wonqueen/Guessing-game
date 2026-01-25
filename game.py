import random

def main():
    number = random.randint(1, 100)

    while True:
        try:
            guess = int(input("Guess the number (1–100): "))
        except ValueError:
            continue

        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Correct!")
            break


if __name__ == "__main__":
    main()
