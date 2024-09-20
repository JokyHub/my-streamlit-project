# visualizer.py

import matplotlib.pyplot as plt
from wordcloud import WordCloud

class Visualizer:
    def __init__(self):
        pass

    def generate_word_cloud(self, text_data):
        """Generate and display a word cloud from the given text data."""
        text = ' '.join(text_data)
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Word Cloud of Fetched Posts')
        plt.show()

    def plot_upvote_distribution(self, upvotes):
        """Plot the distribution of upvotes."""
        plt.figure(figsize=(10, 5))
        plt.hist(upvotes, bins=20, color='skyblue', edgecolor='black')
        plt.title("Upvote Distribution")
        plt.xlabel("Upvotes")
        plt.ylabel("Frequency")
        plt.show()
