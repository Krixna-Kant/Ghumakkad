import streamlit as st
from utils.config import (
    PAGE_CONFIG, THEME_COLOR, BACKGROUND_COLOR, TEXT_COLOR, 
    ACCENT_COLOR, CARD_BACKGROUND, MUTED_TEXT, SECONDARY_COLOR,
    HEADING_COLOR, LINK_COLOR, BORDER_COLOR
)
from utils.map_utils import create_cultural_map, display_state_info, load_map_data
from utils.chatbot_utils import initialize_gemini, get_chatbot_response, suggest_itinerary, get_suggested_questions
from utils.youtube_utils import get_youtube_service, search_youtube_shorts, display_youtube_shorts, get_trending_shorts
from utils.data_loader import (
    get_all_states, get_state_data, load_state_overview,
    load_tourism_stats, load_cultural_info, load_destinations
)
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import requests
from PIL import Image
from io import BytesIO

def arts_revival_section():
    st.markdown("""
    <div style='background-color: rgba(0, 0, 0, 0.3); padding: 2rem; border-radius: 10px; margin: 1rem 0;'>
        <h2 style='color: #FF6B6B;'>Arts Revival - Preserving India's Cultural Heritage</h2>
        <p style='color: #E0E0E0;'>
        India's rich artistic heritage faces numerous challenges in the modern world. Many traditional art forms 
        are at risk of being lost forever. Through this initiative, we aim to raise awareness about endangered art forms 
        and connect art enthusiasts directly with artisan communities.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        df = pd.read_csv('data/endangered_arts.csv')
        
        for _, row in df.iterrows():
            with st.container():
                # Display image at the top if available
                try:
                    response = requests.get(row['art_image'])
                    img = Image.open(BytesIO(response.content))
                    st.image(img, caption=row['art_name'], use_column_width=True)
                except:
                    st.warning(f"Unable to load image for {row['art_name']}")
                
                st.markdown(f"""
                <div style='background-color: rgba(0, 0, 0, 0.3); padding: 2rem; border-radius: 10px; margin: 1rem 0;'>
                    <h3 style='color: #FF6B6B;'>{row['art_name']} - {row['art_type']}</h3>
                    <div style='color: #E0E0E0; margin-bottom: 1rem;'>
                        <strong>State:</strong> {row['state_name']}<br>
                        <strong>Artisan Community:</strong> {row['artisan_community']}<br>
                        <strong>Status:</strong> <span style='color: {"#FF4444" if row["current_status"] in ["Critically Endangered", "Endangered"] else "#FFB302" if row["current_status"] in ["Vulnerable", "At Risk"] else "#66BB6A"}'>{row['current_status']}</span>
                    </div>
                    <p style='color: #E0E0E0;'>{row['description']}</p>
                    <div style='color: #E0E0E0; margin-top: 1rem;'>
                        <strong>Preservation Efforts:</strong><br>
                        {"<br>".join(f"• {effort}" for effort in row['preservation_efforts'].split('|'))}
                    </div>
                    <div style='margin-top: 1rem;'>
                        <a href='{row["purchase_link"]}' target='_blank' style='background-color: #FF6B6B; color: white; padding: 0.5rem 1rem; text-decoration: none; border-radius: 5px; display: inline-block;'>🛍️ Support this Art Form</a>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("<hr style='margin: 2rem 0; border-color: rgba(255, 255, 255, 0.1);'>", unsafe_allow_html=True)
                
    except Exception as e:
        st.error("Error loading arts data. Please check the data file.")

# Configure the app
st.set_page_config(**PAGE_CONFIG)

# Add custom CSS
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {BACKGROUND_COLOR};
        color: {TEXT_COLOR};
    }}
    .main {{
        padding: 1rem;
    }}
    h1, h2, h3 {{
        color: {HEADING_COLOR} !important;
        font-weight: 600;
    }}
    p {{
        color: {TEXT_COLOR} !important;
    }}
    .stButton>button {{
        background-color: {THEME_COLOR};
        color: {TEXT_COLOR};
        border-radius: 10px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: 500;
    }}
    .stButton>button:hover {{
        background-color: {ACCENT_COLOR};
        color: {BACKGROUND_COLOR};
    }}
    .stSelectbox {{
        background-color: {CARD_BACKGROUND};
        border-radius: 10px;
        border: 1px solid {BORDER_COLOR};
    }}
    .stTextInput>div>div>input {{
        background-color: {CARD_BACKGROUND} !important;
        color: {TEXT_COLOR} !important;
        border-radius: 10px;
        border: 1px solid {BORDER_COLOR} !important;
    }}
    .nav-link {{
        text-decoration: none;
        color: {TEXT_COLOR};
        font-weight: 500;
        padding: 10px 20px;
        border-radius: 20px;
        transition: all 0.3s ease;
        background-color: {CARD_BACKGROUND};
        border: 1px solid {BORDER_COLOR};
    }}
    .nav-link:hover {{
        background-color: {ACCENT_COLOR};
        color: {BACKGROUND_COLOR};
    }}
    .nav-link.active {{
        background-color: {THEME_COLOR};
        color: {TEXT_COLOR};
    }}
    [data-testid="stSidebar"] {{
        background-color: {CARD_BACKGROUND};
        border-right: 1px solid {BORDER_COLOR};
    }}
    [data-testid="stToolbar"] {{
        background-color: {CARD_BACKGROUND};
        border-bottom: 1px solid {BORDER_COLOR};
    }}
    .stRadio > label {{
        color: {TEXT_COLOR} !important;
        font-weight: 500;
    }}
    .stRadio > div {{
        background-color: {CARD_BACKGROUND};
        border-radius: 10px;
        padding: 10px;
        border: 1px solid {BORDER_COLOR};
    }}
    .stRadio > div > div {{
        background-color: transparent !important;
    }}
    .stMarkdown a {{
        color: {LINK_COLOR} !important;
        text-decoration: none;
    }}
    .stMarkdown a:hover {{
        text-decoration: underline;
    }}
    </style>
