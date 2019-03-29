from django.http import HttpResponse
from django.shortcuts import render
from main.dbTesting import get_all_stocks, stocks, get_user,get_user_stocks_and_price
import matplotlib.pyplot as plt
import stock_info

def index(request):
    return render(request, 'main/home.html')

def dash(request):
	user = request.user
	user = get_user("isaaccarone")
	U_stocks = get_user_stocks_and_price(user.values_list()[0][0])
	stocks = []
	names = []
	for i,k in U_stocks:
		stocks.append(float(k)*(stock_info.getStockPrice(i)))
		names.append(i)
	plt.pie(stocks,labels=names,autopct='%.1f%%', startangle=90,shadow=True)
	plt.savefig("main/static/pie.jpg")
	return render(request, 'main/dash.html',{"stocks":stocks,"last":U_stocks,"cash":user.values_list()[0][5]})

def buy_sell(request):
	user = request.user
	user = get_user("isaaccarone")
	U_stocks = get_user_stocks_and_price(user.values_list()[0][0])
	return render(request, 'main/buy_sell.html',{"stocks":stocks,"last":U_stocks,"cash":user.values_list()[0][5]})