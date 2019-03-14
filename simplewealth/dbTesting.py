import os
import django
import datetime
import stock_info
import numpy as np

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simplewealth.settings")
django.setup()

from main.models import Users, Stocks, Transactions
from django.db.models import Count

stocks = ["TD","JPM","V","BRK.B","AAPL","MSFT","AMZN","FB","ENB","TRP","XOM","CVX","BA","UNP","UTX","TSLA","PG","KO","MCD","WMT"]

def create_stock(symbol, company, current_price, change_percentage, vwap):
	new_stock = Stocks(symbol=symbol, company=company, current_price=current_price, change_percentage=change_percentage, vwap=vwap)
	new_stock.save()

def create_transaction(user, stock, amount, transaction_type):
	new_transaction = Transactions(user=user, stock=stock, timestamp=datetime.datetime.now(),amount=amount, transaction_type=transaction_type)
	new_transaction.save()

def create_user(username, password, first_name, last_name, risk_status, cash_amount, sector):
	new_user = Users(username=username,password=password,first_name=first_name,last_name=last_name,risk_status=risk_status,cash_amount=cash_amount,sector_breakdown=sector)
	new_user.save()

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
	table_list = Transactions.objects.annotate(Count('timestamp')).order_by('-timestamp__count')[:10].values_list()
	table_array = np.core.records.fromrecords(table_list, names=[f.name for f in Transactions._meta.fields])
	return table_array

def perform_transaction(username, amount):
	user = Users.objects.get(username = username)
	user.cash_amount -= amount
	user.save()

#create_user("1005555555", "password2", "Jude", "Arokiam", "Hi", "1000", "Sector")
# create_user("100553756", "password2", "Mitch", "Childerhose", "Hi", "1000", "Sector")
#mitch = Users.objects.get(username = "100553756")
# jude = Users.objects.get(username = "100553756")
#TD = Stocks.objects.get(symbol="TD")
#TSLA = Stocks.objects.get(symbol="TSLA")
# create_transaction(jude, TSLA, 600, "-")
# create_transaction(mitch, TSLA, 100.0, "+")