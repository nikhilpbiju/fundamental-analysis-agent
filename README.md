# 📊 AI Fundamental Analysis Agent

An AI-powered stock analysis tool that combines **financial data, real-time news, and AI reasoning** to provide intelligent investment insights.

---

## 🚀 Features

* 💬 **Conversational Queries**

  * Ask anything like:

    * *“Is TCS a good investment?”*
    * *“Why is Reliance trending?”*

* 📊 **Financial Analysis**

  * Pulls real company data using Yahoo Finance

* 📰 **Real-Time News Integration**

  * Analyzes latest news and sentiment

* 📄 **Optional Annual Report Analysis (RAG)**

  * Upload PDFs for deeper insights

* 🧠 **AI-Powered Reasoning**

  * Uses Gemini to generate structured analysis

---

## 🧠 How It Works

1. User inputs stock + question
2. System fetches:

   * Financial data (yfinance)
   * Latest news (NewsAPI)
   * Optional PDF context (RAG)
3. Gemini combines all inputs
4. Generates a clear, analytical response

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python
* **LLM**: Gemini API
* **Data Source**: yfinance
* **News**: NewsAPI
* **RAG**: FAISS + HuggingFace embeddings

---

## 📁 Project Structure

```
ai-stock-analyst/
│
├── app.py
├── data.py
├── analysis.py
├── news.py
├── rag.py
├── requirements.txt
├── .env.example
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/ai-stock-analyst-agent.git
cd ai-stock-analyst-agent
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Create `.env` file

```
GEMINI_API_KEY=your_key_here
NEWS_API_KEY=your_key_here
```

---

### 4. Run the app

```
streamlit run app.py
```

---

## 💡 Example Queries

* *“Is INFY a good long-term investment?”*
* *“What are the risks for STOVEKRAFT?”*
* *“Why is this stock moving recently?”*

---

## ⚠️ Disclaimer

This tool is for **educational purposes only** and does not constitute financial advice.

---

## 📌 Future Improvements

* 📈 Stock price charts
* 🧠 Sentiment scoring (ML integration)
* 🆚 Company comparison
* 🌐 Deployment (public web app)

---

## 👨‍💻 Author

Built by Nikhil

---

## ⭐ If you like this project

Give it a star on GitHub!
