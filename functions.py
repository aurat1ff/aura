import streamlit as st

# Function to translate roles between Gemini and Streamlit terminology
def map_role(role):
    if role == "model":
        return "assistant"
    else:
        return role

fetch_gemini_response(user_query):
    # Use the session's model to generate a response
    # Access the model instance from session_state
    model_instance = st.session_state.chat_session

    # Pass timeout directly to generate_content method
    response = model_instance.generate_content(
        user_query,
        timeout=600  # Set your desired timeout in seconds (e.g., 600 for 10 minutes)
    )
    print(f"Aura's Response: {response}")
    return response.parts[0].text