import streamlit as st
import nlp_processor as nlp
import medical_kb as kb
from utils import initialize_session_state, display_disclaimer, display_emergency_warning

# Page configuration
st.set_page_config(
    page_title="HealthCare Assistant",
    page_icon="🏥",
    layout="centered"
)

# Initialize session state
initialize_session_state()

# Header and disclaimer
st.title("🏥 Healthcare Assistant")
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stTextInput > div > div > input {
        background-color: white;
    }
</style>
""", unsafe_allow_html=True)

# Display disclaimer
display_disclaimer()

# Chat interface
st.markdown("### Chat with Healthcare Assistant")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your health concern here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Process user input
    processed_input = nlp.process_text(prompt)
    response = kb.generate_response(processed_input)
    
    # Check for emergency keywords
    if kb.is_emergency(processed_input):
        display_emergency_warning()
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)

# Sidebar with additional information
with st.sidebar:
    st.header("Important Information")
    st.warning("""
    This is not a substitute for professional medical advice. 
    If you're experiencing a medical emergency, call your local emergency services immediately.
    """)
    
    st.header("Emergency Contacts")
    st.info("""
    🚑 Emergency: 911\n
    🏥 Poison Control: 1-800-222-1222\n
    💊 Health Line: 811
    """)
