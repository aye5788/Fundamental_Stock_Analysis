import streamlit as st
from utils import (
    fetch_fmp_data,
    fetch_stock_data,
    plot_candlestick_chart,
    fetch_sector_pe,
    fetch_industry_pe,
)

# Streamlit app
def main():
    st.title("Fundamental Stock Analysis Dashboard")

    # Input for stock ticker
    ticker = st.text_input("Enter Stock Ticker (e.g., AAPL):").upper()

    if ticker:
        api_key = "j6kCIBjZa1pHewFjf7XaRDlslDxEFuof"  # Replace with your actual FMP API key

        # Allow user to select timeframe
        timeframe = st.selectbox("Select Timeframe", ["Last 7 Days", "Last 30 Days", "Last 90 Days"])
        stock_data = None
        if timeframe == "Last 7 Days":
            stock_data = fetch_stock_data(ticker, api_key, days=7)
        elif timeframe == "Last 30 Days":
            stock_data = fetch_stock_data(ticker, api_key, days=30)
        elif timeframe == "Last 90 Days":
            stock_data = fetch_stock_data(ticker, api_key, days=90)

        # Fetch company profile
        profile = fetch_fmp_data("profile", ticker, api_key)

        # Side-by-side layout for chart and description
        col1, col2 = st.columns([2, 1])  # Adjust the ratio for better alignment

        with col1:
            # Display candlestick chart
            if stock_data:
                st.plotly_chart(plot_candlestick_chart(stock_data, timeframe), use_container_width=True)

        with col2:
            if profile:
                # Display company description
                st.subheader(f"{profile[0]['companyName']} ({ticker})")
                st.write(f"**Industry:** {profile[0]['industry']}")
                st.write(f"**Sector:** {profile[0]['sector']}")
                st.write(profile[0]['description'][:500] + "...")  # Limit description length

        # Fetch DCF valuation and financial ratios
        dcf = fetch_fmp_data("discounted-cash-flow", ticker, api_key)
        ratios = fetch_fmp_data("ratios", ticker, api_key)
        sector_pe = fetch_sector_pe(api_key)
        industry_pe = fetch_industry_pe(profile[0]['industry'], api_key)

        if dcf or ratios:
            st.subheader("Valuation and Key Ratios")
            col1, col2 = st.columns(2)

            with col1:
                if dcf:
                    st.write("### Discounted Cash Flow (DCF) Valuation")
                    st.write(f"**DCF Value:** ${dcf[0]['dcf']}")
                    st.write(f"**Stock Price:** ${dcf[0]['Stock Price']}")
                    valuation = "undervalued" if dcf[0]['dcf'] > dcf[0]['Stock Price'] else "overvalued"
                    st.write(f"The stock appears to be **{valuation}** based on DCF analysis.")

            with col2:
                if ratios:
                    st.write("### Key Financial Ratios")
                    latest_ratios = ratios[0]
                    st.write(f"**P/E Ratio:** {round(latest_ratios['priceEarningsRatio'], 2)}")
                    st.write(f"**P/B Ratio:** {round(latest_ratios['priceToBookRatio'], 2)}")
                    st.write(f"**Debt-to-Equity Ratio:** {round(latest_ratios['debtEquityRatio'], 2)}")
                    st.write(f"**Return on Equity (ROE):** {round(latest_ratios['returnOnEquity'], 2)}%")
                    st.write(f"**Dividend Yield:** {round(latest_ratios['dividendYield'], 2)}%")

            if sector_pe or industry_pe:
                st.subheader("Relative Valuation")
                st.write(f"**Sector P/E Ratio:** {sector_pe}")
                st.write(f"**Industry P/E Ratio:** {industry_pe}")
                stock_pe = latest_ratios['priceEarningsRatio']
                st.write(
                    f"The stock's P/E ratio ({round(stock_pe, 2)}) is compared to the sector and industry:"
                )
                if stock_pe < sector_pe:
                    st.write("- **Below sector average**")
                else:
                    st.write("- **Above sector average**")

                if stock_pe < industry_pe:
                    st.write("- **Below industry average**")
                else:
                    st.write("- **Above industry average**")


if __name__ == "__main__":
    main()
