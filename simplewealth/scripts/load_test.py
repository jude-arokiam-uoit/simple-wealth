# import libraries -------------------------------------------------------------
import names
import random
from pprint import pprint
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# USERS TABLE
# ------------------------------------------------------------------------------
# generate random names for users
str_names = [names.get_full_name() for i in range(20)]
pprint(str_names)

# derive username, firstname and lastname from generated names
users = []
for name in str_names:
	split_name = name.split(' ')
		
	username = split_name[0].lower() + split_name[1].lower()
	firstname = split_name[0]
	lastname = split_name[1]

	user = [username, firstname, lastname]
	users.append(user)
pprint(users)

# randomly assign a risk status to each user
risk_status = ('Low', 'Medium', 'High')
for user in users:
	user.append(risk_status[random.randint(0,2)])
pprint(users)

# randomly allocate cash amount to each user within 5000 and 100000
for user in users:
	user.append(round(random.uniform(5000,100000),2))
pprint(users)

# ------------------------------------------------------------------------------
# TRANSACTIONS TABLE
# ------------------------------------------------------------------------------
stocks = (
	('TD', 'Financial'),
	('JPM', 'Financial'),
	('V', 'Financial'),
	('BRK.B', 'Financial'),
	('AAPL', 'Technology'),
	('MSFT', 'Technology'),
	('AMZN', 'Technology'),
	('FB', 'Technology'),
	('ENB', 'Energy'),
	('TRP', 'Energy'),
	('XOM', 'Energy'),
	('CVX', 'Energy'),
	('BA', 'Transportation'),
	('UNP', 'Transportation'),
	('UTX', 'Transportation'),
	('TSLA', 'Transportation'),
	('PG', 'Consumer'),
	('KO', 'Consumer'),
	('MCD', 'Consumer'),
	('WMT', 'Consumer')
	)
pprint(stocks)

sectors = ('Financial', 'Technology', 'Energy', 'Transportation', 'Consumer')

#for user in users:
