import csv

user_table = []

with open('users.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        user_table.append(row)
csvFile.close()

import dbTesting

for user in user_table:
    username = user[0]
    password = user[1]
    firstname = user[2]
    lastname = user[3]
    risk_profile = user[4]
    cash_bal = user[5]

    dbTesting.create_user(username, password, firstname, lastname, risk_profile, cash_bal)

print('DONE')
