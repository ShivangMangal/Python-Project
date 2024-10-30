import random
from nltk.chat.util import Chat, reflections

# Define some patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ['I am doing well, thank you!', 'I\'m good, thanks for asking.', 'I\'m fine, how about you?']),
    (r'(.*) your name?', ['I am a chatbot.', 'My name is Chatbot.']),
    (r'(.*) (weather|temperature) (?:today|tomorrow)', ['Sorry, I cannot provide weather information.']),
    (r'(.*) (do you like|think about) (.*)', ['I don\'t have personal opinions.', 'I\'m not capable of liking or thinking.']),
    (r'(.*) (good|bad)', ['That\'s good to hear!', 'I\'m sorry to hear that.']),
    (r'quit', ['Goodbye!', 'Bye!', 'Take care!']),
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

def main():
    print("Hello! I am a chatbot. How can I assist you today?")
    print("Type 'quit' to exit.")

    # Start chatting
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    main()
