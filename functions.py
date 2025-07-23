import streamlit as st

# Function to translate roles between Gemini and Streamlit terminology
def map_role(role):
    if role == "model":
        return "assistant"
    else:
        return role

def fetch_gemini_response(user_query):
    # Use the session's model to generate a response
    response = st.session_state.chat_session.model.generate_content(user_query,
    timeout=300 # Increase timeout to 5 minutes (300 seconds))
    print(f"Aura's Response: {response}")
    return response.parts[0].text