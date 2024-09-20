# src/reddit_api_handler.py

import praw

class RedditClient:
    def __init__(self, client_id=None, client_secret=None, user_agent=None):
        """Initializes the Reddit client with provided credentials or defaults to praw.ini."""
        if client_id and client_secret and user_agent:
            # Use provided credentials
            self.reddit = praw.Reddit(
                client_id=client_id,
                client_secret=client_secret,
                user_agent=user_agent
            )
        else:
            # Fallback to praw.ini configuration
            self.reddit = praw.Reddit()  # This will look for credentials in praw.ini

    def fetch_posts(self, subreddit, limit=10):
        """Fetch trending posts from a given subreddit."""
        posts = []
        upvotes = []
        try:
            subreddit_instance = self.reddit.subreddit(subreddit)
            for submission in subreddit_instance.hot(limit=limit):
                posts.append(submission.title)
                upvotes.append(submission.score)
            return posts, upvotes
        except Exception as e:
            raise ValueError(f"Failed to fetch posts: {e}")
    def fetch_trending_topics(self, limit=10):
        """Fetch trending subreddits or posts on Reddit."""
        trending_topics = []
        try:
            # Using Reddit's popular subreddits feature
            for submission in self.reddit.subreddit("all").hot(limit=limit):
                trending_topics.append({
                    'title': submission.title,
                    'subreddit': submission.subreddit.display_name,
                    'score': submission.score,
                    'url': submission.url
                })
            return trending_topics
        except Exception as e:
            raise ValueError(f"Failed to fetch trending topics: {e}")
            return []