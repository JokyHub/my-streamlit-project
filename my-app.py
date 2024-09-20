# app.py

#Import Librairies

import streamlit as st
import praw
import pandas as pd
import spacy
from textblob import TextBlob
import matplotlib.pyplot as plt

#Load the spacy model for text processing
nlp = spacy.load("en_core_web_sm")

# Function to analyze sentiment
def analyze_sentiment(text):
    """Analysing tweets using blob and giving them a score"""
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Function to fetch Reddit posts
def fetch_reddit_posts(client_id, client_secret, user_agent, subreddit, query, limit=10):
    # Initialize Reddit API connection
    reddit = praw.Reddit(client_id=client_id, 
                         client_secret=client_secret, 
                         user_agent=user_agent)

    # Fetch posts from the subreddit based on the query
    posts = []
    try:
        subreddit_instance = reddit.subreddit(subreddit)
        for submission in subreddit_instance.search(query, limit=limit):
            posts.append(submission.title)
        return posts
    except Exception as e:
        st.error(f"Error fetching data from Reddit API: {e}")
        return []
#App layout

st.title("Reddit Sentiment Analysis Dashboard")
st.write("Welcome to the Sentiment Analysis Dashboard. This app fetchs posts from Reddit and analyze their sentiments.")

# Input fields for Reddit API credentials
client_id = st.text_input("Enter your Reddit Client ID:", type="password")
client_secret = st.text_input("Enter your Reddit Client Secret:", type="password")
user_agent = st.text_input("Enter your Reddit User Agent:")
# Input field for the subreddit and search query
subreddit = st.text_input("Enter the subreddit (e.g., 'Python'):")
query = st.text_input("Enter a search query for posts:")

# Input field for the number of posts to fetch
limit = st.number_input("Number of posts to fetch:", min_value=1, max_value=100, value=10)

if st.button("Fetch Posts and Analyze"):
    if client_id and client_secret and user_agent and subreddit and query:
        posts = fetch_reddit_posts(client_id, client_secret, user_agent, subreddit, query, limit)
        if posts:
            st.write("Fetched Reddit Posts:")
            sentiments = []
            for post in posts:
                st.write(f"- {post}")
                sentiment_score = analyze_sentiment(post)
                st.write(f"Sentiment Score: {sentiment_score}")
                sentiments.append(sentiment_score)
            
            # Plot sentiment distribution
            st.write("Sentiment Distribution:")
            plt.hist(sentiments, bins=20, color='skyblue', edgecolor='black')
            plt.title("Sentiment Score Distribution")
            plt.xlabel("Sentiment Score")
            plt.ylabel("Frequency")
            st.pyplot()
        else:
            st.write("No posts found or unable to fetch data.")
    else:
        st.write("Please enter all required Reddit API credentials and subreddit details.")