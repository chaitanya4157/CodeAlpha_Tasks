import random

words = {
    "python": "A popular programming language",
    "github": "A platform for sharing code",
    "coding": "Writing instructions for a computer",
    "program": "Instructions given to a computer",
    "debug": "Finding and fixing errors in code"
}

word = random.choice(list(words))
hint = words[word]

guessed_letters = []
wrong_guesses = 0

print("\nWelcome to Hangman!")
print("Hint:", hint)

while wrong_guesses < 6:

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong guesses:", wrong_guesses, "/ 6")

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed_letters:
        print("You already tried that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong guess.")

    if all(letter in guessed_letters for letter in word):
        print("\nYou won!")
        print("The word was:", word)
        break

else:
    print("\nGame over.")
    print("The word was:", word)