""", unsafe_allow_html=True)

# Initialize services
gemini_model = initialize_gemini()
youtube_service = get_youtube_service()

# Top Navigation Bar
st.markdown(f"""
    <div style="
        background-color: {CARD_BACKGROUND};
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        border: 1px solid {BORDER_COLOR};
        display: flex;
        justify-content: space-between;
        align-items: center;
    ">
        <div style="display: flex; align-items: center;">
            <h1 style="margin: 0; color: {HEADING_COLOR}; font-size: 2em;">🗺️ Ghumakkad</h1>
            <span style="margin-left: 15px; color: {MUTED_TEXT};">Discover India's Rich Cultural Heritage</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Navigation tabs
page = st.radio(
    "",
    ["Cultural Map", "Plan Your Yatra", "Destination Insights", "Arts Revival"],
    horizontal=True,
    label_visibility="collapsed"
)

# Main content container
st.markdown(f"""
    <div style="
        background-color: {CARD_BACKGROUND};
        padding: 2rem;
        border-radius: 15px;
        margin-top: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        border: 1px solid {BORDER_COLOR};
    ">
""", unsafe_allow_html=True)

if page == "Cultural Map":
    st.markdown(f"""
        <h2 style='color: {HEADING_COLOR}; font-size: 2em; margin-bottom: 1em;'>
            Interactive Cultural Map of India
        </h2>
        <p style='color: {MUTED_TEXT}; font-size: 1.1em; margin-bottom: 2em;'>
            Explore India's diverse cultural landscape through our interactive map. 
            Click on any state to discover its unique heritage, attractions, and hidden gems.
        </p>
    """, unsafe_allow_html=True)
    
    # Create and display map
    cultural_map = create_cultural_map()
    if cultural_map:
        st.components.v1.html(cultural_map._repr_html_(), height=600)
        
        # State selection
        st.markdown(f"<h3 style='color: {HEADING_COLOR}; margin: 2em 0 1em 0;'>Explore State Details</h3>", unsafe_allow_html=True)
        df = load_map_data()
        if df is not None:
            selected_state = st.selectbox(
                "Select a state to learn more",
                sorted(df['State_UT'].unique()),
                format_func=lambda x: f"📍 {x}",
                label_visibility="collapsed"
            )
            if selected_state:
                display_state_info(selected_state, df)

