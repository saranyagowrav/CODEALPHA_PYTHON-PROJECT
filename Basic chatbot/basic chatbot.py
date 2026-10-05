# Basic Chatbot

def chatbot(user_input):
    user_input = user_input.lower()

    if user_input == "hello" or user_input == "hi":
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "what is your name":
        return "I am a simple Python chatbot."

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand that."


print("🤖 Chatbot started!")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    reply = chatbot(user_input)
    print("Bot:", reply)

    if user_input.lower() == "bye":
        break
