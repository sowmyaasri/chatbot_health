import streamlit as st
from src.backend import AI


if 'messages' not in st.session_state:
    
    st.session_state.messages = []


if 'llm' not in st.session_state:
    st.session_state.llm = AI()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your prompt here..."):
    
    st.chat_message("user").markdown(prompt)
    
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    
    assistant_response = st.session_state.llm.chat(message=prompt)
    
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
    
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

import streamlit as st

sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")
