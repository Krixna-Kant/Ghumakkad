import google.generativeai as genai
import streamlit as st
from .config import GEMINI_API_KEY, CHATBOT_PROMPT

def initialize_gemini():
    """Initialize the Gemini model"""
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        # Configure the model
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.8,
            "top_k": 40
        }
        
        # Create the model
        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash",
            generation_config=generation_config
        )
        
        # Start a chat
        chat = model.start_chat(history=[])
        return chat
    except Exception as e:
        st.error(f"Error initializing Gemini: {str(e)}")
        return None

def get_chatbot_response(chat, user_input):
    """Get response from the chatbot"""
    try:
        if not chat:
            return "Sorry, I'm not available right now. Please make sure the API key is properly configured."
        
        # Send message and get response
        response = chat.send_message(user_input)
        return response.text
    except Exception as e:
        return f"Error getting response: {str(e)}"

def get_suggested_questions():
    """Return a list of suggested questions"""
    return [
        "What's the best time to visit Rajasthan?",
        "Tell me about Kerala's backwaters",
        "Must-visit places in Varanasi?",
        "Popular festivals in Gujarat",
        "Budget trip to Northeast India",
        "Best trekking spots in Himachal",
        "Famous street food in Delhi",
        "Beaches in Goa to visit"
    ]

def suggest_itinerary(model, preferences, duration=3):
    """Generate a customized itinerary based on user preferences"""
    if not model:
        return None
    
    try:
        prompt = f"""As an Indian tourism expert, create a {duration}-day itinerary based on these preferences: {', '.join(preferences)}.
        Include:
        - Daily activities
        - Cultural experiences
        - Local cuisine recommendations
        - Travel tips
        Format the response in a clear, day-by-day structure."""
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating itinerary: {str(e)}")
        return None

def get_destination_recommendations(model, criteria):
    """Get personalized destination recommendations"""
    if not model:
        return None
    
    try:
        prompt = f"""Recommend 5 Indian destinations that match these criteria: {criteria}.
        For each destination, include:
        - Best time to visit
        - Cultural significance
        - Must-see attractions
        - Local experiences"""
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error getting recommendations: {str(e)}")
        return None 