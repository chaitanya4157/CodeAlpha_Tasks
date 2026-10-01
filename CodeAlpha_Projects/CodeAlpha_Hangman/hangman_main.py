import random

word_data = {
    "python": {
        "hint": "A popular programming language",
        "category": "Programming"
    },
    "github": {
        "hint": "A platform for sharing code",
        "category": "Technology"
    },
    "coding": {
        "hint": "Writing instructions for a computer",
        "category": "Programming"
    },
    "program": {
        "hint": "A set of instructions for a computer",
        "category": "Programming"
    },
    "debug": {
        "hint": "Finding and fixing errors in code",
        "category": "Programming"
    }
}

wins = 0
losses = 0

print("\nWelcome to Hangman!")

while True:

    word = random.choice(list(word_data))
    hint = word_data[word]["hint"]
    category = word_data[word]["category"]

    guessed_letters = []
    wrong_letters = []
    wrong_guesses = 0

    print("\nNew Game")
    print("Category:", category)
    print("Hint:", hint)

    while wrong_guesses < 6:

        display = ""

        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display)
        print("Lives left:", 6 - wrong_guesses)

        if wrong_letters:
            print("Wrong letters:", ", ".join(wrong_letters))

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue

        if guess in guessed_letters or guess in wrong_letters:
            print("You already tried that letter.")
            continue

        if guess in word:
            guessed_letters.append(guess)
            print("Correct!")
        else:
            wrong_letters.append(guess)
            wrong_guesses += 1
            print("Wrong guess.")

        if all(letter in guessed_letters for letter in word):
            wins += 1
            print("\nYou won!")
            print("The word was:", word)
            break

    else:
        losses += 1
        print("\nGame over.")
        print("The word was:", word)

    print("\nScore:", wins, "win(s)", "-", losses, "loss(es)")

    again = input("Play again? (yes/no): ").lower().strip()

    if again != "yes":
        print("\nThanks for playing!")
        break