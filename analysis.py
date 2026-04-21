import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze(data, context, news, question):

    prompt = f"""
You are a professional stock analyst.

User Question:
{question}

Company Data:
{data}

Latest News:
{news}

Report Context:
{context}

Instructions:
- Answer clearly and directly
- Use financials + news
- Identify sentiment (positive/negative)
- Mention risks & opportunities
- Give a confident conclusion
"""

    response = model.generate_content(prompt)
    return response.text