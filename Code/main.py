#by Coding with Jan
#subscribe to my channel

import random
import re
import difflib

patterns = {
    r'hi|hello|hey': ['Hello!', 'Hi there!', 'Hey!'],
    r'what is your name': ['My name is Chatbot. What is your name?'],
    r'my name is (.*)': ['Nice to meet you, %1!', 'Hi %1, how are you doing today?'],
    r'how are you': ['I am doing well, thank you!', 'I am fine, thanks for asking.', "I'm feeling great today! How about you?"],
    r'what do you do': ['I am a chatbot designed to chat with people!', 'I chat with people like you!'],
    r'what is your purpose': ['My purpose is to chat with people and provide them with helpful responses.'],
    r'what can you do': ['I can chat with you and answer your questions!'],
    r'how old are you': ['I am a chatbot, I do not age.'],
    r'where are you from': ['I was created by a programmer in the United States.'],
    r'what do you like': ['I like chatting with people like you!', 'I enjoy helping people and answering their questions.'],
    r'what is your favorite color': ['I am a chatbot, I do not have a favorite color.'],
    r'what is your favorite food': ['I am a chatbot, I do not eat food.'],
    r'what is the weather like': ['I am sorry, but I am not able to answer that question.'],
    r'tell me a joke': ['Why did the tomato turn red? Because it saw the salad dressing!'],
    r'what is python': ['Python is a popular programming language that is used for a wide range of applications, including web development, data analysis, and artificial intelligence.'],
    r'how do I install python': ['To install Python, go to the official Python website and download the latest version for your operating system. Follow the installation instructions to complete the process.'],
    r'what is a variable': ['A variable is a named location in memory that can hold a value. Variables are used to store data in a program.'],
    r'what is a function': ['A function is a block of code that performs a specific task. Functions can be called multiple times from different parts of a program, making them a useful tool for organizing and reusing code.'],
    r'what is an if statement': ['An if statement is a conditional statement that allows a program to perform different actions based on whether a condition is true or false.'],
    r'what is a for loop': ['A for loop is a control flow statement that allows a program to repeat a block of code a fixed number of times.'],
    r'what is a while loop': ['A while loop is a control flow statement that allows a program to repeat a block of code while a specified condition is true.'],
    r'what is a module': ['A module is a file containing Python definitions and statements. Modules can be imported into other programs to provide additional functionality.'],
    r'what is object-oriented programming': ['Object-oriented programming is a programming paradigm that emphasizes the use of objects and classes. It allows for the creation of complex programs by breaking them down into smaller, more manageable pieces.'],
    r'what is a class': ['A class is a blueprint for creating objects in an object-oriented program. It defines the attributes and methods that the objects will have.'],
    r'what is inheritance': ['Inheritance is a mechanism in object-oriented programming that allows a class to inherit properties and methods from another class.'],
    r'what is polymorphism': ['Polymorphism is a concept in object-oriented programming that allows objects of different types to be treated as if they were the same type.'],
    r'what is pip': ['Pip is the package installer for Python. It is used to install, upgrade, and remove packages and their dependencies.'],
    r'what is a virtual environment': ['A virtual environment is an isolated Python environment that allows you to install packages and dependencies without affecting the system Python installation. It is a best practice for managing dependencies in a project.'],
    r'bye|goodbye': ['Goodbye!', 'See you later.']
}




def generate_response(user_input):
    max_similarity = 0
    best_response = "I'm sorry, I didn't understand what you're asking."
    for pattern, responses in patterns.items():
        similarity = difflib.SequenceMatcher(None, user_input, pattern).ratio()
        if similarity > max_similarity:
            max_similarity = similarity
            best_response = random.choice(responses)
            if '%1' in best_response:
                match = re.match(pattern, user_input)
                if match:
                    best_response = best_response.replace('%1', match.group(1))
    if max_similarity >= 0.8:
        return best_response
    else:
        return "I'm sorry, I didn't understand what you're asking."


print("Hi! I'm a chatbot. You can start chatting with me by typing a message.")
while True:
    user_input = input("You: ")
    bot_response = generate_response(user_input)
    print("Chatbot:", bot_response)
