import streamlit as st
from src.backend import AI
import random

# ✅ Apply Custom CSS for Background and Chat Styling
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

# ✅ Function to play background music
def play_music():
    audio_file = open("C:\\Users\\coral\\Downloads\\calm-background-music-ambient-guitar-298550.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3", autoplay=True)

# ✅ Display chatbot title with emoji
st.markdown('<h1 style="text-align:center; color:white;">🧠 MENTAL HEALTH Chatbot - Your Friendly Mental Health Companion 🤗</h1>', unsafe_allow_html=True)

# ✅ Play background music
play_music()

# ✅ Display fun animated GIF
st.markdown(
    '<div style="text-align: center;">'
    '<img src="https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif" width="200">'
    '</div>',
    unsafe_allow_html=True
)

# ✅ Daily Motivational Quote
motivational_quotes = [
    "🌟 Believe in yourself! You are stronger than you think.",
    "💪 Every day is a fresh start. Keep pushing forward!",
    "😇 You are loved, you are enough, and you matter!",
    "🚀 The best time to start was yesterday. The next best time is now!"
]
st.info(random.choice(motivational_quotes))

# ✅ Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []  # Stores chat history

if "llm" not in st.session_state:
    st.session_state.llm = AI()  # Initializes chatbot AI

if "last_reaction" not in st.session_state:
    st.session_state.last_reaction = None  # Tracks last reaction for confetti fix

# ✅ Display Previous Chat Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ✅ Handle User Input
if prompt := st.chat_input("Enter your message here..."):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get Assistant Response
    assistant_response = st.session_state.llm.chat(message=prompt)
    
    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)

    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

# ✅ Emoji Reactions for Responses
st.markdown("### React to the chatbot's response:")
reaction = st.radio("", ["😀 Happy", "🤔 Thoughtful", "😢 Sad", "😡 Angry"], horizontal=True)

# ✅ Confetti Effect ONLY for Happy Reaction
if reaction == "😀 Happy" and st.session_state.last_reaction != "😀 Happy":
    st.balloons()  # 🎉 Show confetti only ONCE when Happy is selected
    st.success("Glad to hear that!")

# ✅ Update the last reaction in session state
st.session_state.last_reaction = reaction

# ✅ GIF Responses
gif_dict = {
    "😀 Happy": "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif",
    "🤔 Thoughtful": "C:\\Users\\coral\\OneDrive\\Desktop\\thoughtful.gif",
    "😢 Sad": "C:\\Users\\coral\\OneDrive\\Desktop\\sad picka.gif",
    "😡 Angry": "C:\\Users\\coral\\OneDrive\\Desktop\\angry.jpg"
}

if reaction in gif_dict:
    st.image(gif_dict[reaction], width=200)
