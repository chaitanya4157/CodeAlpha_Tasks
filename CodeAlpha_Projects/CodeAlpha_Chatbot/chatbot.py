def chatbot(message):
    message = message.lower().strip()

    if message == "hello" or message == "hi":
        return "Hello! Nice to talk to you."

    elif message == "how are you":
        return "I'm doing well. Thanks for asking!"

    elif message == "what is python":
        return "Python is a popular programming language."

    elif message == "what can you do":
        return "I can answer some basic questions and have a simple conversation."

    elif message == "thank you" or message == "thanks":
        return "You're welcome!"

    elif message == "bye":
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that."

print("Basic Chatbot")
print("Type 'bye' to end the conversation.")

while True:
    message = input("\nYou: ")

    reply = chatbot(message)

    print("Bot:", reply)

    if message.lower().strip() == "bye":
        break