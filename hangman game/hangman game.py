import random

# List of 5 predefined words
words = ["apple", "tiger", "python", "school", "laptop"]

# Choose a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 0
max_guesses = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

while incorrect_guesses < max_guesses:

    # Display the word
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if word is completely guessed
    if "_" not in display:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    # Take user's guess
    guess = input("Enter a letter: ").lower()

    # Check the guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct guess!")
    else:
        guessed_letters.append(guess)
        incorrect_guesses += 1
        print("Wrong guess!")
        print("Incorrect guesses left:", max_guesses - incorrect_guesses)

# If player loses
if incorrect_guesses == max_guesses:
    print("\n😢 Game Over!")
    print("The word was:", word)
