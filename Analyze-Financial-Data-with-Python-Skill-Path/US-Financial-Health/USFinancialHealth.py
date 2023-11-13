"""
In this project, we'll be importing various types of financial data to try and determine the financial health and volatility of the US between 1999 and 2019.
"""
import pandas as pd
import pandas_datareader.data as web
import pandas_datareader.wb as wb
import numpy as np
from datetime import datetime

gold_prices = pd.read_csv('gold_prices.csv')
crude_oil_prices = pd.read_csv('crude_oil_prices.csv')
#print(gold_prices)
#print(crude_oil_prices)

#Calculating Log Return
def log_return(prices):
  return np.log(prices / prices.shift(1))

start_date = datetime(1999, 1, 1)
end_date = datetime(2019, 1, 1)
nasdaq_data = web.DataReader("NASDAQ100", "fred", start_date, end_date)
sap_data = web.DataReader("SP500", "fred", start_date, end_date)

gold_returns = log_return(gold_prices['Gold_Price'])
crude_oil_returns = log_return(crude_oil_prices['Crude_Oil_Price'])
nasdaq_returns = log_return(nasdaq_data['NASDAQ100'])
sap_returns = log_return(sap_data['SP500'])

try:
    gdp_data = wb.download(indicator = 'NY.GDP.MKTP.CD', country = ['US'], start = start_date, end = end_date)
    export_data = wb.download(indicator = 'NE.EXP.GNFS.CN', country = ['US'], start = start_date, end = end_date)
    gdp_returns = log_return(gdp_data['NY.GDP.MKTP.CD'])
    export_returns = log_return(export_data['NE.EXP.GNFS.CN'])
except Exception as e:
    print(f"An error occurred: {e}")