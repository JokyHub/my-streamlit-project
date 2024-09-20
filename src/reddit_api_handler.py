# reddit_client.py

import praw
import os
from dotenv import load_dotenv

class RedditClient:
    def __init__(self, client_id=None, client_secret=None, user_agent=None):
        # Load environment variables
        load_dotenv()

        # Set credentials from environment or use provided parameters
        self.client_id = client_id or os.getenv("REDDIT_CLIENT_ID")
        self.client_secret = client_secret or os.getenv("REDDIT_CLIENT_SECRET")
        self.user_agent = user_agent or os.getenv("REDDIT_USER_AGENT")

        # Check if credentials are set properly
        if not self.client_id or not self.client_secret or not self.user_agent:
            raise ValueError("Reddit credentials are missing. Please set them in the .env file or provide them explicitly.")

        # Initialize the Reddit API connection
        self.reddit = self._authenticate()

    def _authenticate(self):
        """Authenticate and return the Reddit instance."""
        try:
            return praw.Reddit(
                client_id=self.client_id,
                client_secret=self.client_secret,
                user_agent=self.user_agent
            )
        except Exception as e:
            raise ValueError(f"Failed to authenticate with Reddit API: {e}")

    def fetch_posts(self, subreddit, limit=10):
        """Fetch trending posts from Reddit."""
        posts = []
        upvotes = []
        try:
            subreddit_instance = self.reddit.subreddit(subreddit)

            # Fetch trending posts (hot posts)
            for submission in subreddit_instance.hot(limit=limit):
                posts.append(submission.title)
                upvotes.append(submission.ups)

            return posts, upvotes
        except Exception as e:
            raise ValueError(f"Error fetching data from Reddit API: {e}")