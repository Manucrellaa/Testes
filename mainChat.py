#-------ChatBot-------#
import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer 
import random

#--------First interection with the user-------#
st.title("Bolha - Your Friendly ChatBot")
st.write("Welcome to the Bolha! Please enter your name to start chatting.")
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! How can I assist you today?")
    
    #--------ChatBot Creation-------#
    chatbot = ChatBot('Bolha')
    trainer = ListTrainer(chatbot)
    #--------Training the ChatBot-------#
    trainer.train([
        "Hi",
        "Hello!",
        "How are you?",
        "I'm good, thank you! How can I help you?",
        "What is your name?",
        "My name is Bolha. Nice to meet you!",
        "What can you do?",
        "I can chat with you and answer your questions. Feel free to ask me anything!"
    ])
    #--------Chatting with the ChatBot-------#
    user_input = st.text_input("You:")
    if user_input:
        response = chatbot.get_response(user_input)
        st.write(f"Bolha: {response}")

#-------Exit message-------#
st.write("Thank you for chatting with Bolha! Have a great day!")
