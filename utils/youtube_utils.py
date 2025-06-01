from googleapiclient.discovery import build
import streamlit as st
from .config import YOUTUBE_API_KEY

def get_youtube_service():
    """Initialize YouTube API service"""
    if not YOUTUBE_API_KEY:
        st.error("Please set your YouTube API key in the .env file")
        return None
    
    try:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        return youtube
    except Exception as e:
        st.error(f"Error initializing YouTube API: {str(e)}")
        return None

def search_youtube_shorts(youtube, query, max_results=5):
    """Search for YouTube Shorts related to a destination"""
    if not youtube:
        return []
    
    try:
        # Search for shorts with location-specific keywords
        search_query = f"{query} india travel shorts"
        
        # Execute search request
        request = youtube.search().list(
            part="snippet",
            q=search_query,
            type="video",
            videoDuration="short",
            maxResults=max_results
        )
        response = request.execute()
        
        # Extract video information
        videos = []
        for item in response.get('items', []):
            video_id = item['id']['videoId']
            title = item['snippet']['title']
            thumbnail = item['snippet']['thumbnails']['high']['url']
            
            videos.append({
                'id': video_id,
                'title': title,
                'thumbnail': thumbnail,
                'url': f"https://www.youtube.com/shorts/{video_id}"
            })
        
        return videos
    except Exception as e:
        st.error(f"Error searching YouTube: {str(e)}")
        return []

def display_youtube_shorts(videos):
    """Display YouTube Shorts in the Streamlit app"""
    if not videos:
        st.info("No relevant YouTube Shorts found.")
        return
    
    # Display videos in a grid
    cols = st.columns(min(len(videos), 3))
    for idx, video in enumerate(videos):
        with cols[idx % 3]:
            st.image(video['thumbnail'], 
                    caption=video['title'][:50] + "..." if len(video['title']) > 50 else video['title'])
            st.markdown(f"[Watch on YouTube]({video['url']})")

def get_trending_shorts(youtube, region_code='IN', max_results=5):
    """Get trending travel-related YouTube Shorts in India"""
    if not youtube:
        return []
    
    try:
        # Search for trending travel shorts
        request = youtube.search().list(
            part="snippet",
            q="india travel culture tourism",
            type="video",
            videoDuration="short",
            maxResults=max_results,
            regionCode=region_code,
            order="viewCount"
        )
        response = request.execute()
        
        # Process videos
        videos = []
        for item in response.get('items', []):
            video_id = item['id']['videoId']
            title = item['snippet']['title']
            thumbnail = item['snippet']['thumbnails']['high']['url']
            
            videos.append({
                'id': video_id,
                'title': title,
                'thumbnail': thumbnail,
                'url': f"https://www.youtube.com/shorts/{video_id}"
            })
        
        return videos
    except Exception as e:
        st.error(f"Error fetching trending shorts: {str(e)}")
        return [] 