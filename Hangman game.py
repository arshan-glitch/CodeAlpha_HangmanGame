import random

# List of 5 predefined words
words = ["python", "laptop", "coding", "school", "gaming"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

# Game loop
while incorrect_guesses > 0:

    # Display the current word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the word is completely guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Check whether input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess! 👍")
    else:
        incorrect_guesses -= 1
        print("Wrong guess! ❌")
        print("Remaining guesses:", incorrect_guesses)

# If player runs out of guesses
if incorrect_guesses == 0:
    print("\nGame Over! 💀")
    print("The correct word was:", word)