import os
import django
import datetime
import stock_info
import numpy as np
import pprint

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simplewealth.settings")
django.setup()

from main.models import Users, Stocks, Transactions, Shares
from django.db.models import Count

stocks = ["TD","JPM","V","BRK.B","AAPL","MSFT","AMZN","FB","ENB","TRP","XOM","CVX","BA","UNP","UTX","TSLA","PG","KO","MCD","WMT"]

def create_stock(symbol, company, current_price, change_percentage, vwap):
	new_stock = Stocks(symbol=symbol, company=company, current_price=current_price, change_percentage=change_percentage, vwap=vwap)
	new_stock.save()

def create_user(username, password, first_name, last_name, risk_status, cash_amount):
	new_user = Users(username=username,password=password,first_name=first_name,last_name=last_name,risk_status=risk_status,cash_amount=cash_amount)
	init_share = Shares(username = new_user, risk_status = new_user.risk_status, cash_amount = new_user.cash_amount)
	new_user.save()
	init_share.save()

def populate_shares(username, risk_status, cash_amount,
	stock1,stock2,stock3,stock4,stock5,
	stock6,stock7,stock8,stock9,stock10,
	stock11,stock12,stock13,stock14,stock15,
	stock16,stock17,stock18,stock19,stock20):
	share = Shares.objects.get(username = username)
	share.risk_status = risk_status
	share.cash_amount = cash_amount
	share.TD = stock1; share.JPM = stock2; share.V = stock3; share.BRKB = stock4; share.AAPL = stock5;
	share.MSFT = stock6; share.AMZN = stock7; share.FB = stock8; share.ENB = stock9; share.TRP = stock10;
	share.XOM = stock11; share.CVX = stock12; share.BA = stock13; share.UNP = stock14; share.UTX = stock15;
	share.TSLA = stock16; share.PG = stock17; share.KO = stock18; share.MCD = stock19; share.WMT = stock20;

	share.save()

def create_all_stocks():
	for x in stocks:
		create_stock(x,stock_info.getStockCompany(x),stock_info.getStockPrice(x),stock_info.getStockPercentChange(x),stock_info.getStockVWAP(x))

def get_all_transactions():
	print(Transactions.objects.all().values_list())

def get_all_stocks():
	print(Stocks.objects.all().values_list())

def delete_all_transactions():
	Transactions.objects.all().delete()

def delete_all_users():
	Users.objects.all().delete()

def get_table_array(table):
	table_list = table.objects.all().values_list()
	table_array = np.core.records.fromrecords(table_list, names=[f.name for f in table._meta.fields])
	return table_array

def get_last_ten_transactions():
	table_list = Transactions.objects.annotate(Count('transaction_id')).order_by('transaction_id__count')[:10].values_list()
	table_array = np.core.records.fromrecords(table_list, names=[f.name for f in Transactions._meta.fields])
	return table_array[::-1]

#transaction_type: True = buy, False = sell
def perform_transaction(username, symbol, shares, transaction_type):
	user = Users.objects.get(username = username)
	stock = Stocks.objects.get(symbol = symbol)
	share = Shares.objects.get(username = username)

	new_transaction = Transactions(user=user, stock=stock, timestamp=datetime.datetime.now(),number_of_shares=shares, transaction_type=transaction_type)
	new_transaction.save()	

	if transaction_type == "+":
		#subtract stock amount purchased from users wallet
		user.cash_amount -= stock_info.getStockPrice(symbol) * shares
		#add number of shares on the given stock in Shares table
		share.__dict__[symbol] += shares
	else:
		#add stock amount sold to users wallet
		user.cash_amount += stock_info.getStockPrice(symbol) * shares
		#subtract number of shares from the given stock in Shares table
		share.__dict__[symbol] -= shares

	user.save()
	share.save()

#get_user_stocks returns all the user's currently owned stock
#list of lists containing stock symbol, stock name, number of shares owned, and current stock price
def get_user_stocks(username):
	column = 1

	shares = Shares.objects.filter(username = username).values_list()
	shares_array = shares[::1]
	user_stocks = []

	for i in shares_array:
		for j in i:
			if column > 3 and j!=0:
				user_stocks.append([stocks[column-4], stock_info.getStockCompany(stocks[column-4]), str(j), str(stock_info.getStockPrice(stocks[column-4]))])
			column+=1

		column = 0			

	return user_stocks

# get_user_stocks_raw returns all the user's currently owned stock in the raw 
# format stored in the database table
#list containing stock symbol, stock name, number of shares owned, and current stock price
def get_user_stocks_raw(username):
	return Shares.objects.filter(username = username).values_list()[0]

def empty_all_tables():
	Users.objects.all().delete()
	Stocks.objects.all().delete()
	Transactions.objects.all().delete()
	Shares.objects.all().delete()

#empty_all_tables()
#Users.objects.all().delete()
#create_user("1005559999", "1005559999", "mit", "jud", 1, 100.0)
# perform_transaction("1005559999", "TD", 5, "+")
# print(get_table_array(Shares))
# print(get_user_stocks("1005559999"))
#populate_shares("1005559999", 1, 1000.0, 1,1,1,1,1,1,1,1,1,1,12,1,1,1,1,14,1,1,1,1)
#print(get_table_array(Shares))