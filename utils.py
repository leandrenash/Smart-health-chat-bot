import streamlit as st

def initialize_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I'm your Healthcare Assistant. How can I help you today? Please describe your symptoms or health concerns."}
        ]

def display_disclaimer():
    """Display medical disclaimer."""
    st.markdown("""
    <div style='background-color: #f8d7da; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;'>
        <h4 style='color: #721c24; margin: 0;'>⚠️ Medical Disclaimer</h4>
        <p style='color: #721c24; margin: 0.5rem 0 0 0;'>
            This chatbot provides general information only and is not a substitute for professional medical advice. 
            Always consult with a qualified healthcare provider for medical diagnosis and treatment.
        </p>
    </div>
    """, unsafe_allow_html=True)

def display_emergency_warning():
    """Display emergency warning message."""
    st.error("""
    🚨 EMERGENCY WARNING 🚨
    
    Your symptoms may indicate a serious medical condition requiring immediate attention.
    Please:
    1. Call emergency services (911) immediately
    2. Seek immediate medical care
    3. Do not wait or delay getting professional help
    """)

def format_response(text: str) -> str:
    """Format response text for better readability."""
    return text.replace('\n', '<br>')
