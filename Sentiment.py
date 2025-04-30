import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the Reddit data
with open('reddit_data.json', 'r') as file:
    reddit_data = json.load(file)

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(text):
    sentiment = analyzer.polarity_scores(text)
    return sentiment

# Add sentiment analysis to each mention
for mention in reddit_data:
    sentiment = analyze_sentiment(mention['text'])
    mention['sentiment'] = sentiment

# Save data with sentiment analysis to new JSON file
with open('reddit_data_with_sentiment.json', 'w') as output_file:
    json.dump(reddit_data, output_file, indent=4)

print("Sentiment analysis added to data and saved in 'reddit_data_with_sentiment.json'")
