
import random
from collections import Counter


def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\n--- Number Guessing Game ---")
    print("Guess a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                score = max(100 - (attempts - 1) * 10, 10)
                print("Congratulations! You guessed correctly.")
                print("Attempts:", attempts)
                print("Score:", score)
                break

        except ValueError:
            print("Please enter a valid whole number.")


def word_counter():
    print("\n--- File-Based Word Counter ---")
    filename = input("Enter text filename (e.g., sample.txt): ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        words = text.lower().split()
        cleaned_words = [
            word.strip(".,!?;:\"'()[]{}")
            for word in words
        ]
        cleaned_words = [word for word in cleaned_words if word]

        frequency = Counter(cleaned_words)

        print("Total words:", len(words))
        print("Unique words:", len(frequency))
        print("\nWord Frequency:")

        for word, count in frequency.items():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("File not found. Check the filename.")
    except OSError:
        print("Unable to read the file.")


def main():
    while True:
        print("\n=== Number Game & Word Counter ===")
        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            word_counter()
        elif choice == "3":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
