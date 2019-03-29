import csv

accounts_table = []

with open('accounts.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        accounts_table.append(row)
csvFile.close()

import dbTesting

for user in accounts_table:
    dbTesting.populate_shares(
        user[0],        
        user[1],        
        user[2],        
        user[3],        
        user[4],        
        user[5],        
        user[6],        
        user[7],        
        user[8],        
        user[9],        
        user[10],        
        user[11],        
        user[12],        
        user[13],        
        user[14],        
        user[15],        
        user[16],        
        user[17],        
        user[18],        
        user[19],        
        user[20],        
        user[21],        
        user[22]        
    )

print('DONE')
