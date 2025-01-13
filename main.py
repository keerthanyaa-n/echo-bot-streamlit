import streamlit as st
import uuid
import logging

# Setup logging (this acts like console.log in JS)
logging.basicConfig(level=logging.DEBUG)

# Generate a unique thread ID using UUID
if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = str(uuid.uuid4())

# Title
st.title("Echo Bot with Console Logs")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Log the user input to the console
    logging.debug(f"Thread ID: {st.session_state['thread_id']} | User input: {prompt}")

    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate assistant response
    response = f"Echo: {prompt}"
    
    # Log the echoed response to the console
    logging.debug(f"Thread ID: {st.session_state['thread_id']} | Echoed Response: {response}")

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
