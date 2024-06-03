import os
import time
import requests
import tempfile
import streamlit as st


BASE_URL = "http://0.0.0.0:8001"


def shorten_text(text):
    api_url = f"{BASE_URL}/shorten-text"
    params = {"text": text}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        llm_response = response.json().get("response")
        return llm_response
    except requests.RequestException as e:
        st.error(f"Error: {e}")
        return None


def correct_grammar(text):
    api_url = f"{BASE_URL}/check-grammar"
    params = {"text": text}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        llm_response = response.json().get("response")
        return llm_response
    except requests.RequestException as e:
        st.error(f"Error: {e}")
        return None


def make_professional(text):
    api_url = f"{BASE_URL}/convert-to-professional"
    params = {"text": text}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        llm_response = response.json().get("response")
        return llm_response
    except requests.RequestException as e:
        st.error(f"Error: {e}")
        return None


def make_casual(text):
    api_url = f"{BASE_URL}/convert-to-casual"
    params = {"text": text}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        llm_response = response.json().get("response")
        return llm_response
    except requests.RequestException as e:
        st.error(f"Error: {e}")
        return None

def elaborate_text(text):
    api_url = f"{BASE_URL}/elaborate-text"
    params = {"text": text}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        llm_response = response.json().get("response")
        return llm_response
    except requests.RequestException as e:
        st.error(f"Error: {e}")
        return None

def ask_llm(text):
    api_url = f"{BASE_URL}/response-from-llm"
    params = {"text": text}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        llm_response = response.json().get("response")
        return llm_response
    except requests.RequestException as e:
        st.error(f"Error: {e}")
        return None

def enter_prompt_and_get_response(prompt):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.spinner("Thinking..."):
            user_input = st.session_state.messages[-1]["content"]
            response = ask_llm(text=user_input)

            st.session_state.messages.append({"role": "assistant", "content": response})

        with st.chat_message("assistant"):
            st.markdown(response)
    except Exception as e:
        print(f"LLM response generation error: {e}")
        st.error("Assistant currently not available")


def keyword_extraction(text):
    api_url = f"{BASE_URL}/keyword-extraction"
    params = {"text": text}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        llm_response = response.json().get("response")
        return llm_response
    except requests.RequestException as e:
        st.error(f"Error: {e}")
        return None

def sentiment_analysis(text):
    api_url = f"{BASE_URL}/sentiment-analysis"
    params = {"text": text}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        llm_response = response.json().get("response")
        return llm_response
    except requests.RequestException as e:
        st.error(f"Error: {e}")
        return None

# Main app layout
st.markdown(
    """
    <style>
    .centered-content {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        flex-direction: column;
        padding-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Centered Title and Subtitle
st.markdown("""
    <div class="centered-content">
        <h1>Welcome to AI Service</h1>
        <p>Perform various text processing tasks with our AI services.</p>
    </div>
""", unsafe_allow_html=True)

# User input
# user_input = st.text_area("Enter your text here:")
#
# if st.button("Shorten Text"):
#     try:
#         with st.spinner("Loading..."):
#             result = shorten_text(user_input)
#             if result:
#                 st.write("Shortened Text:", result)
#             else:
#                 st.write("Shortened Text Failed")
#     except Exception as e:
#         print(f"Error : {e}")
#         st.error("Shortened failed")
#
# if st.button("Correct Grammar"):
#     result = correct_grammar(user_input)
#     if result:
#         st.write("Corrected Text:", result)
#
# if st.button("Make Professional"):
#     result = make_professional(user_input)
#     if result:
#         st.write("Professional Text:", result)
#
# if st.button("Make Casual"):
#     result = make_casual(user_input)
#     if result:
#         st.write("Casual Text:", result)
#
# if st.button("Elaborate Text"):
#     result = elaborate_text(user_input)
#     if result:
#         st.write("Elaborated Text:", result)
#
# if st.button("Extract Keywords"):
#     result = keyword_extraction(user_input)
#     if result:
#         st.write("Extracted Keywords:", result)
#
# if st.button("Sentiment Analysis"):
#     result = sentiment_analysis(user_input)
#     if result:
#         st.write("Sentiment:", result)
#
# # Chat with AI
# st.subheader("Chat with AI")
# prompt = st.text_input("Enter your prompt:")
# if st.button("Ask AI"):
#     enter_prompt_and_get_response(prompt)