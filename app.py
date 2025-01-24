import streamlit as st
from utils import fetch_fmp_data, fetch_stock_data, plot_stock_chart

# Streamlit app
def main():
    st.title("Fundamental Stock Analysis Dashboard")

    # Input for stock ticker
    ticker = st.text_input("Enter Stock Ticker (e.g., AAPL):").upper()

    if ticker:
        api_key = "j6kCIBjZa1pHewFjf7XaRDlslDxEFuof"  # Replace with your actual FMP API key

        # Fetch company profile
        profile = fetch_fmp_data("profile", ticker, api_key)
        stock_data = fetch_stock_data(ticker, api_key)

        if profile:
            col1, col2 = st.columns([1, 2])

            with col1:
                # Display stock chart
                if stock_data:
                    st.plotly_chart(plot_stock_chart(stock_data))

            with col2:
                # Display company description
                st.subheader(f"{profile[0]['companyName']} ({ticker})")
                st.write(f"**Industry:** {profile[0]['industry']}")
                st.write(f"**Sector:** {profile[0]['sector']}")
                st.write(profile[0]['description'][:500] + "...")  # Limit description length

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
            st.write(f"**P/E Ratio:** {round(latest_ratios['priceEarningsRatio'], 2)}")
            st.write(f"**P/B Ratio:** {round(latest_ratios['priceToBookRatio'], 2)}")
            st.write(f"**Debt-to-Equity Ratio:** {round(latest_ratios['debtEquityRatio'], 2)}")
            st.write(f"**Return on Equity (ROE):** {round(latest_ratios['returnOnEquity'], 2)}%")
            st.write(f"**Dividend Yield:** {round(latest_ratios['dividendYield'], 2)}%")

if __name__ == "__main__":
    main()

