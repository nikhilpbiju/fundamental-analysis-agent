import yfinance as yf

COMPANY_TO_TICKER = {
    "stovekraft": "STOVEKRAFT.NS",
    "tcs": "TCS.NS",
    "reliance": "RELIANCE.NS",
    "infosys": "INFY.NS",
}

def normalize_ticker(user_input):
    user_input = user_input.lower().strip()

    if user_input in COMPANY_TO_TICKER:
        return COMPANY_TO_TICKER[user_input]

    return user_input.upper()

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    data = {
        "Company Name": info.get("longName"),
        "Sector": info.get("sector"),
        "Industry": info.get("industry"),
        "Business Summary": info.get("longBusinessSummary"),

        "Revenue": info.get("totalRevenue"),
        "Net Income": info.get("netIncomeToCommon"),
        "ROE": info.get("returnOnEquity"),
        "Debt/Equity": info.get("debtToEquity"),
        "P/E": info.get("trailingPE"),

        "Market Cap": info.get("marketCap"),
        "Current Price": info.get("currentPrice"),
    }

    return data