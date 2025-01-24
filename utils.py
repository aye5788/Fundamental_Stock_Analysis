import requests
import plotly.graph_objects as go

# Fetch data from FMP API
def fetch_fmp_data(endpoint, symbol, api_key):
    url = f"https://financialmodelingprep.com/api/v3/{endpoint}/{symbol}?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Fetch historical stock data
def fetch_stock_data(ticker, api_key, days):
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?timeseries={days}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Fetch sector P/E ratios
def fetch_sector_pe(api_key):
    url = f"https://financialmodelingprep.com/api/v3/pe-ratio-sector?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Fetch industry P/E ratios
def fetch_industry_pe(industry, api_key):
    url = f"https://financialmodelingprep.com/api/v3/pe-ratio-industry?apikey={api_key}&industry={industry}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Plot candlestick chart
def plot_candlestick_chart(data, timeframe):
    historical = data["historical"]
    dates = [entry["date"] for entry in historical]
    opens = [entry["open"] for entry in historical]
    highs = [entry["high"] for entry in historical]
    lows = [entry["low"] for entry in historical]
    closes = [entry["close"] for entry in historical]

    fig = go.Figure(
        data=[
            go.Candlestick(
                x=dates,
                open=opens,
                high=highs,
                low=lows,
                close=closes,
                name="Candlestick Chart",
            )
        ]
    )
    fig.update_layout(
        title=f"Stock Price ({timeframe})",
        xaxis_title="Date",
        yaxis_title="Price ($)",
        autosize=False,
        width=900,  # Set a wider width
        height=500,  # Set an appropriate height
        margin=dict(l=50, r=50, t=50, b=50),  # Add some padding
    )
    return fig
