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
def fetch_stock_data(ticker, api_key):
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?timeseries=30&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Plot stock price chart
def plot_stock_chart(data):
    dates = [entry['date'] for entry in data['historical']]
    prices = [entry['close'] for entry in data['historical']]
    fig = go.Figure(data=[go.Scatter(x=dates, y=prices, mode='lines', name='Price')])
    fig.update_layout(title="Stock Price (Last 30 Days)", xaxis_title="Date", yaxis_title="Price ($)")
    return fig
