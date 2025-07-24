import google.generativeai as genai
import streamlit as st
import os



# Configure Streamlit page settings
st.set_page_config(
    page_title="Aura Unchained!",
    page_icon=":robot_face:",  # Favicon emoji
    layout="wide",  # Page layout option
)


import google.generativeai as genai


# --- Model Initialization with Timeout ---
if "chat_session" not in st.session_state:
    # Initialize the model with a longer timeout
    st.session_state.chat_session = genai.GenerativeModel(
        "gemini-1.5-flash",
        generation_config={"temperature": 0.7},
        request_options={"timeout": 600} 
    )
    # Start a chat session with the model
    st.session_state.chat_session = st.session_state.chat_session.start_chat(history=[])

# Display the chatbot's title on the page
st.title("🤖 Set your inner Aura free!")

# Display the chat history
for msg in st.session_state.chat_session.history:
    with st.chat_message(map_role(msg["role"])):
        st.markdown(msg["content"])

# Input field for user's message
user_input = st.chat_input("Ask Aura...")
if user_input:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_input)

    # Send user's message to Gemini and get the response
    gemini_response = fetch_gemini_response(user_input)

    # Display Gemini's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response)

    # Add user and assistant messages to the chat history
    st.session_state.chat_session.history.append({"role": "user", "content": user_input})
    st.session_state.chat_session.history.append({"role": "model", "content": gemini_response})