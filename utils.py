import requests
import plotly.graph_objects as go

# Fetch data from FMP API
def fetch_fmp_data(endpoint, symbol, api_key):
    """
    Fetch data from the Financial Modeling Prep API for a given endpoint and stock symbol.
    
    Args:
        endpoint (str): API endpoint (e.g., "profile", "ratios").
        symbol (str): Stock ticker symbol (e.g., "AAPL").
        api_key (str): Financial Modeling Prep API key.
    
    Returns:
        dict or None: JSON response if successful, None otherwise.
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
    
    Args:
        ticker (str): Stock ticker symbol.
        api_key (str): Financial Modeling Prep API key.
        days (int): Number of days of historical data to fetch.
    
    Returns:
        dict or None: JSON response if successful, None otherwise.
    """
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?timeseries={days}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Fetch sector P/E ratios
def fetch_sector_pe(api_key):
    """
    Fetch sector P/E ratios from the Financial Modeling Prep API.
    
    Args:
        api_key (str): Financial Modeling Prep API key.
    
    Returns:
        dict or None: JSON response if successful, None otherwise.
    """
    url = f"https://financialmodelingprep.com/api/v3/pe-ratio-sector?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Fetch industry P/E ratios
def fetch_industry_pe(industry, api_key):
    """
    Fetch industry P/E ratios from the Financial Modeling Prep API.
    
    Args:
        industry (str): Industry name.
        api_key (str): Financial Modeling Prep API key.
    
    Returns:
        dict or None: JSON response if successful, None otherwise.
    """
    url = f"https://financialmodelingprep.com/api/v3/pe-ratio-industry?apikey={api_key}&industry={industry}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Plot candlestick chart
def plot_candlestick_chart(data, timeframe):
    """
    Plot a candlestick chart for the given stock data.
    
    Args:
        data (dict): Historical stock data.
        timeframe (str): Timeframe for the chart (e.g., "Last 7 Days").
    
    Returns:
        Plotly Figure: Candlestick chart.
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
        width=700,  # Adjust width
        height=400,  # Adjust height
        margin=dict(l=40, r=40, t=40, b=40),  # Add padding
    )
    return fig

