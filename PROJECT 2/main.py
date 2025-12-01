# Project 2 MINI AI CHATBOT 

import datetime
import time

name = input("Welcome, Enter your name :")
currentTime = datetime.datetime.now().hour

if 5 <= currentTime <= 11:
    print("Good morning,", name)
elif 11<= currentTime <= 17:
    print("Good Afternoon,",name)
elif 17 <= currentTime <= 20:
    print("Good Evening,", name)
else:
    print("Good Night,",name)

print("Namaste ! Your asistant here to help you ")
print("You can ask me basic questions, type'bye' to exit from the chat. ")

# Chatbot  memory creation 
responses ={
    "hello": "Hi, welcome . How can I help you?",
    "how are you": " I am very fine. Thank you",
    "who are you": " I am smart AI chatbot",
    "motivate me": " 🌟Every step forward, no matter how small, is proof that you’re stronger than yesterday.",
    "happy": "✨Great to heae that",
    "what are the functions in python":"In Python,👉 functions are reusable blocks of code defined with def that perform a specific task when called",
    "Explain loops":"➰Loops in Python are used to repeatedly execute a block of code over sequences or conditions until they’re exhausted.",
    "who made python": "Python was created by Guido van Rossum in 1989 at Centrum Wiskunde",
    "packages in python": "In Python, a package is simply a collection of modules grouped together in a directory that contains an __init__.py file",
    "bye":"Byee byee, Take care"
}

# function to get response
def getResponse(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
        
    return "Now I am not able to tell that yet. I am in learning mode:"

# user input
while True:
    userInput = input("Please ask your querry:")
    reply = getResponse(userInput)
    time.sleep(1)
    print("Bot Response:",reply)
    time.sleep(1)
    if "bye" in userInput.lower():
        break