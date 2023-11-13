from utils import *

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

amazon_prices = [1699.8, 1777.44, 2012.71, 2003.0, 1598.01, 1690.17, 1501.97, 1718.73, 1639.83, 1780.75, 1926.52, 1775.07, 1893.63]
ebay_prices = [35.98, 33.2, 34.35, 32.77, 28.81, 29.62, 27.86, 33.39, 37.01, 37.0, 38.6, 35.93, 39.5]

# Write code here
def get_returns(prices):
  returns = []
  for i in range(len(prices) - 1):
    returns.append(calculate_log_return(prices[i], prices[i+1]))
  return returns

amazon_returns = get_returns(amazon_prices)
ebay_returns = get_returns(ebay_prices)

amazon_returns_percentage = [display_as_percentage(a) for a in amazon_returns]
ebay_returns_percentage = [display_as_percentage(e) for e in ebay_returns]
#print('The monthly log rates of return for Amazon are', ', '.join(amazon_returns_percentage))
#print('The monthly log rates of return for eBay are',', '.join(ebay_returns_percentage))

amazon_annual_return = sum(amazon_returns)
ebay_annual_return = sum(ebay_returns)
#print('The annual log rate of return for Amazon is', display_as_percentage(amazon_annual_return))
#print('The annual log rate of return for Ebay is', display_as_percentage(ebay_annual_return))

#Assess Investment Risk
amazon_price_variance = calculate_variance(amazon_returns)
ebay_price_variance = calculate_variance(ebay_returns)
#print('The variance of Amazon stock is', amazon_price_variance)
#print('The variance of eBay stock is', ebay_price_variance)

amazon_stddev = calculate_stddev(amazon_returns)
ebay_stddev = calculate_stddev(ebay_returns)
#print('The standard deviation of Amazon stock returns is', display_as_percentage(amazon_stddev))
#print('The standard deviation of eBay stock returns is', display_as_percentage(ebay_stddev))

amazon_ebay_corr = calculate_correlation(amazon_returns, ebay_returns)
print('The correlation coefficient between Amazon and ebay stock is', amazon_ebay_corr)

