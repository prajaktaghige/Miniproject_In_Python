def respond_to_message(message):
    responses = {
        "hi": "Hello!",
        "how are you": "I'm good, thank you!",
        "bye": "Goodbye!",
    }
    return responses.get(message.lower(), "I don't understand that.")

def main():
    print("Simple Chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        print(f"Chatbot: {respond_to_message(user_input)}")

if __name__ == "__main__":
    main()
