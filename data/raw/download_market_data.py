'''
Download market data from yahoo finance.

Output :
    - market_data.csv
'''

import yfinance as yf

data = yf.download(
    ["SPY", "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "TSLA", "META"],
    start="2010-01-01",
    end="2026-01-01",
    auto_adjust= False,
    actions= True,
)

data.to_csv("data/raw/market_data.csv")

prices = data["Close"]