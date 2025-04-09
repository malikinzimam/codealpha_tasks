import nltk
import random
import string  # To process standard python strings
from nltk.chat.util import Chat, reflections

# Sample conversation pairs
pairs = [
    [
        r"hi|hello|hey", 
        ["Hello!", "Hey there!", "Hi, how can I help you?"]
    ],
    [
        r"how are you ?", 
        ["I'm doing well, how about you?", "I'm great! What about you?"]
    ],
    [
        r"(.*) your name ?", 
        ["I'm a chatbot created to assist you!", "You can call me ChatBot."]
    ],
    [
        r"quit", 
        ["Goodbye! Have a great day!", "Bye! It was nice talking to you."]
    ]
]

# Creating the chatbot
chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chat()
