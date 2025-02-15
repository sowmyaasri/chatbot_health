import streamlit as st
from src.backend import AI  # Ensure this is correctly defined in backend.py
import os
import random

# Apply Custom CSS for Background and Chat Styling
st.markdown(
    """
    <style>
    /* Background color for the whole page */
    [data-testid="stAppViewContainer"] {
        background-color: #ADD8E6; /* Light Blue */
    }

    /* Style the chatbot message bubbles */
    [data-testid="stChatMessage"] {
        background-color: #f0f0f0; /* Light Gray */
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to play background music
def play_music():
    music_path = os.path.join("downloads", "C:\Users\coral\Downloads\calm-background-music-ambient-guitar-298550.mp3")  # Use relative path
    if os.path.exists(music_path):
        with open(music_path, "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3", autoplay=True)

# Display chatbot title with emoji
st.markdown('<h1 style="text-align:center; color:white;">🤖 MENTAL HEALTH Chatbot - Your Friendly Mental Health Companion</h1>', unsafe_allow_html=True)

# Play background music
play_music()

# Display fun animated GIF
st.markdown(
    '<div style="text-align: center;">'
    '<img src="https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif" width="200">'
    '</div>',
    unsafe_allow_html=True
)

# Daily Motivational Quote
motivational_quotes = [
    "🌟 Believe in yourself! You are stronger than you think.",
    "💪 Every day is a fresh start. Keep pushing forward!",
    "😇 You are loved, you are enough, and you matter!",
    "🚀 The best time to start was yesterday. The next best time is now!"
]
st.info(random.choice(motivational_quotes))

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

if "llm" not in st.session_state:
    st.session_state.llm = AI()  # Ensure backend.py contains AI class

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle User Input
prompt = st.chat_input("Enter your message here...")  # Ensure Streamlit version >= 1.25
if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get Assistant Response
    assistant_response = st.session_state.llm.chat(message=prompt)

    with st.chat_message("assistant"):
        st.markdown(assistant_response)

    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

# Emoji Reactions for Responses
st.markdown("### React to the chatbot's response:")
reaction = st.radio("", ["😀 Happy", "🤔 Thoughtful", "😢 Sad", "😡 Angry"], horizontal=True)


# GIF Responses
gif_dict = {
    "😀 Happy": "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif",
    "🤔 Thoughtful": "C:\\Users\\coral\\OneDrive\\Desktop\\thoughtful.gif",
    "😢 Sad": "C:\\Users\\coral\\OneDrive\\Desktop\\sad picka.gif",
    "😡 Angry": "C:\\Users\\coral\\OneDrive\\Desktop\\angry.jpg"
}
if reaction in gif_dict:
    st.image(gif_dict[reaction], width=200)
