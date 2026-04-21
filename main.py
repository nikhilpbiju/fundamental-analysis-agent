from data import get_stock_data
from rag import load_and_index
from analysis import analyze

# Step 1: Input
ticker = input("Enter stock ticker (e.g. TCS.NS): ")
pdf_path = "report.pdf"  # keep a sample annual report

# Step 2: Get financial data
data = get_stock_data(ticker)

# Step 3: Load RAG
db = load_and_index(pdf_path)

# Step 4: Query
query = "What are the risks and growth opportunities?"
docs = db.similarity_search(query)

context = " ".join([doc.page_content for doc in docs])

# Step 5: Analyze
result = analyze(data, context)

print(result)