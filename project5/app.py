# Hangman Game
import random
from words import words

HANGMANPICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\\  |
 / \\  |
     ===''']

secret_word = random.choice(words["data"])

# Intialize the Game Variables

guessed_letters = []
tries = 0
max_tries = len(HANGMANPICS) - 1

while tries < max_tries:
    # Display the current hangman stage
    print(HANGMANPICS[tries])

    # Display the word with guessed letter
    display_word = ''
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter +  " "
        else:
            display_word += "_"
    print(f"Word: {display_word.strip()}")
    
    # Check for win condition
    if display_word == secret_word:
        print("Congratulations! You've guessed the word correctly.")
        break

    # Prompt the user for a guess
    guess = input("Guess a letter: ".lower())

    # Validate input
    if len(guess) != 1 and not guess.isalpha():
        print("Please enter a single-alphabetical character.")
        continue

    # Check if letter has already been guessed
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue
    
    # Add guess to guessed_letters
    guessed_letters.append(guess)

    # Check if guess is in secret word
    if guess not in secret_word:
        print(f"The letter {guess} is not in the word.")
        tries += 1
else:
    print(HANGMANPICS[tries])
    print(f"Game Over! The word was '{secret_word}'.")