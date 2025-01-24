import streamlit as st
import requests

# Function to fetch data from FMP API
def fetch_fmp_data(endpoint, symbol, api_key):
    url = f"https://financialmodelingprep.com/api/v3/{endpoint}/{symbol}?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching data from FMP API.")
        return None

# Streamlit app
def main():
    st.title("Fundamental Stock Analysis Dashboard")

    # Input for stock ticker
    ticker = st.text_input("Enter Stock Ticker (e.g., AAPL):").upper()

    if ticker:
        api_key = "j6kCIBjZa1pHewFjf7XaRDlslDxEFuof"  # Replace with your actual FMP API key

        # Fetch company profile
        profile = fetch_fmp_data("profile", ticker, api_key)
        if profile:
            st.header(f"{profile[0]['companyName']} ({ticker})")
            st.write(f"**Industry:** {profile[0]['industry']}")
            st.write(f"**Sector:** {profile[0]['sector']}")
            st.write(f"**Description:** {profile[0]['description']}")

        # Fetch DCF valuation
        dcf = fetch_fmp_data("discounted-cash-flow", ticker, api_key)
        if dcf:
            st.subheader("Discounted Cash Flow (DCF) Valuation")
            st.write(f"**DCF Value:** ${dcf[0]['dcf']}")
            st.write(f"**Stock Price:** ${dcf[0]['Stock Price']}")
            valuation = "undervalued" if dcf[0]['dcf'] > dcf[0]['Stock Price'] else "overvalued"
            st.write(f"The stock appears to be **{valuation}** based on DCF analysis.")

        # Fetch financial ratios
        ratios = fetch_fmp_data("ratios", ticker, api_key)
        if ratios:
            st.subheader("Key Financial Ratios")
            latest_ratios = ratios[0]
            st.write(f"**P/E Ratio:** {latest_ratios['priceEarningsRatio']}")
            st.write(f"**P/B Ratio:** {latest_ratios['priceToBookRatio']}")
            st.write(f"**Debt-to-Equity Ratio:** {latest_ratios['debtEquityRatio']}")
            st.write(f"**Return on Equity (ROE):** {latest_ratios['returnOnEquity']}%")
            st.write(f"**Dividend Yield:** {latest_ratios['dividendYield']}%")

if __name__ == "__main__":
    main()
