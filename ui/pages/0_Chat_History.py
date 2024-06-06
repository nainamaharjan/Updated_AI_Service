import streamlit as st

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Chat History")

# Check if there are chat messages in session state
if not st.session_state.messages:
    st.write("No chat messages yet.")
else:
    # Display chat messages
    for message in st.session_state.messages:
        role = message.get("role")
        task = message.get("task", "")
        input_text = message.get("input", "")
        output_text = message.get("content", message.get("output", ""))

        if role == "user":
            st.markdown(f"**User:** {input_text}")
        elif role == "assistant":
            st.markdown(f"**Assistant:** {output_text}")
        elif role == "system":
            st.markdown(f"**System ({task}):** {input_text} \n**Output:** {output_text}")

# Add a divider for better visualization
st.markdown("---")
