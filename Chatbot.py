def simple_chatbot(user_input):
    if "hello" in user_input:
        return "Hello! How can I help you?"
    elif "how are you" in user_input:
        return "Yeah..I'm feeling Great!"
    elif "motivation" in user_input:
        return "“Turn your wounds into wisdom.” ―Oprah Winfrey.hello"
    elif "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that."

# Example usage:
while True:
    user_input = input("You: ")
    response = simple_chatbot(user_input)
    print("Bot:", response)
