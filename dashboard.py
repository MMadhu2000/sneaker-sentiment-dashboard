import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import nltk
import json
from nltk.corpus import stopwords
import numpy as np
import re

nltk.download('stopwords')

# Load and clean data
with open("reddit_data_with_sentiment.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df['compound'] = df['sentiment'].apply(lambda x: x['compound'])
df['neg'] = df['sentiment'].apply(lambda x: x['neg'])
df['neu'] = df['sentiment'].apply(lambda x: x['neu'])
df['pos'] = df['sentiment'].apply(lambda x: x['pos'])

# Sidebar filters
st.sidebar.title("🔍 Filters")
keywords = df['keyword'].unique()
selected_keyword = st.sidebar.selectbox("Select Keyword", keywords)

date_range = st.sidebar.date_input("Select Date Range", [df['date'].min(), df['date'].max()])
filtered = df[(df['keyword'] == selected_keyword) & (df['date'] >= pd.to_datetime(date_range[0])) & (df['date'] <= pd.to_datetime(date_range[1]))]

# Main dashboard
st.title("👟 Reddit Sneaker Sentiment Dashboard")
st.markdown("Powered by VADER | Enhanced by Streamlit")

col1, col2, col3 = st.columns(3)
col1.metric("🔢 Total Posts", len(filtered))
col2.metric("😀 Avg Positive", f"{filtered['pos'].mean():.2f}")
col3.metric("😐 Avg Neutral", f"{filtered['neu'].mean():.2f}")

# Sentiment pie chart
st.subheader("🧠 Sentiment Breakdown")
avg_sentiments = {
    'Positive': filtered['pos'].mean(),
    'Neutral': filtered['neu'].mean(),
    'Negative': filtered['neg'].mean()
}
pie_fig = px.pie(names=avg_sentiments.keys(), values=avg_sentiments.values(), title="Sentiment Proportion")
st.plotly_chart(pie_fig, use_container_width=True)

# Sentiment over time
st.subheader("📈 Compound Sentiment Over Time")
line_fig = px.line(filtered.sort_values('date'), x='date', y='compound', title="Sentiment Trend", markers=True)
st.plotly_chart(line_fig, use_container_width=True)

# Bar chart: average sentiment per keyword
st.subheader("📊 Avg Sentiment per Keyword")
avg_by_keyword = df.groupby('keyword')[['pos', 'neu', 'neg']].mean().reset_index()
bar_fig = px.bar(avg_by_keyword, x='keyword', y=['pos', 'neu', 'neg'], barmode='group')
st.plotly_chart(bar_fig, use_container_width=True)

# Word cloud
st.subheader("☁️ Word Cloud")

# Cleaning text
def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"\b(?:com|html|aspx|itemid|twitter|fangraphs|weidian|players|search|q|tweets|en|last|name|item|iso|obp|ab|ba|bb|hr|k)\b", "", text, flags=re.IGNORECASE)
    return text

text = " ".join([clean_text(t) for t in filtered['text']])

# Custom stopwords
custom_stopwords = set(STOPWORDS)
custom_stopwords.update([
    "https", "http", "www", "com", "reddit", "amp", "imgur", "jpg", "png", "gl", "rl",
    "x", "air", "jordan", "retro", "search", "item", "aspx", "players", "twitter",
    "fangraphs", "weidian", "html", "q", "tweets", "en", "last", "name", "itemid",
    "obp", "ab", "ba", "bb", "hr", "k", "iso"
])

# Generate standard word cloud
wc = WordCloud(
    width=800,
    height=400,
    stopwords=custom_stopwords,
    background_color='white'
).generate(text)

# Display the word cloud
fig, ax = plt.subplots()
ax.imshow(wc, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)

# Top posts
st.subheader("🏆 Top Positive Posts")
top_pos = filtered.sort_values('compound', ascending=False).head(3)
for _, row in top_pos.iterrows():
    with st.expander(f"💬 {row['text'][:80]}..."):
        st.write(row['text'])
        st.markdown(f"[🔗 View Reddit Post]({row['link']})")
        st.success(f"Sentiment Score: {row['compound']}")

st.subheader("🚨 Top Negative Posts")
top_neg = filtered.sort_values('compound', ascending=True).head(3)
for _, row in top_neg.iterrows():
    with st.expander(f"💬 {row['text'][:80]}..."):
        st.write(row['text'])
        st.markdown(f"[🔗 View Reddit Post]({row['link']})")
        st.error(f"Sentiment Score: {row['compound']}")

# Full data table
st.subheader("📋 Full Data Table")
st.dataframe(filtered[['date', 'text', 'compound', 'link']].reset_index(drop=True))
