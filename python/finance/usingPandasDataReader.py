# https://aroussi.com/post/python-yahoo-finance

from pandas_datareader import data as pdr

import yfinance as yf
yf.pdr_override() # <== that's all it takes :-)

# download dataframe using pandas_datareader
data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")

print(data)
