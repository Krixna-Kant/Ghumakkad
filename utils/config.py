import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

# Constants
REGIONS = {
    'North': ['Delhi', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Ladakh', 'Punjab', 'Rajasthan', 'Uttarakhand', 'Uttar Pradesh'],
    'South': ['Andhra Pradesh', 'Karnataka', 'Kerala', 'Tamil Nadu', 'Telangana'],
    'East': ['Bihar', 'Jharkhand', 'Odisha', 'West Bengal'],
    'West': ['Gujarat', 'Goa', 'Maharashtra'],
    'Central': ['Madhya Pradesh', 'Chhattisgarh'],
    'Northeast': ['Arunachal Pradesh', 'Assam', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Sikkim', 'Tripura']
}

# Dark theme colors
THEME_COLOR = "#FF6B6B"  # Coral red - primary accent
SECONDARY_COLOR = "#4ECDC4"  # Turquoise - secondary accent
BACKGROUND_COLOR = "#121212"  # Very dark gray - main background
CARD_BACKGROUND = "#1E1E1E"  # Slightly lighter dark - card background
TEXT_COLOR = "#FFFFFF"  # Pure white - primary text
ACCENT_COLOR = "#FFD93D"  # Bright yellow - highlights
MUTED_TEXT = "#E0E0E0"  # Light gray - secondary text
HEADING_COLOR = "#FF8A8A"  # Lighter coral - headings
LINK_COLOR = "#6BC4FF"  # Light blue - links
BORDER_COLOR = "#333333"  # Dark gray - borders

# Page configuration
PAGE_CONFIG = {
    "page_title": "Ghumakkad",
    "page_icon": "🗺️",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Map configuration
MAP_CENTER = [23.5937, 78.9629]  # Center of India
MAP_ZOOM = 5

# State coordinates for map markers
STATE_COORDINATES = {
    'Delhi': [28.7041, 77.1025],
    'Maharashtra': [19.7515, 75.7139],
    'Tamil Nadu': [11.1271, 78.6569],
    'Karnataka': [15.3173, 75.7139],
    'Gujarat': [22.2587, 71.1924],
    'Rajasthan': [27.0238, 74.2179],
    'Kerala': [10.8505, 76.2711],
    'Uttar Pradesh': [26.8467, 80.9462],
    'West Bengal': [22.9868, 87.8550],
    'Telangana': [17.1231, 79.2088],
    'Andhra Pradesh': [15.9129, 79.7400],
    'Madhya Pradesh': [22.9734, 78.6569],
    'Punjab': [31.1471, 75.3412],
    'Haryana': [29.0588, 76.0856],
    'Bihar': [25.0961, 85.3131],
    'Odisha': [20.9517, 85.0985],
    'Jharkhand': [23.6102, 85.2799],
    'Assam': [26.2006, 92.9376],
    'Uttarakhand': [30.0668, 79.0193],
    'Himachal Pradesh': [31.1048, 77.1734],
    'Jammu and Kashmir': [33.7782, 76.5762],
    'Chhattisgarh': [21.2787, 81.8661],
    'Goa': [15.2993, 74.1240],
    'Arunachal Pradesh': [28.2180, 94.7278],
    'Manipur': [24.6637, 93.9063],
    'Mizoram': [23.1645, 92.9376],
    'Meghalaya': [25.4670, 91.3662],
    'Nagaland': [26.1584, 94.5624],
    'Sikkim': [27.5330, 88.5122],
    'Tripura': [23.9408, 91.9882],
    'Ladakh': [34.2996, 78.2932],
    'Puducherry': [11.9416, 79.8083],
    'Chandigarh': [30.7333, 76.7794],
    'Andaman and Nicobar Islands': [11.7401, 92.6586],
    'Lakshadweep': [10.5667, 72.6417],
    'Dadra and Nagar Haveli and Daman and Diu': [20.1809, 73.0169]
}

# Chatbot configuration
CHATBOT_PROMPT = """You are a knowledgeable Indian tourism expert. 
Help users discover cultural experiences and travel destinations in India. 
Provide specific, accurate information about cultural heritage, art forms, and tourism.""" 