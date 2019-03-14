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

	user_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	risk_status = models.CharField(max_length=2,
		choices = RISK_STATUS_CHOICES, default = MED,
	)
	cash_amount = models.FloatField(default=0)
	sector_breakdown = models.CharField(max_length=100)

	def __str__(self):
		return str(self.user_id) + " " + self.username

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
	amount = models.FloatField(default=0)

	transaction_type = models.CharField(
		max_length=2,
		choices = TRANSACTION_TYPE_CHOICES, 
		default = "+",
	)