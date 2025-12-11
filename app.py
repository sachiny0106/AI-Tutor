"""
AI Tutor - Local AI Study Buddy

A privacy-focused AI tutoring application that runs entirely on your local machine.
Provides personalized explanations and generates custom quizzes across multiple subjects.

Author: Sachin Yadav
License: MIT
Repository: https://github.com/sachiny0106/AI-Tutor
"""

import streamlit as st
import ollama
from typing import List, Optional
import logging

# ============== Configuration ==============
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Application Constants
APP_TITLE = "🎓 AI Study Buddy - Learn Locally"
EDUCATION_LEVELS = ["School", "High School", "Graduate", "PG/PhD"]
SUBJECTS = ["Math", "History", "Computer Science", "Physics", "Biology", "Chemistry"]
PREFERRED_MODELS = ['gemma3:latest', 'gemma3', 'gemma2:2b', 'gemma2', 'llama3', 'mistral', 'deepseek-coder']


# ============== Helper Functions ==============
def extract_model_name(model_obj) -> Optional[str]:
    """Extract model name from various response formats."""
    if hasattr(model_obj, 'model'):
        return model_obj.model
    elif isinstance(model_obj, dict):
        return model_obj.get('name') or model_obj.get('model') or model_obj.get('id')
    elif isinstance(model_obj, str):
        return model_obj
    return None


def sort_models_by_priority(model_names: List[str]) -> List[str]:
    """Sort models with preferred ones first."""
    prioritized = [m for m in PREFERRED_MODELS if m in model_names]
    remaining = [m for m in model_names if m not in prioritized]
    return prioritized + remaining


@st.cache_data
def fetch_ollama_models() -> List[str]:
    """Fetch and return available Ollama models."""
    try:
        response = ollama.list()
        models = []
        
        # Handle ListResponse object
        if hasattr(response, 'models'):
            models = [extract_model_name(m) for m in response.models]
        elif isinstance(response, dict) and 'models' in response:
            models = [extract_model_name(m) for m in response['models']]
        
        # Filter out None values and sort
        models = [m for m in models if m]
        return sort_models_by_priority(models)
        
    except Exception as e:
        st.error(f"❌ Ollama connection failed: {e}")
        st.info("💡 Run `ollama serve` to start the server")
        return []


def build_prompt(mode: str, level: str, subject: str, user_input: str) -> str:
    """Generate context-aware prompt based on user preferences."""
    if mode == "Explain a Topic":
        return f"""You are an expert {subject} tutor for {level} students.
        
Explain this topic clearly: "{user_input}"

Guidelines:
• Break down complex ideas into simple steps
• Use relevant examples and analogies  
• Keep language appropriate for {level} level
• Be concise but thorough"""
    else:
        return f"""Create a {level}-level {subject} quiz.

Topic: {user_input}

Format:
• One clear question
• Four options (A, B, C, D)
• Mark correct answer with [CORRECT]
• Include brief explanation"""


def display_model_status(model: str, available: List[str]):
    """Show model selection feedback."""
    if 'gemma3' in model.lower():
        st.success("✅ Gemma3 - Optimal for education")
    elif 'deepseek-coder' in model.lower():
        st.success("✅ DeepSeek - Great for coding")
    elif not any('gemma3' in m.lower() for m in available):
        st.info("💡 Try: `ollama pull gemma3`")


def stream_response(model: str, prompt: str, placeholder) -> str:
    """Stream AI response with real-time display."""
    full_response = ""
    try:
        for chunk in ollama.generate(model=model, prompt=prompt, stream=True):
            full_response += chunk["response"]
            placeholder.markdown(full_response + "▌")
        placeholder.markdown(full_response)
    except ollama.ResponseError:
        full_response = f"❌ Model '{model}' not available. Install with: `ollama pull {model}`"
        placeholder.markdown(full_response)
    except Exception as e:
        full_response = f"❌ Error: {e}"
        placeholder.markdown(full_response)
    return full_response


# ============== Session State ==============
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ============== Main UI ==============
st.title(APP_TITLE)

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Settings")
    
    education_level = st.selectbox("Education Level", EDUCATION_LEVELS, index=1)
    subject = st.selectbox("Subject", SUBJECTS, index=2)
    mode = st.radio("Mode", ["Explain a Topic", "Generate a Quiz"])
    
    st.divider()
    
    # Model Selection
    available_models = fetch_ollama_models()
    if available_models:
        selected_model = st.selectbox("AI Model", available_models, index=0)
        display_model_status(selected_model, available_models)
    else:
        st.error("⚠️ No models found")
        st.code("ollama pull gemma3", language="bash")
        selected_model = None
    
    st.divider()
    st.caption("🔒 All data stays on your device")

# Chat Display
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Input Handler
if user_prompt := st.chat_input(f"Ask about {subject}..."):
    if not selected_model:
        st.error("Install an Ollama model first!")
        st.stop()
    
    # Add user message
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)
    
    # Generate AI response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        prompt = build_prompt(mode, education_level, subject, user_prompt)
        ai_response = stream_response(selected_model, prompt, response_placeholder)
    
    st.session_state.chat_history.append({"role": "assistant", "content": ai_response})