elif page == "Plan Your Yatra":
    # Initialize chat if not already done
    if 'chat' not in st.session_state:
        st.session_state.chat = initialize_gemini()
    
    # Two-column layout with adjusted ratios
    col1, col2 = st.columns([7, 3])
    
    with col1:
        # Chat container with cleaner layout and no empty space
        st.markdown(f"""
            <div style='background-color: {CARD_BACKGROUND}; 
                        padding: 15px; 
                        border-radius: 10px; 
                        border: 1px solid {BORDER_COLOR};
                        height: 80vh;
                        display: flex;
                        flex-direction: column;'>
                <div style='margin-bottom: 10px;'>
                    <h3 style='color: {THEME_COLOR}; margin: 0; font-size: 1.2em;'>Chat with Travel Expert</h3>
                    <p style='color: {MUTED_TEXT}; margin: 3px 0 0 0; font-size: 0.9em;'>
                        Ask me anything about traveling in India
                    </p>
                </div>
                <div id="chat-container" style='flex-grow: 1; 
                                              overflow-y: auto; 
                                              margin: 10px 0;
                                              padding-right: 8px;
                                              display: flex;
                                              flex-direction: column;
                                              justify-content: flex-start;'>
        """, unsafe_allow_html=True)
        
        # Initialize chat history if not exists
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        
        # Display welcome message if no chat history
        if not st.session_state.chat_history:
            st.markdown(f"""
                <div style='background-color: {BACKGROUND_COLOR}; 
                           color: {TEXT_COLOR};
                           padding: 10px 15px;
                           border-radius: 15px;
                           margin: 8px 0;
                           max-width: 85%;
                           border: 1px solid {BORDER_COLOR};
                           font-size: 0.95em;'>
                    👋 Hi! I'm your travel expert for exploring India. I can help you with:
                    <ul style='margin: 8px 0; padding-left: 20px;'>
                        <li>Planning your itinerary</li>
                        <li>Finding the best places to visit</li>
                        <li>Local culture and customs</li>
                        <li>Travel tips and recommendations</li>
                    </ul>
                    Feel free to ask me anything!
                </div>
            """, unsafe_allow_html=True)
        
        # Display chat history with improved styling
        for role, message in st.session_state.chat_history:
            if role == "user":
                st.markdown(f"""
                    <div style='background-color: {THEME_COLOR}; 
                               color: white;
                               padding: 10px 15px;
                               border-radius: 15px 15px 5px 15px;
                               margin: 8px 0;
                               max-width: 85%;
                               margin-left: auto;
                               font-size: 0.95em;
                               box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                        {message}
                    </div>
                """, unsafe_allow_html=True)
            else:
                # Process bot message to remove any stray HTML tags
                cleaned_message = message.replace('</div>', '').strip()
                st.markdown(f"""
                    <div style='background-color: {BACKGROUND_COLOR}; 
                               color: {TEXT_COLOR};
                               padding: 10px 15px;
                               border-radius: 15px 15px 15px 5px;
                               margin: 8px 0;
                               max-width: 85%;
                               border: 1px solid {BORDER_COLOR};
                               font-size: 0.95em;'>
                        {cleaned_message}
                    </div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Input area with improved styling
        st.markdown(f"""
            <style>
            .stTextInput > div > div > input {{
                color: {TEXT_COLOR} !important;
                background-color: {BACKGROUND_COLOR} !important;
                border: 1px solid {BORDER_COLOR} !important;
                font-size: 0.95em !important;
                padding: 8px 12px !important;
                border-radius: 8px !important;
                margin-bottom: 0 !important;
            }}
            .stTextInput > div > div > input::placeholder {{
                color: {MUTED_TEXT} !important;
                opacity: 0.8 !important;
            }}
            .stButton > button {{
                background-color: {THEME_COLOR} !important;
                color: white !important;
                font-size: 0.95em !important;
                padding: 0.45em 1em !important;
                border-radius: 8px !important;
                border: none !important;
                margin-top: 0 !important;
            }}
            </style>
        """, unsafe_allow_html=True)
        
        # Input row with better spacing
        input_col1, input_col2 = st.columns([5, 1])
        with input_col1:
            user_input = st.text_input(
                "",
                key="chat_input",
                placeholder="Type your question here...",
                label_visibility="collapsed"
            )
        with input_col2:
            send_button = st.button("Send", use_container_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        # Suggested questions with improved styling
        st.markdown(f"""
            <div style='background-color: {CARD_BACKGROUND}; 
                        padding: 12px; 
                        border-radius: 10px; 
                        border: 1px solid {BORDER_COLOR};'>
                <h4 style='color: {THEME_COLOR}; 
                           margin: 0 0 10px 0; 
                           font-size: 1em;'>
                    Suggested Questions
                </h4>
        """, unsafe_allow_html=True)
        
        # Display suggested questions with compact styling
        for question in get_suggested_questions():
            if st.button(
                question,
                key=f"q_{question}",
                use_container_width=True,
                type="secondary"
            ):
                user_input = question
                st.session_state.user_input = question
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Handle user input
    if user_input and (send_button or user_input != st.session_state.get('last_input', '')):
        if st.session_state.chat:
            # Add user message to chat history
            st.session_state.chat_history.append(("user", user_input))
            st.session_state.last_input = user_input
            
            with st.spinner("Thinking..."):
                # Get bot response
                response = get_chatbot_response(st.session_state.chat, user_input)
                # Add bot response to chat history
                st.session_state.chat_history.append(("bot", response))
            
            # Clear input and rerun to update chat
            st.session_state.user_input = ""
            st.rerun()

elif page == "Destination Insights":
    st.markdown(f"""
        <div style='background-color: {CARD_BACKGROUND}; 
                    padding: 20px; 
                    border-radius: 10px; 
                    border: 1px solid {BORDER_COLOR};'>
            <h2 style='color: {HEADING_COLOR}; margin-bottom: 1rem;'>Destination Insights</h2>
            <p style='color: {MUTED_TEXT}; margin-bottom: 2rem;'>
                Discover detailed insights about Indian destinations - from popular attractions to hidden gems, 
                local culture to tourism statistics.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Search Section with single column
    st.markdown(f"""
        <div style='margin: 2rem 0;'>
            <h3 style='color: {HEADING_COLOR}; margin-bottom: 1rem;'>Explore Destinations</h3>
        </div>
    """, unsafe_allow_html=True)
    
    destination = st.selectbox(
        "Select a destination",
        get_all_states(),
        placeholder="Choose a state",
        label_visibility="collapsed"
    )

    # Main content area with tabs
    if destination:
        state_data = get_state_data(destination)
        overview_data = load_state_overview(destination)
        tourism_data = load_tourism_stats(destination)
        cultural_data = load_cultural_info(destination)
        destinations_data = load_destinations(destination)

        # Display state banner image
        if 'banner_image' in state_data:
            st.image(state_data['banner_image'], use_column_width=True)

        st.markdown(f"""
            <div style='background-color: {CARD_BACKGROUND}; 
                        padding: 20px; 
                        border-radius: 10px; 
                        border: 1px solid {BORDER_COLOR};
                        margin: 2rem 0;'>
                <h3 style='color: {HEADING_COLOR}; margin-bottom: 1rem;'>{destination}</h3>
            </div>
        """, unsafe_allow_html=True)

        tabs = st.tabs([
            "Overview", 
            "Tourism Analytics", 
            "Cultural Insights",
            "Places to Visit",
            "Local Cuisine"
        ])

        with tabs[0]:  # Overview Tab
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown("### Quick Facts")
                st.markdown(f"- **Capital:** {overview_data.get('capital', 'N/A')}")
                st.markdown(f"- **Best Time to Visit:** {overview_data.get('best_time', 'N/A')}")
                st.markdown("- **Known For:**")
                known_for = overview_data.get('known_for', '').split('|')
                for item in known_for:
                    if item:
                        st.markdown(f"  * {item.strip()}")
                st.markdown("- **Languages Spoken:**")
                languages = overview_data.get('languages', '').split('|')
                for lang in languages:
                    if lang:
                        st.markdown(f"  * {lang.strip()}")
                st.markdown(f"- **Climate:** {overview_data.get('climate', 'N/A')}")
                st.markdown(f"- **Geography:** {overview_data.get('geography', 'N/A')}")

            with col2:
                st.markdown("### Weather")
                # Create state-specific weather visualization based on climate data
                months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                
                # Define temperature patterns based on climate type
                climate = overview_data.get('climate', '').lower()
                if 'tropical' in climate:
                    temps = [24, 25, 26, 28, 29, 28, 27, 27, 26, 25, 24, 24]  # Tropical pattern
                elif 'cold' in climate or 'alpine' in climate:
                    temps = [-5, -2, 2, 8, 12, 15, 18, 17, 14, 8, 2, -2]  # Cold/Alpine pattern
                elif 'hot' in climate or 'arid' in climate:
                    temps = [20, 22, 28, 32, 35, 38, 35, 33, 30, 27, 23, 20]  # Hot/Arid pattern
                elif 'subtropical' in climate:
                    temps = [18, 20, 24, 28, 32, 33, 30, 29, 28, 25, 22, 19]  # Subtropical pattern
                elif 'moderate' in climate:
                    temps = [15, 17, 20, 24, 27, 28, 27, 26, 25, 22, 18, 16]  # Moderate pattern
                else:
                    temps = [20, 22, 25, 28, 30, 29, 28, 27, 26, 24, 22, 20]  # Default pattern
                
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=months, 
                    y=temps,
                    name='Temperature (°C)',
                    line=dict(color='#FF9800', width=3)
                ))
                fig.update_layout(
                    title='Average Monthly Temperature',
                    xaxis_title='Month',
                    yaxis_title='Temperature (°C)',
                    template='plotly_dark',
                    height=300,
                    margin=dict(t=30, l=60, r=30, b=30)
                )
                st.plotly_chart(fig, use_container_width=True)

        with tabs[1]:  # Tourism Analytics Tab
            st.markdown("### Tourism Statistics")
            
            # Create tourism growth chart
            yearly_stats = tourism_data.get('yearly_stats', [])
            years = [stat['year'] for stat in yearly_stats]
            domestic = [stat['domestic_visitors'] for stat in yearly_stats]
            foreign = [stat['foreign_visitors'] for stat in yearly_stats]
            growth = [stat['growth_rate'] for stat in yearly_stats]
            total = [stat['total_visitors'] for stat in yearly_stats]
            
            # Overview metrics
            latest_year = years[0] if years else "N/A"
            latest_total = total[0] if total else 0
            latest_growth = growth[0] if growth else 0
            
            metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
            with metrics_col1:
                st.metric(
                    "Total Visitors (Latest)",
                    f"{latest_total:,}",
                    f"{latest_growth:+.1f}% vs prev year"
                )
            with metrics_col2:
                domestic_share = (domestic[0] / latest_total * 100) if latest_total > 0 else 0
                st.metric(
                    "Domestic Share",
                    f"{domestic_share:.1f}%",
                    f"{domestic[0]:,} visitors"
                )
            with metrics_col3:
                foreign_share = (foreign[0] / latest_total * 100) if latest_total > 0 else 0
                st.metric(
                    "International Share",
                    f"{foreign_share:.1f}%",
                    f"{foreign[0]:,} visitors"
                )

            st.markdown("---")
            
            col1, col2 = st.columns(2)
            with col1:
                # Visitor trends
                fig = go.Figure()
                fig.add_trace(go.Bar(x=years, y=domestic, name='Domestic Visitors'))
                fig.add_trace(go.Bar(x=years, y=foreign, name='Foreign Visitors'))
                fig.update_layout(
                    title='Visitor Trends',
                    barmode='stack',
                    template='plotly_dark',
                    xaxis_title='Year',
                    yaxis_title='Number of Visitors'
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Growth rate
                fig = go.Figure()
                fig.add_trace(go.Line(x=years, y=growth, name='Growth Rate'))
                fig.add_trace(go.Bar(x=years, y=growth, name='Growth Rate', opacity=0.3))
                fig.update_layout(
                    title='Tourism Growth Rate (%)',
                    template='plotly_dark',
                    xaxis_title='Year',
                    yaxis_title='Growth Rate (%)'
                )
                st.plotly_chart(fig, use_container_width=True)

            # Monthly distribution if available
            if 'monthly_distribution' in tourism_data:
                st.markdown("### Seasonal Patterns")
                monthly_data = tourism_data['monthly_distribution']
                
                col1, col2 = st.columns(2)
                with col1:
                    # Monthly visitors distribution
                    fig = go.Figure()
                    fig.add_trace(go.Line(
                        x=monthly_data['months'],
                        y=monthly_data['visitors'],
                        name='Visitors',
                        fill='tozeroy'
                    ))
                    fig.update_layout(
                        title='Monthly Visitor Distribution',
                        template='plotly_dark',
                        xaxis_title='Month',
                        yaxis_title='Average Visitors'
                    )
                    st.plotly_chart(fig, use_container_width=True)
                
                with col2:
                    # Peak season analysis
                    peak_months = [m for i, m in enumerate(monthly_data['months']) 
                                 if monthly_data['visitors'][i] > sum(monthly_data['visitors'])/len(monthly_data['visitors'])]
                    
                    st.markdown("#### Peak Season Analysis")
                    st.markdown(f"**Peak Months:** {', '.join(peak_months)}")
                    
                    # Create a heatmap for occupancy rates
                    fig = go.Figure(data=go.Heatmap(
                        z=[monthly_data['occupancy_rate']],
                        x=monthly_data['months'],
                        colorscale='Viridis',
                        showscale=True
                    ))
                    fig.update_layout(
                        title='Hotel Occupancy Rates by Month (%)',
                        template='plotly_dark',
                        height=200
                    )
                    st.plotly_chart(fig, use_container_width=True)

            # Tourism impact metrics if available
            if 'impact_metrics' in tourism_data:
                st.markdown("### Economic Impact")
                impact = tourism_data['impact_metrics']
                
                metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)
                with metrics_col1:
                    st.metric(
                        "Revenue Generated",
                        f"₹{impact['revenue_cr']:,} Cr",
                        f"{impact['revenue_growth']:+.1f}%"
                    )
                with metrics_col2:
                    st.metric(
                        "Employment Generated",
                        f"{impact['employment']:,}",
                        f"{impact['employment_growth']:+.1f}%"
                    )
                with metrics_col3:
                    st.metric(
                        "Hotels/Accommodations",
                        f"{impact['hotels']:,}",
                        f"{impact['hotels_growth']:+.1f}%"
                    )
                with metrics_col4:
                    st.metric(
                        "Avg. Stay Duration",
                        f"{impact['avg_stay']:.1f} days",
                        f"{impact['stay_duration_change']:+.1f} days"
                    )

        with tabs[2]:  # Cultural Insights Tab
            st.markdown("### Cultural Heritage")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### Traditional Art Forms")
                for art in cultural_data.get('art_forms', []):
                    st.markdown(f"""
                        <div style='background-color: {BACKGROUND_COLOR}; 
                                   padding: 15px; 
                                   border-radius: 10px; 
                                   margin: 10px 0;
                                   border: 1px solid {BORDER_COLOR};'>
                            <h4 style='color: {HEADING_COLOR}; margin: 0;'>{art['name']}</h4>
                            <p style='color: {TEXT_COLOR}; margin: 5px 0 0 0;'>{art['description']}</p>
                        </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("#### Festivals")
                for festival in cultural_data.get('festivals', []):
                    st.markdown(f"""
                        <div style='background-color: {BACKGROUND_COLOR}; 
                                   padding: 15px; 
                                   border-radius: 10px; 
                                   margin: 10px 0;
                                   border: 1px solid {BORDER_COLOR};'>
                            <h4 style='color: {HEADING_COLOR}; margin: 0;'>{festival['name']}</h4>
                            <p style='color: {MUTED_TEXT}; margin: 2px 0;'>{festival['month']}</p>
                            <p style='color: {TEXT_COLOR}; margin: 5px 0 0 0;'>{festival['description']}</p>
                        </div>
                    """, unsafe_allow_html=True)

        with tabs[3]:  # Places to Visit Tab
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown("### Must-Visit Destinations")
                for place in destinations_data.get('popular', []):
                    st.markdown(f"""
                        <div style='background-color: {BACKGROUND_COLOR}; 
                                   padding: 15px; 
                                   border-radius: 10px; 
                                   margin: 10px 0;
                                   border: 1px solid {BORDER_COLOR};'>
                            <h4 style='color: {HEADING_COLOR}; margin: 0;'>{place['name']}</h4>
                            <p style='color: {TEXT_COLOR}; margin: 5px 0;'>{place['description']}</p>
                            <p style='color: {MUTED_TEXT}; margin: 5px 0;'>Best Time: {place['best_time']}</p>
                            <p style='color: {THEME_COLOR}; margin: 5px 0;'>Attractions:</p>
                            <ul style='color: {TEXT_COLOR}; margin: 5px 0;'>
                                {''.join(f"<li>{attraction}</li>" for attraction in place['attractions'])}
                            </ul>
                        </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("### Hidden Gems")
                for place in destinations_data.get('hidden_gems', []):
                    st.markdown(f"""
                        <div style='background-color: {BACKGROUND_COLOR}; 
                                   padding: 15px; 
                                   border-radius: 10px; 
                                   margin: 10px 0;
                                   border: 1px solid {BORDER_COLOR};'>
                            <h4 style='color: {HEADING_COLOR}; margin: 0;'>{place['name']}</h4>
                            <p style='color: {TEXT_COLOR}; margin: 5px 0;'>{place['description']}</p>
                            <p style='color: {MUTED_TEXT}; margin: 5px 0;'>Best Time: {place['best_time']}</p>
                            <p style='color: {THEME_COLOR}; margin: 5px 0;'>Attractions:</p>
                            <ul style='color: {TEXT_COLOR}; margin: 5px 0;'>
                                {''.join(f"<li>{attraction}</li>" for attraction in place['attractions'])}
                            </ul>
                        </div>
                    """, unsafe_allow_html=True)

        with tabs[4]:  # Local Cuisine Tab
            st.markdown("### Food & Cuisine")
            cuisine_cols = st.columns(3)
            for idx, cuisine in enumerate(cultural_data.get('cuisines', [])):
                with cuisine_cols[idx % 3]:
                    st.markdown(f"""
                        <div style='background-color: {BACKGROUND_COLOR}; 
                                   padding: 15px; 
                                   border-radius: 10px; 
                                   margin: 10px 0;
                                   border: 1px solid {BORDER_COLOR};'>
                            <h4 style='color: {HEADING_COLOR}; margin: 0;'>{cuisine['name']}</h4>
                            <p style='color: {TEXT_COLOR}; margin: 5px 0;'>{cuisine['description']}</p>
                        </div>
                    """, unsafe_allow_html=True)

elif page == "Arts Revival":
    arts_revival_section()
    st.markdown("""
    <div style='background-color: rgba(0, 0, 0, 0.3); padding: 2rem; border-radius: 10px; margin: 1rem 0;'>
        <h3 style='color: #FF6B6B;'>How You Can Help</h3>
        <ul style='color: #E0E0E0;'>
            <li>Purchase Traditional Art: Support artisans by buying authentic pieces</li>
            <li>Spread Awareness: Share information about these art forms</li>
            <li>Learn More: Research and document these traditions</li>
            <li>Visit Artisan Communities: Experience the craft firsthand</li>
        </ul>
        <p style='color: #E0E0E0; font-style: italic;'>Together, we can preserve India's artistic heritage for future generations.</p>
    </div>
    """, unsafe_allow_html=True)

# Close main content container
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown(f"""
    <div style='text-align: center; padding: 2rem; color: {MUTED_TEXT};'>
        <p>Made with ❤️ for YourStory x Snowflake Hackathon</p>
        <div style='margin-top: 0.5rem;'>
            <a href='https://github.com' style='color: {LINK_COLOR}; text-decoration: none; margin: 0 10px;'>GitHub</a> | 
            <a href='https://yourstory.com' style='color: {LINK_COLOR}; text-decoration: none; margin: 0 10px;'>About</a>
        </div>
    </div>
""", unsafe_allow_html=True) 