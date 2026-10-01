CodeAlpha Basic Chatbot

1. Project Overview

This project is a simple rule-based chatbot created using Python as part of the CodeAlpha Python Programming Internship.

The chatbot interacts with the user through the terminal and gives predefined responses based on the message entered by the user.

This is not an AI chatbot. It works using basic Python `if-elif-else` conditions and predefined replies.

2. Key Features

- Accepts messages from the user
- Responds to common greetings
- Answers a few basic questions
- Handles thank-you messages
- Continues the conversation until the user types `bye`
- Gives a default response for unknown messages
- Simple text-based interface

3. Python Concepts Used

- `input()` for taking user messages
- `print()` for displaying responses
- `while` loop for continuous conversation
- `if-elif-else` for checking messages
- String methods such as `lower()`
- Variables and basic conditions

4. Project Structure

CodeAlpha_Chatbot
├── chatbot.py
└── README.md


5. How to Run

1. Open the project folder in VS Code.
2. Open `chatbot.py`.
3. Run the Python file.
4. Type a message in the terminal.
5. Type `bye` to end the conversation.

6. How the Chatbot Works

The chatbot checks the message entered by the user.

For example:

- `hello` or `hi` → Gives a greeting
- `how are you` → Gives a simple reply
- `what is python` → Explains Python
- `what can you do` → Explains what the chatbot can answer
- `thank you` or `thanks` → Gives a polite reply
- `bye` → Ends the conversation
- Any other message → Gives an unknown-message response

7. Example Conversation


Basic Chatbot
Type bye to stop.

You: hello
Bot: Hello! Nice to talk to you.

You: what is python
Bot: Python is a programming language.

You: how are you
Bot: I am doing well. Thank you!

You: thanks
Bot: You are welcome!

You: bye
Bot: Goodbye! Have a nice day.


8. Design Approach

The chatbot was intentionally created using simple Python logic so that the working of every part of the program is easy to understand.

Instead of using external AI libraries or APIs, the program uses predefined conditions and responses.

9. What I Learned

Through this project, I practiced:

- Taking user input
- Working with strings
- Using conditional statements
- Using loops
- Building a simple interactive Python program
- Handling unknown user input

 10. Future Improvements

Some possible improvements are:

- Add more questions and responses
- Add more conversation options
- Store responses in a separate file
- Add a graphical user interface
- Connect the chatbot to an AI API in a future version

11. Internship Context

This project was completed as part of the CodeAlpha Python Programming Internship.

The task requires creating a basic rule-based chatbot using predefined responses and Python fundamentals.

12. Author

Chaitanya Deshaboina

