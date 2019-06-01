# https://aroussi.com/post/python-yahoo-finance

import yfinance as yf
data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30",
                   group_by="ticker")
print(data)
