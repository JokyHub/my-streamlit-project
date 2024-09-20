# app.py

import streamlit as st
from src.reddit_api_handler import RedditClient
from src.sentiment_analyzer import SentimentAnalyzer
from src.visualization import Visualizer
import matplotlib.pyplot as plt  
# Initialize sentiment analyzer and visualizer
analyzer = SentimentAnalyzer()
visualizer = Visualizer()

# App layout
st.title("Reddit Sentiment Analysis Dashboard")
st.write("Welcome to the Sentiment Analysis Dashboard. This app fetches posts from Reddit and analyzes their sentiments.")

# Input fields for Reddit API credentials
client_id = st.text_input("Enter your Reddit Client ID:", type="password")
client_secret = st.text_input("Enter your Reddit Client Secret:", type="password")
user_agent = st.text_input("Enter your Reddit User Agent:")

# Input field for the subreddit and search query
subreddit = st.text_input("Enter the subreddit (e.g., 'Python'):")
query = st.text_input("Enter a search query for posts:")

# Input field for the number of posts to fetch
limit = st.number_input("Number of posts to fetch:", min_value=1, max_value=100, value=10)

# Fetch and analyze Reddit posts on button click
if st.button("Fetch Posts and Analyze"):
    try:
        # Initialize Reddit client with provided or environment credentials
        reddit_client = RedditClient(client_id, client_secret, user_agent)
        posts, upvotes = reddit_client.fetch_posts(subreddit, limit)

        if posts:
            st.write("Fetched Reddit Posts:")
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
            st.write("No posts found or unable to fetch data.")
    except ValueError as e:
        st.error(e)
