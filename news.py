import os
import requests

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_news(company_name):
    query = f"{company_name} stock India"

    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"

    response = requests.get(url).json()
    articles = response.get("articles", [])[:5]

    news_text = ""
    for article in articles:
        title = article.get("title", "")
        desc = article.get("description", "")
        news_text += f"{title} - {desc}\n"

    return news_text