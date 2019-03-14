from iexfinance.stocks import Stock
#aapl = Stock("AAPL")
#aapl.get_price()

def getStockPrice(symbol):
	price = Stock(symbol).get_price()
	return price

def getStockCompany(symbol):
	company = Stock(symbol).get_company_name()
	return company

def getStockPercentChange(symbol):
	#change since previous day
	percentChange = Stock(symbol).get_previous()["changePercent"]
	return percentChange

def getStockVWAP(symbol):
	#volume-weighted average price, average price of stock over time
	vwap = Stock(symbol).get_previous()["vwap"]
	return vwap

#also get_previous()["date", "open", "close", "high", "low", "close", "volume", "change"]

# print getStockPrice("AAPL")
# print getStockCompany("AAPL")
# print getStockPercentChange("AAPL")
# print getStockVWAP("AAPL")