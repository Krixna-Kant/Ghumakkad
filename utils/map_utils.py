import pandas as pd
import folium
import streamlit as st
from streamlit_folium import folium_static
from .config import MAP_CENTER, MAP_ZOOM, REGIONS, STATE_COORDINATES, THEME_COLOR, ACCENT_COLOR, CARD_BACKGROUND, BORDER_COLOR, BACKGROUND_COLOR

def load_map_data():
    """Load and process the map dataset"""
    try:
        df = pd.read_csv('Datasets/interactive_map_dataset.csv')
        return df
    except Exception as e:
        st.error(f"Error loading map data: {str(e)}")
        return None

def create_state_popup(state_data):
    """Create an HTML popup for state information"""
    return f"""
    <div style="width: 300px; 
                font-family: 'Roboto', sans-serif; 
                background-color: {CARD_BACKGROUND}; 
                color: white;
                padding: 20px; 
                border-radius: 10px; 
                border: 1px solid {BORDER_COLOR};">
        <h3 style="color: {THEME_COLOR}; 
                   margin-bottom: 15px; 
                   font-size: 1.5em; 
                   font-weight: 600;">{state_data['State_UT']}</h3>
        <img src="{state_data['Image_URL']}" 
             style="width: 100%; 
                    height: 150px; 
                    object-fit: cover; 
                    border-radius: 8px; 
                    margin-bottom: 15px;">
        <div style="background-color: {BACKGROUND_COLOR}; 
                    padding: 15px; 
                    border-radius: 8px; 
                    margin-bottom: 15px; 
                    border: 1px solid {BORDER_COLOR};">
            <p style="margin: 8px 0; color: white;">
                <strong style="color: {ACCENT_COLOR};">Region:</strong> {state_data['Region']}
            </p>
            <p style="margin: 8px 0; color: white;">
                <strong style="color: {ACCENT_COLOR};">Best Time to Visit:</strong> {state_data['Best_Season']}
            </p>
            <p style="margin: 8px 0; color: white;">
                <strong style="color: {ACCENT_COLOR};">Famous Art Form:</strong> {state_data['Popular_Art_Form']}
            </p>
        </div>
        <div style="margin-top: 15px;">
            <h4 style="color: {THEME_COLOR}; 
                       margin: 10px 0; 
                       font-weight: 600;">Popular Attractions</h4>
            <p style="margin: 8px 0; 
                      color: white; 
                      line-height: 1.4;">{state_data['Popular_Attractions']}</p>
        </div>
        <div style="margin-top: 15px;">
            <h4 style="color: {THEME_COLOR}; 
                       margin: 10px 0; 
                       font-weight: 600;">Hidden Gems</h4>
            <p style="margin: 8px 0; 
                      color: white; 
                      line-height: 1.4;">{state_data['Hidden_Gems']}</p>
        </div>
    </div>
    """

def create_cultural_map():
    """Create an interactive folium map with cultural data"""
    # Create base map with a modern style
    m = folium.Map(
        location=MAP_CENTER,
        zoom_start=MAP_ZOOM,
        tiles='CartoDB positron',
        min_zoom=4,
        max_zoom=7,
        max_bounds=True,
        min_lat=6,
        max_lat=37,
        min_lon=68,
        max_lon=98
    )
    
    # Add a title to the map
    title_html = '''
        <div style="position: fixed; 
                    top: 10px; 
                    left: 50px; 
                    width: 300px; 
                    height: 60px; 
                    z-index: 9999; 
                    background-color: white; 
                    border-radius: 10px;
                    padding: 10px;
                    box-shadow: 0 0 15px rgba(0,0,0,0.2);">
            <h3 style="color: #FF6B6B; margin: 0;">Explore India's Cultural Heritage</h3>
            <p style="margin: 5px 0 0 0; color: #666;">Click on markers to discover more</p>
        </div>
    '''
    m.get_root().html.add_child(folium.Element(title_html))
    
    # Load data
    df = load_map_data()
    if df is None:
        return None
    
    # Create feature group for markers
    markers = folium.FeatureGroup(name="State Markers")
    
    # Add state markers with popups
    for _, row in df.iterrows():
        state_name = row['State_UT']
        if state_name in STATE_COORDINATES:
            # Create custom icon
            icon = folium.DivIcon(
                html=f'''
                    <div style="width: 15px; 
                              height: 15px; 
                              background-color: {row['Map_Highlight_Color']}; 
                              border-radius: 50%; 
                              border: 3px solid white;
                              box-shadow: 0 0 10px rgba(0,0,0,0.3);">
                    </div>
                '''
            )
            
            # Create marker with popup
            folium.Marker(
                location=STATE_COORDINATES[state_name],
                icon=icon,
                popup=folium.Popup(
                    create_state_popup(row),
                    max_width=350
                ),
                tooltip=f"Click to explore {state_name}"
            ).add_to(markers)
    
    # Add markers to map
    markers.add_to(m)
    
    # Set map bounds to India
    m.fit_bounds([[6, 68], [37, 98]])
    
    return m

