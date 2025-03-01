



rules = {
    "hello": "Hi! How are you?",
    "how are you": "I'm good, thanks! How can I help you?",
    "what is your name": "My name is ChatBot",
    "exit": "Goodbye! See you later.",
    "default": "I didn't understand that. Can you please rephrase?"
}

def chatbot(message):
    # Convert the message to lowercase
    message = message.lower()
    
    # Check if the message matches any of the rules
    for keyword, response in rules.items():
        if keyword in message:
            return response
    
    # If no rule matches, return the default response
    return rules["default"]

def main():
    print("Welcome to the chatbot!")
    
    while True:
        # Get the user's message
        message = input("You: ")
        
        # Check if the user wants to exit
        if message.lower() == "exit":
            print("ChatBot:", chatbot(message))
            break
        
        # Print the chatbot's response
        print("ChatBot:", chatbot(message))

if __name__ == "__main__":
    main()


