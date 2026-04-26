# Q8: Real-time Data Pipeline
# Task: Scrape data -> clean with pandas -> store in SQLite -> visualize on dashboard
# Tools: BeautifulSoup, pandas, SQLite, Plotly Dash
# Install: pip install requests beautifulsoup4 pandas plotly dash
# Dash Docs: https://dash.plotly.com/

import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from datetime import datetime
import dash
from dash import dcc, html
import plotly.express as px

DB = "pipeline.db"

def scrape_data():
    url = "https://news.ycombinator.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    stories = []
    for item in soup.select(".athing")[:20]:
        title_tag = item.select_one(".titleline a")
        score_tag = item.find_next_sibling("tr").select_one(".score")
        if title_tag:
            stories.append({
                "title": title_tag.text.strip()[:80],
                "score": int(score_tag.text.replace(" points", "")) if score_tag else 0,
                "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
    return stories

def clean_and_store(stories):
    df = pd.DataFrame(stories)
    df.drop_duplicates(subset=["title"], inplace=True)
    df = df[df["score"] > 0]
    df.sort_values("score", ascending=False, inplace=True)

    conn = sqlite3.connect(DB)
    df.to_sql("stories", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Stored {len(df)} stories in database")
    return df

def load_from_db():
    conn = sqlite3.connect(DB)
    df = pd.read_sql("SELECT * FROM stories ORDER BY score DESC", conn)
    conn.close()
    return df

# Run pipeline
print("Running pipeline...")
stories = scrape_data()
df = clean_and_store(stories)

# Dashboard
app = dash.Dash(__name__)
df = load_from_db()

app.layout = html.Div([
    html.H1("Hacker News Dashboard", style={"textAlign": "center"}),
    dcc.Graph(
        figure=px.bar(
            df.head(10), x="score", y="title",
            orientation="h", title="Top 10 Stories by Score",
            color="score", color_continuous_scale="blues"
        )
    )
])

if __name__ == "__main__":
    print("Dashboard running at http://127.0.0.1:8050")
    app.run(debug=True)