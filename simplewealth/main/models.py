from django.db import models

class Users(models.Model):
	HI = "Hi"
	MED = "Med"
	LO = "Lo"
	RISK_STATUS_CHOICES = (
		(HI, 'High'),
		(MED, 'Medium'),
		(LO, 'Low'),
	)

	username = models.CharField(primary_key=True, max_length=20)
	password = models.CharField(max_length=20)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	risk_status = models.CharField(max_length=2,
		choices = RISK_STATUS_CHOICES, default = MED,
	)
	cash_amount = models.FloatField(default=0)
	sector_breakdown = models.CharField(max_length=100)

	def __str__(self):
		return self.username

class Shares(models.Model):
	username = models.ForeignKey(Users, on_delete=models.CASCADE, primary_key=True)
	TD = models.PositiveSmallIntegerField(default = 0)
	JPM = models.PositiveSmallIntegerField(default = 0)
	V = models.PositiveSmallIntegerField(default = 0)
	BRKB = models.PositiveSmallIntegerField(default = 0)
	AAPL = models.PositiveSmallIntegerField(default = 0)
	MSFT = models.PositiveSmallIntegerField(default = 0)
	AMZN = models.PositiveSmallIntegerField(default = 0)
	FB = models.PositiveSmallIntegerField(default = 0)
	ENB = models.PositiveSmallIntegerField(default = 0)
	TRP = models.PositiveSmallIntegerField(default = 0)
	XOM = models.PositiveSmallIntegerField(default = 0)
	CVX = models.PositiveSmallIntegerField(default = 0)
	BA = models.PositiveSmallIntegerField(default = 0)
	UNP = models.PositiveSmallIntegerField(default = 0)
	UTX = models.PositiveSmallIntegerField(default = 0)
	TSLA = models.PositiveSmallIntegerField(default = 0)
	PG = models.PositiveSmallIntegerField(default = 0)
	KO = models.PositiveSmallIntegerField(default = 0)
	MCD = models.PositiveSmallIntegerField(default = 0)
	WMT = models.PositiveSmallIntegerField(default = 0)

class Stocks(models.Model):
	symbol = models.CharField(primary_key=True, max_length=5)
	company = models.CharField(max_length=50)
	current_price = models.FloatField(default=0)
	change_percentage = models.FloatField(default=0)
	vwap = models.FloatField(default=0)

	def __str__(self):
		return self.symbol

class Transactions(models.Model):
	TRANSACTION_TYPE_CHOICES = (
		('+', 'Buy'),
		('-', 'Sell'),
	)

	transaction_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(Users, on_delete=models.CASCADE)
	stock = models.ForeignKey(Stocks, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)
	number_of_shares = models.FloatField(default=0)

	transaction_type = models.CharField(
		max_length=2,
		choices = TRANSACTION_TYPE_CHOICES, 
		default = "+",
	)