def display_state_info(state_name, df):
    """Display detailed information about a selected state"""
    if df is None:
        return
    
    try:
        state_data = df[df['State_UT'] == state_name].iloc[0]
        
        # Create modern card layout
        st.markdown(f"""
            <div style='background-color: {CARD_BACKGROUND}; 
                        padding: 30px; 
                        border-radius: 15px; 
                        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
                        margin-bottom: 20px;
                        border: 1px solid {BORDER_COLOR};'>
                <div style='display: flex; align-items: center; margin-bottom: 20px;'>
                    <h2 style='color: {THEME_COLOR}; margin: 0; font-size: 2.2em;'>{state_name}</h2>
                    <span style='background-color: {THEME_COLOR}; 
                               color: white; 
                               padding: 8px 20px; 
                               border-radius: 20px; 
                               margin-left: 15px;
                               font-weight: 600;'>{state_data['Region']}</span>
                </div>
                <img src='{state_data['Image_URL']}' 
                     style='width: 100%; 
                            height: 300px; 
                            object-fit: cover; 
                            border-radius: 10px; 
                            margin-bottom: 20px;'>
                <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 20px;'>
                    <div style='background-color: {BACKGROUND_COLOR}; 
                               padding: 25px; 
                               border-radius: 10px;
                               border: 1px solid {BORDER_COLOR};'>
                        <h3 style='color: {THEME_COLOR}; 
                                 margin-bottom: 20px; 
                                 font-size: 1.8em; 
                                 font-weight: 600;'>Quick Facts</h3>
                        <p style='color: white; 
                                 font-size: 1.1em; 
                                 margin-bottom: 15px;'>
                            <strong style='color: {ACCENT_COLOR}; 
                                       display: block; 
                                       margin-bottom: 5px;'>Best Time to Visit:</strong> 
                            {state_data['Best_Season']}
                        </p>
                        <p style='color: white; 
                                 font-size: 1.1em;'>
                            <strong style='color: {ACCENT_COLOR}; 
                                       display: block; 
                                       margin-bottom: 5px;'>Famous Art Form:</strong> 
                            {state_data['Popular_Art_Form']}
                        </p>
                    </div>
                    <div style='background-color: {BACKGROUND_COLOR}; 
                               padding: 25px; 
                               border-radius: 10px;
                               border: 1px solid {BORDER_COLOR};'>
                        <h3 style='color: {THEME_COLOR}; 
                                 margin-bottom: 20px; 
                                 font-size: 1.8em; 
                                 font-weight: 600;'>Popular Attractions</h3>
                        <p style='color: white; 
                                 font-size: 1.1em; 
                                 line-height: 1.6;'>{state_data['Popular_Attractions']}</p>
                    </div>
                </div>
                <div style='background-color: {BACKGROUND_COLOR}; 
                           padding: 25px; 
                           border-radius: 10px; 
                           margin-top: 20px;
                           border: 1px solid {BORDER_COLOR};'>
                    <h3 style='color: {THEME_COLOR}; 
                             margin-bottom: 20px; 
                             font-size: 1.8em; 
                             font-weight: 600;'>Hidden Gems</h3>
                    <p style='color: white; 
                             font-size: 1.1em; 
                             line-height: 1.6;'>{state_data['Hidden_Gems']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Error displaying state information: {str(e)}")

def get_region_states(region):
    """Get list of states in a specific region"""
    return REGIONS.get(region, []) 