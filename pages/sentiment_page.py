# app.py

import streamlit as st
from src.reddit_api_handler import RedditClient
from src.sentiment_analyzer import SentimentAnalyzer
from src.visualization import Visualizer
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
import time

# Initialize sentiment analyzer and visualizer
analyzer = SentimentAnalyzer()
visualizer = Visualizer()

def sentiment_analysis_page():
    """Function to analyse the sentiment of the Reddit posts"""
    # Load environment variables (Optional: if you still want to use .env as a fallback)
    load_dotenv()
    # Set up the checkbox to use default credentials
    use_default_credentials = st.checkbox("Use default credentials from praw.ini")

    # App layout
    st.title("Reddit 🔍 Sentiment Analysis Dashboard")
    st.write("This app fetches posts from Reddit and analyzes their sentiments.")
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

    # Section to Analyze Posts
    st.subheader("Analyze Reddit Posts")
    # Fetch and analyze Reddit posts on button click
    if st.button("🔍 Fetch Posts and Analyze"):
        with st.spinner("Fetching data, please wait..."):
            time.sleep(2)
        # Check if credentials are provided correctly based on the checkbox state
        if use_default_credentials or (client_id and client_secret and user_agent):
            try:
                # Initialize Reddit client, passing credentials if not using the default
                if use_default_credentials:
                    reddit_client = RedditClient()  # Use default credentials from praw.ini
                else:
                    reddit_client = RedditClient(client_id, client_secret, user_agent)  # Use provided credentials

                # Fetch posts
                posts, upvotes = reddit_client.fetch_posts(subreddit, limit)

                if posts:
                    st.success("Posts récupérés avec succès!")
                    sentiments = []
                    for post in posts:
                        st.write(f"- {post}")
                        sentiment_score = analyzer.analyze_sentiment(post)
                        st.write(f"Sentiment Score: {sentiment_score}")
                        sentiments.append(sentiment_score)

                    # Plot sentiment distribution
                    st.write("Sentiment Distribution:")
                    plt.hist(sentiments, bins=20, color='skyblue', edgecolor='black')
                    plt.title("Sentiment Score Distribution")
                    plt.xlabel("Sentiment Score")
                    plt.ylabel("Frequency")
                    st.pyplot()

                    # Generate and display the word cloud
                    st.write("Word Cloud:")
                    visualizer.generate_word_cloud(posts)
                    st.pyplot()

                    # Plot upvote distribution
                    st.write("Upvote Distribution:")
                    visualizer.plot_upvote_distribution(upvotes)
                    st.pyplot()

                else:
                    st.error("No posts found or unable to fetch data.")
            except ValueError as e:
                st.error(e)