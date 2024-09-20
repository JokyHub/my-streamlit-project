# sentiment_analyzer.py

from textblob import TextBlob

class SentimentAnalyzer:
    def analyze_sentiment(self, text):
        """Analyze the sentiment of the provided text."""
        blob = TextBlob(text)
        return blob.sentiment.polarity
