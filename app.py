import streamlit as st
from src.backend import AI
import time

# Apply Custom CSS for Background and Chat Styling
st.markdown(
    """
    <style>
    /* Gradient background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to right, #ff9a9e, #fad0c4);
        color: #ffffff;
    }

    /* Chat message bubbles */
    [data-testid="stChatMessage"] {
        border-radius: 15px;
        padding: 12px;
        margin: 5px 0;
    }

    /* User message */
    [data-testid="stChatMessage"][data-role="user"] {
        background-color: #a29bfe;
        color: white;
    }

    /* Assistant message */
    [data-testid="stChatMessage"][data-role="assistant"] {
        background-color: #ffeaa7;
        color: black;
    }

    /* Title styling */
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }

    /* Centered GIF */
    .gif-container {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display chatbot title with emoji
st.markdown('<p class="title">🤖 Mental health support Chatbot</p>', unsafe_allow_html=True)

# Display a fun animated GIF (cartoon robot)
st.markdown(
    '<div class="gif-container">'
    '<img src="https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif" width="200">'
    '</div>',
    unsafe_allow_html=True
)

# Initialize Session State for Messages and AI Model
if "messages" not in st.session_state:
    st.session_state.messages = []

if "llm" not in st.session_state:
    st.session_state.llm = AI()

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle User Input
if prompt := st.chat_input("Enter your message here..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Simulate typing animation before AI responds
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        typing_response = "Thinking..."
        for i in range(len(typing_response)):
            message_placeholder.markdown(typing_response[:i+1])
            time.sleep(0.1)  # Typing delay effect

        # Get Assistant Response
        assistant_response = st.session_state.llm.chat(message=prompt)
        message_placeholder.markdown(assistant_response)

    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

# Feedback Section
st.markdown("### Did you find this response helpful?")
sentiment_mapping = ["👎 No", "👍 Yes"]
selected = st.radio("Your feedback:", options=[0, 1], format_func=lambda x: sentiment_mapping[x])

if selected is not None:
    st.markdown(f"✅ You selected: {sentiment_mapping[selected]}")
