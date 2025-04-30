import praw
import json
from datetime import datetime

# Reddit API credentials
reddit = praw.Reddit(client_id='YOUR_ID',
                     client_secret='YOUR_SECRET',
                     user_agent='YOUR_AGENT')

# Keywords (from the list of 30+)
keywords = [
    "Jordan", "Jordans", "Air Jordan", "AJ1", "AJ4", "AJ5", "Air Jordan 1", "Air Jordan 4",
    "Nike Jordan", "Jordan Brand", "Jordan release", "Jordan drop", "Jordan restock", "Jordan collab",
    "Jordan launch", "Retro Jordan", "Jordan sneakers", "Jordan shoes", "Jordan colorway", "Jordan SE",
    "Sneakerhead", "Grail sneakers", "Hype sneakers", "Sneaker drop", "Sneaker resale", "Jordan resale",
    "Copped Jordans", "Missed drop", "Jordan SNKRS", "Jordan heat", "Drip check", "On feet Jordans",
    "W or L", "Jordan flex", "Kicks of the day"
]

# Function to fetch Reddit data
def fetch_reddit_data():
    mentions = []
    
    for keyword in keywords:
        # Search Reddit with each keyword in top posts for the past 3-4 months
        for submission in reddit.subreddit('all').search(keyword, sort='new', time_filter='month'):
            mention = {
                'source': 'Reddit',
                'date': datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d'),
                'text': submission.title + " " + submission.selftext,
                'link': f"https://www.reddit.com{submission.permalink}",
                'keyword': keyword
            }
            mentions.append(mention)
    
    return mentions

# Save data to JSON file
def save_data_to_json(data, filename='reddit_data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Fetch and save Reddit data
reddit_data = fetch_reddit_data()
save_data_to_json(reddit_data)
