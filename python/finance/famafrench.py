# WORKS PERFECTLY!!!!!!!!!

# Source
# https://pandas-datareader.readthedocs.io/en/latest/remote_data.html

from pandas_datareader.famafrench import get_available_datasets
import pandas_datareader.data as web

len(get_available_datasets())

ds = web.DataReader('5_Industry_Portfolios', 'famafrench')

print(ds['DESCR'])
