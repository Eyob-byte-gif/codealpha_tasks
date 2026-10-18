
import random

WORDS = ["PYTHON", "COMPUTER", "PROGRAM", "CODING", "SOFTWARE"]

HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]


def play_game():
    word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0
    display = ["_"] * len(word)

    print("\nWelcome to Hangman!")
    print("Guess the hidden word one letter at a time.")
    print(f"The word has {len(word)} letters.")

    while True:
        print(HANGMAN_STAGES[wrong_guesses])
        print("Word:", " ".join(display))
        print("Guessed letters:", ", ".join(guessed_letters) or "None")
        print(f"Attempts remaining: {6 - wrong_guesses}")

        guess = input("Guess a letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess! Enter one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            for i, letter in enumerate(word):
                if letter == guess:
                    display[i] = guess
        else:
            print("Wrong guess!")
            wrong_guesses += 1

        if "_" not in display:
            print("\nCongratulations! You guessed the word!")
            print("The word was:", word)
            return

        if wrong_guesses == 6:
            print(HANGMAN_STAGES[wrong_guesses])
            print("\nGame over! You lost.")
            print("The word was:", word)
            return


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()

        if again != "y":
            print("Thanks for playing Hangman!")
            break


if __name__ == "__main__":
    main()

