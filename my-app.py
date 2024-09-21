# app.py

import streamlit as st
from src.reddit_api_handler import RedditClient
from src.sentiment_analyzer import SentimentAnalyzer
from src.visualization import Visualizer
import matplotlib.pyplot as plt
import os
import plotly.express as px
import plotly.graph_objects as go
from dotenv import load_dotenv
from pages.sentiment_page import sentiment_analysis_page  
from pages.trend_page import trending_topics_page 
load_dotenv()
# Load custom CSS file
def load_css():
    """Loading the style.css file defined."""
    with open("src/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Call this function at the beginning of your app
load_css()

st.markdown(
    """
    <style>
    /* Example of some global styling to improve UI */
    .stButton>button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar for navigation
st.sidebar.title("Navigation")
# Selection box to navigate between the pages
page = st.sidebar.selectbox(
    "Choose a Page", 
    ["Sentiment Analysis", "Trending Topics"]  # Add more pages here as needed
)

# Load and render the selected page
if page == "Sentiment Analysis":
    sentiment_analysis_page()  # Call the function that renders the Sentiment Analysis page
    st.markdown("""
        <style>
        body {background-color: #333; color: #FFF;}
        .stButton>button {background-color: #555; color: #FFF;}
        </style>
    """, unsafe_allow_html=True)
elif page == "Trending Topics":
    trending_topics_page()      # Call the function that renders the Trending Topics page
    st.markdown("""
        <style>
        body {background-color: #FFF; color: #000;}
        .stButton>button {background-color: #4CAF50; color: #FFF;}
        </style>
    """, unsafe_allow_html=True)


# Optional: You can include any common footer or disclaimers here if needed
st.sidebar.markdown("---")
st.sidebar.write("© 2024 Reddit Posts Analysis V1 - All rights reserved.")