import streamlit as st
import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import re
from collections import deque  # Optimized chat history handling

# Load API Key
load_dotenv()
groq_api = os.getenv("GROQ_API_KEY")

# Streamlit App Header
st.header("Gen AI Application with Groq")

# Initialize Chat Model
model = ChatGroq(model="deepseek-r1-distill-llama-70b", api_key=groq_api)

# Define Chat Prompt Template
prompt = ChatPromptTemplate(
    [
        ("system", "Answer the questions asked by the user in natural human typed like content."),
        ("user", "{question}")
    ]
)

# Output Parser
parser = StrOutputParser()

# Combine prompt, model, and parser into a chain
chain = prompt | model | parser

# Function to clean response (removes <think>...</think>)
def clean_response(response):
    return re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()

# Function to truncate long chat titles dynamically based on UI width
def truncate_title(title, max_chars=25):
    """Truncate chat title if it exceeds max_chars, keeping first part and adding '...'."""
    return title+' '*(len(title)-25) if len(title) < max_chars else title[:max_chars]


# Initialize session state for storing chats
if "chats" not in st.session_state:
    st.session_state.chats = {}  # Dictionary to store multiple chat histories
if "current_chat" not in st.session_state:
    st.session_state.current_chat = None  # Tracks the selected chat title
if "new_chat_started" not in st.session_state:
    st.session_state.new_chat_started = False  # Tracks if a fresh chat was started

# Sidebar: "Start Fresh Chat" Button
if st.sidebar.button("🆕 Start Fresh Chat"):
    st.session_state.new_chat_started = True  # Indicate a fresh chat has started
    st.session_state.current_chat = None  # Reset current chat selection
    st.rerun()  # Force UI refresh to prompt for title

# If a fresh chat was started, ask for a title
if st.session_state.new_chat_started:
    chat_title = st.sidebar.text_input("Enter chat title:", key="new_chat_title")

    if chat_title and chat_title not in st.session_state.chats:
        st.session_state.chats[chat_title] = deque()  # Initialize deque for new chat
        st.session_state.current_chat = chat_title  # Set as active chat
        st.session_state.new_chat_started = False  # Reset flag
        st.rerun()  # Refresh UI to display the chat interface

# Apply Custom CSS for Sidebar Buttons & Title Bar Alignment
sidebar_css = """
    <style>
        .sidebar-button {
            display: block;
            width: 100%;
            padding: 20px;
            margin: 5px 0;
            border-radius: 8px;
            border: 1px solid #ddd;
            text-align: center;
            font-weight: normal;
            background-color: white;
            cursor: pointer;
            transition: 0.2s ease-in-out;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 200px;  /* Static title bar width */
        }
        
        .sidebar-button:hover {
            background-color: #f0f2f6;
        }
    </style>
"""
st.sidebar.markdown(sidebar_css, unsafe_allow_html=True)

# Display Available Chat Titles in the Sidebar (Properly Aligned, Truncated if Too Long)
st.sidebar.subheader("📁 Previous Chats")
for title in st.session_state.chats.keys():
    truncated_title = truncate_title(title, max_chars=25)  # Truncate only if it exceeds length
    if st.sidebar.button(truncated_title, key=f"chat_{title}"):
        st.session_state.current_chat = title
        st.session_state.new_chat_started = False
        st.rerun()  # Ensure UI refreshes when switching chats

# Ensure a chat is selected before proceeding
if not st.session_state.current_chat:
    st.warning("Please start a fresh chat and enter a title to proceed.")
else:
    # Retrieve chat history for the selected chat
    chat_history = st.session_state.chats[st.session_state.current_chat]

    # User Input
    user_input = st.text_input("Enter your prompt here👇")

    if user_input:
        response = chain.invoke(user_input)
        response = clean_response(response)

        # Append latest conversation at the beginning using deque's appendleft()
        chat_history.appendleft(("assistant", response))
        chat_history.appendleft(("user", user_input))

    # Display Chat History (Latest messages first)
    for role, message in chat_history:
        if role == "user":
            with st.chat_message("user"):  # User messages are left-aligned
                st.write(message)
        else:
            with st.chat_message("assistant"):  # Bot messages are right-aligned
                st.write(message)
