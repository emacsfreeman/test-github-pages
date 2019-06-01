# WORKS PERFECTLY!!!!!!

# Source
# https://pandas-datareader.readthedocs.io/en/latest/remote_data.html

from pandas_datareader import wb
mathces = wb.search('gdp.*capita.*const')

dat = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'CA', 'MX'], start=2005, end=2008)

print(dat)
