from django.http import HttpResponse
from django.shortcuts import render
from main.dbTesting import get_user,get_user_stocks_and_price,perform_transaction
import matplotlib.pyplot as plt
import stock_info
from main.ai import get_recommendations
from django.shortcuts import redirect

def index(request):
    return render(request, 'main/home.html')

def dash(request):
	user = request.user
	user = get_user(user.username)
	U_stocks = get_user_stocks_and_price(user.values_list()[0][0])
	stocks = []
	names = []
	for i,k in U_stocks:
		stocks.append(float(k)*(stock_info.getStockPrice(i)))
		names.append(i)
	plt.pie(stocks,labels=names,autopct='%.1f%%', startangle=90,shadow=False)
	plt.savefig("main/static/pie.jpg")
	ai = get_recommendations(user.values_list()[0][0])
	return render(request, 'main/dash.html',{"stocks":U_stocks,"cash":user.values_list()[0][5], "reccomend":ai})

def buy_sell(request):
	if request.method == "POST":
		stock = request.POST['stock']
		choice = request.POST['buySell']
		amount = int(request.POST['numStock'])
		print(request.user.username)
		perform_transaction(request.user.username,stock,amount,choice)
		return redirect(dash)
	user = request.user
	user=get_user(user.username)
	return render(request, 'main/buy_sell.html',{"cash":user.values_list()[0][5]})

