import streamlit as st
import speech_recognition as sr
import pyttsx3
import boto3
import requests

# Amazon Product Advertising API details
ACCESS_KEY = 'YOUR_ACCESS_KEY'
SECRET_KEY = 'YOUR_SECRET_KEY'
ASSOCIATE_TAG = 'YOUR_ASSOCIATE_TAG'

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech from audio
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        st.write(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        st.write("Sorry, I could not understand the audio.")
        return ""
    except sr.RequestError:
        st.write("Sorry, there was a request error.")
        return ""

# Function to search for products
def search_products(product_name):
    # Dummy data for demonstration
    return ["Product 1", "Product 2", "Product 3"]

# Function to get recommendations
def get_recommendations(user_preferences):
    # Dummy data for demonstration
    return ["Recommended Product 1", "Recommended Product 2"]

# Function to handle voice commands
def handle_command(command):
    if "search for" in command:
        product_name = command.split("search for")[-1].strip()
        st.write(f"Searching for products: {product_name}")
        search_results = search_products(product_name)
        speak(f"Here are the results for {product_name}.")
        st.write(f"Search results for '{product_name}':")
        for result in search_results:
            st.write(result)
    elif "recommend" in command:
        preferences = command.split("recommend")[-1].strip()
        st.write(f"Getting recommendations based on: {preferences}")
        recommendations = get_recommendations(preferences)
        speak(f"Here are some recommendations based on your preferences.")
        st.write("Personalized recommendations:")
        for recommendation in recommendations:
            st.write(recommendation)
    else:
        st.write("Sorry, I didn't understand that command.")
        speak("Sorry, I didn't understand that command.")

# Streamlit interface
st.title("Alexa Skill Simulator: Product Search and Recommendations")

# Product Search
st.header("Search for Products")
product_name = st.text_input("Enter the product name:")
if st.button("Search"):
    search_results = search_products(product_name)
    st.write(f"Search results for '{product_name}':")
    for result in search_results:
        st.write(result)

# Personalized Recommendations
st.header("Get Personalized Recommendations")
user_preferences = st.text_input("Enter your preferences:")
if st.button("Get Recommendations"):
    recommendations = get_recommendations(user_preferences)
    st.write("Personalized recommendations:")
    for recommendation in recommendations:
        st.write(recommendation)

# Voice Assistant
st.header("Voice Assistant")
st.write("Click the button below and speak your command:")

if st.button("Speak"):
    command = recognize_speech()
    if command:
        handle_command(command)
