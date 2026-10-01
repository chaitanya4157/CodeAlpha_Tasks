CodeAlpha Hangman

A console-based Hangman game developed in Python as part of my CodeAlpha Python Programming Internship.

The project was developed in two stages: a basic implementation to establish the core game logic, followed by an improved version focused on better interaction, validation, and replayability.

---

1. Project Overview

Hangman is a word-guessing game in which the player discovers a hidden word by entering one letter at a time.

The program selects a word from a predefined collection, provides a relevant hint, and allows a maximum of six incorrect guesses.

The project contains two implementations:

- Basic Version — focuses on the fundamental Hangman logic.
- Improved Version — extends the basic implementation with additional user-focused features.

---

2. Key Features

-> Basic Version

1. Random word selection
2. Word-specific hint
3. Letter-by-letter guessing
4. Maximum of six incorrect guesses
5. Input validation
6. Repeated-guess protection
7. Win and loss detection

-> Improved Version

1. Word categories
2. Contextual hints
3. Lives counter
4. Wrong-letter tracking
5. Repeated-guess protection
6. Win and loss score
7. Play-again option
8. New word and hint for every round

---

3. Python Concepts

The project applies fundamental Python concepts in a practical application.

| Concept       | Application                                  |
| ------------- | -------------------------------------------- |
| Random module | Selects a word for each round                |
| Lists         | Stores guessed and incorrect letters         |
| Dictionaries  | Stores words with their hints and categories |
| Strings       | Handles words, letters, and user input       |
| for loops     | Processes individual letters                 |
| while loops   | Controls the game flow                       |
| if-else       | Handles decisions and game conditions        |
| input()       | Receives player guesses                      |

---

4. Project Structure

->
CodeAlpha_Hangman/
│
├── hangman.py
│
├── basic_version/
│   └── hangman_basic.py
│
└── README.md


- hangman.py
The main improved version of the game.

- basic_version/hangman_basic.py
The initial implementation used to establish the core game logic.

- README.md
Project documentation, usage instructions, and development overview.

---

5. How to Run

-> Requirements

- Python 3.x
- Visual Studio Code or any Python-compatible editor
- No external Python packages are required

#Run the improved version


python hangman.py


- Run the basic version


python basic_version/hangman_basic.py


---

6. How the Game Works

1. The program selects a word from the predefined collection.
2. A corresponding hint and, in the improved version, a category are displayed.
3. The player enters one letter at a time.
4. Correct letters are revealed in their respective positions.
5. Incorrect guesses reduce the remaining attempts.
6. The player wins by discovering the complete word before reaching six incorrect guesses.
7. The improved version allows the player to start another round with a new word.

---

7. Design Approach

The project was intentionally developed in two stages.

-> Stage 1 — Build the Core

The basic version focuses on understanding the essential mechanics of Hangman:

- selecting a word
- displaying hidden letters
- accepting guesses
- tracking incorrect attempts
- determining the result

-> Stage 2 — Improve the Interaction

The improved version builds on that foundation by considering how a player actually uses the program.

Hints and categories provide context before guessing. Input validation prevents invalid entries from affecting the game. Repeated-guess protection avoids unnecessary attempts, while scoring and replay make multiple rounds more useful and engaging.

The objective was to improve the experience without introducing unnecessary complexity.

---

8. What I Learned

Through this project, I practiced turning basic Python concepts into a complete interactive program.

The main areas of learning were:

1. Working with collections of data
2. Controlling program flow with loops and conditions
3. Validating user input
4. Managing game state
5. Breaking a problem into smaller logical steps
6. Improving an initial implementation through iteration

---

9. Future Improvements

Possible extensions for a future version include:

1. Multiple difficulty levels
2. Larger word collections
3. Additional word categories
4. Persistent high scores
5. A graphical user interface
6. A larger external word database

These features are intentionally outside the current scope so that the project remains focused on Python fundamentals.

---

10. Internship Context

This project was developed as part of the CodeAlpha Python Programming Internship.

The implementation follows the assigned Hangman requirements while extending the basic task with additional features designed to improve interaction and usability.

---

11. Author

Chaitanya Deshaboina


