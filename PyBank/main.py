#main script for PyBank challenge
#Totals number of months of data, amount of profit/losses, greatest increase and greatest decrease among bank records

import os
import csv

#get csv file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#use csv file to calculate number of months of data
with open(budget_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    monthscounter = 0
    total = 0
    for row in csv_reader:
        monthscounter = monthscounter +1
        total = total + int(row[1])
#print results
print("\n Financial Analysis \n--------------------------------")
print(f"\nTotal Months: ", monthscounter)
print(f"\nTotal: ${total}")

