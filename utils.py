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
        width=700,  # Reduced width
        height=400,  # Reduced height
        margin=dict(l=40, r=40, t=40, b=40),  # Add some padding
    )
    return fig

