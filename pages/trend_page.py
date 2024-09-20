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

def trending_topics_page():
# Load environment variables (Optional: if you still want to use .env as a fallback)
    load_dotenv()
    # Set up the checkbox to use default credentials
    use_default_credentials = st.checkbox("Use default credentials from praw.ini")
    # App layout
    st.title("Reddit Hot 🔥 Topics Dashboard")
    st.write("Welcome to the Trend fetching Dashboard. This Page will allow you to retrieve the latest trending post on reddit.")
    # Input fields for Reddit API credentials only if not using the default ones
    if not use_default_credentials:
        client_id = st.text_input("Enter your Reddit Client ID:", type="password")
        client_secret = st.text_input("Enter your Reddit Client Secret:", type="password")
        user_agent = st.text_input("Enter your Reddit User Agent:")
    else:
        client_id = client_secret = user_agent = None  # No need for manual input if using praw.ini

    # Input field for the subreddit and search query
    subreddit = st.text_input("Enter the subreddit (e.g., 'Python'):", key="subreddit")
    query = st.text_input("Enter a search query for posts:", key="query")

    # Input field for the number of posts to fetch
    limit = st.number_input("Number of posts to fetch:", min_value=1, max_value=100, value=10)
    if st.button("Show Top Trending 🔥Topics Right now"):
        try:
                # Initialize Reddit client, passing credentials if not using the default
                if use_default_credentials:
                    reddit_client = RedditClient()  # Use default credentials from praw.ini
                else:
                    reddit_client = RedditClient(client_id, client_secret, user_agent)  # Use provided credentials

                trending_topics = reddit_client.fetch_trending_topics(limit)
                if trending_topics:
                    for topic in trending_topics:
                        st.write(f"**{topic['title']}** - [{topic['subreddit']}]({topic['url']}) - Upvotes: {topic['score']}")
                else:
                    st.write("No trending topics found.")
        except ValueError as e:
            st.error(e)