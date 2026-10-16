import random

words = ["PYTHON", "COMPUTER", "PROGRAM", "CODING", "SOFTWARE"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0

display = []

for letter in word:
    display.append("_")

print("Welcome to Hangman!")
print("The word has", len(word), "letters.")
print(" ".join(display))

while True:
    guess = input("Guess a letter: ").upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid guess! Enter one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct! 🎉")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

        print(" ".join(display))

    else:
        print("Wrong guess!")
        wrong_guesses += 1

        remaining_attempts = 6 - wrong_guesses
        print("Attempts remaining:", remaining_attempts)

        if wrong_guesses >= 6:
            print("Game over! 😥")
            print("The word was:", word)
            break

    if "_" not in display:
        print("Congratulations! You guessed the word! 🎉")
        break
