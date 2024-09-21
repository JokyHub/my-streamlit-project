# **Project Name: Reddit Sentiment Analysis Dashboard**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen)](https://www.python.org/downloads/)

## **Table of Contents**

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Configuration](#configuration)
7. [Project Structure](#project-structure)
8. [Screenshots](#screenshots)
9. [Contributing](#contributing)
10. [License](#license)
11. [Contact](#contact)

## **Project Overview**

The **Reddit Sentiment Analysis Dashboard** is a streamlit web application that fetches Reddit posts and analyzes their sentiments using advanced NLP techniques. The app provides insights into trending topics, visualizes sentiment distributions, and highlights key themes through word clouds. It's designed for data enthusiasts, researchers, and marketers who want to analyze Reddit content interactively.

## **Features**

- **Fetch Reddit Posts**: Retrieve posts based on subreddit and query.
- **Sentiment Analysis**: Analyze sentiment scores of posts using TextBlob and visualize the results.
- **Trending Topics**: View the latest trending topics in a selected subreddit.
- **Word Cloud Generation**: Visualize the most frequent words in fetched posts.
- **Upvote Analysis**: Analyze the distribution of upvotes for the fetched posts.
- **Multi-page Layout**: Separate sections for sentiment analysis and trending topics.

## **Tech Stack**

- **Frontend**: Streamlit
- **Backend**: Python
- **APIs**: Reddit API (PRAW)
- **Libraries**: Spacy, TextBlob, Matplotlib, Pandas, WordCloud, dotenv

## **Installation**

### **Prerequisites**

- Python 3.8+
- Git
- Docker (Optional, for containerization)

### **Clone the Repository**

```bash
git clone https://github.com/JokyHub/my-streamlit-project.git
cd my-streamlit-project
