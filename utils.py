import requests
import plotly.graph_objects as go


# Fetch data from FMP API
def fetch_fmp_data(endpoint, symbol, api_key):
    """
    Fetch data from the Financial Modeling Prep API for a given endpoint and stock symbol.
    """
    url = f"https://financialmodelingprep.com/api/v3/{endpoint}/{symbol}?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


# Fetch historical stock data
def fetch_stock_data(ticker, api_key, days):
    """
    Fetch historical stock data for the given ticker and timeframe.
    """
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?timeseries={days}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


# Fetch sector P/E ratios
def fetch_sector_pe(date, exchange, api_key):
    """
    Fetch sector P/E ratios from the Financial Modeling Prep API.
    """
    url = f"https://financialmodelingprep.com/api/v4/sector_price_earning_ratio?date={date}&exchange={exchange}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


# Fetch industry P/E ratios
def fetch_industry_pe(date, exchange, api_key):
    """
    Fetch industry P/E ratios from the Financial Modeling Prep API.
    """
    url = f"https://financialmodelingprep.com/api/v4/industry_price_earning_ratio?date={date}&exchange={exchange}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


# Plot candlestick chart
def plot_candlestick_chart(data, timeframe):
    """
    Plot a candlestick chart for the given stock data.
    """
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
        width=700,
        height=400,
        margin=dict(l=40, r=40, t=40, b=40),
    )
    return fig

