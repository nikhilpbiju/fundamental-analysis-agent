import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from data import get_stock_data, normalize_ticker
from rag import load_and_index
from analysis import analyze
from news import get_news

st.title("📊 AI Stock Analyst Agent")

user_input = st.text_input("Enter Stock (e.g. TCS or STOVEKRAFT.NS)")
pdf = st.file_uploader("Upload Annual Report (optional)", type="pdf")
question = st.text_input("Ask anything about the stock")

if st.button("Ask"):

    if not user_input or not question:
        st.warning("Enter stock and question")
    else:
        ticker = normalize_ticker(user_input)

        st.subheader("📊 Fetching Data...")
        data = get_stock_data(ticker)

        company_name = data.get("Company Name", ticker)

        st.subheader("📰 Fetching News...")
        news = get_news(company_name)

        context = ""

        if pdf:
            st.subheader("📄 Processing PDF...")
            with open("temp.pdf", "wb") as f:
                f.write(pdf.read())

            db = load_and_index("temp.pdf")
            docs = db.similarity_search(question)
            context = " ".join([doc.page_content for doc in docs])

        st.subheader("🧠 AI Response")
        result = analyze(data, context, news, question)

        st.write(result)