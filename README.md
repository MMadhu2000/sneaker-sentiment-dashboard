# 👟 Reddit Sneaker Sentiment Dashboard

🎯 **What are sneakerheads saying on Reddit?**  
This interactive dashboard dives into sneaker subreddits and visualizes what the community feels about popular drops like **Air Jordans**, **Yeezys**, and more — using sentiment analysis powered by **VADER**.

---

## 🌟 Features at a Glance

✨ **Keyword & Date Filters**  
🎯 Narrow the analysis by keywords like “Jordan”, “Yeezy”, “Off-White”, or by specific dates.

📊 **Sentiment Pie Chart**  
See how the Reddit crowd feels — Positive 🔥, Neutral 😐, or Negative 😤.

📈 **Sentiment Timeline**  
Watch the hype (or hate) rise and fall over time.

🧠 **Word Cloud Generator**  
Highlight popular words and topics in the sneaker conversation.

🏆 **Top Posts by Sentiment**  
Instantly surface the most 🔥 or 😡 posts with direct Reddit links.

📋 **Raw Data Viewer**  
See every Reddit post and its analyzed sentiment in a sleek table.

---

## 🖼️ Preview
![image](https://github.com/user-attachments/assets/25283fc9-a91d-43cf-9bd0-2702a5d48150)

![image](https://github.com/user-attachments/assets/cc852b2a-46b9-4006-9793-0756b0edc9ae)

![image](https://github.com/user-attachments/assets/b49f4966-789a-47fb-922b-10c1e983f7fb)

![image](https://github.com/user-attachments/assets/04f8186a-ca9e-4259-80a6-94fb8d04a2d1)

![image](https://github.com/user-attachments/assets/f8080a09-ba9e-4009-a6a6-f9f985b558e4)

![image](https://github.com/user-attachments/assets/c11c2473-f261-419a-8ea1-de668f32f20f)

![image](https://github.com/user-attachments/assets/afa79d2d-c152-439f-b1af-21b4dc4d73a9)


---

## 🚀 How to Use

### 1. Clone the Repository

git clone https://github.com/yourusername/sneaker-sentiment-dashboard.git
cd sneaker-sentiment-dashboard

2. Install Dependencies
pip install -r requirements.txt

3. Run the App
streamlit run enhanced_dashboard.py

📁 Folder Structure.

├── enhanced_dashboard.py              # Main dashboard app

├── reddit_data_with_sentiment.json   # Sentiment-annotated Reddit data

├── requirements.txt                  # Python dependencies

└── README.md                         # You're here!

🧪 Sample Data Format

{
  "source": "Reddit",
  "date": "2025-04-30",
  "text": "QC Union LA x Air Jordan 4 Retro Off Noir from Timsneakers GL or RL?",
  "link": "https://www.reddit.com/...",
  "keyword": "Jordan",
  "sentiment": {
    "neg": 0.0,
    "neu": 0.822,
    "pos": 0.178,
    "compound": 0.4648
  }
}
💡 Cool Ideas to Expand This
🔁 Live Reddit scraping using PRAW or Pushshift

🧠 NER or topic modeling on sneaker topics

📱 Mobile-friendly UI

📥 Downloadable sentiment reports

📸 Instagram-style post viewer

❤️ Built With
Streamlit – UI framework

NLTK VADER – Sentiment analysis

Pandas – Data wrangling

Matplotlib & Plotly – Charts

WordCloud – Text cloud visualization

🙌 Stay Fly
If you love kicks, data, and code — this is your playground.
Feel free to fork, remix, or expand. Open to collaborations!

“Real or Rep, the hype is real.”
