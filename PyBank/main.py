#main script for PyBank challenge
#Totals number of months of data, amount of profit/losses, greatest increase and greatest decrease among bank records

import os
import csv

#declare variables
total = 0
prev_row_profit = 0
avg_change = 0
greatest_profit = 0
greatest_decrease = 0
months_counter = 0
change = []
#get csv file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#use csv file to calculate number of months of data, total profit/loss, 
#AVG profit/loss, greatest profit and greatest decrease in profits
with open(budget_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
#find the number of months
        months_counter = months_counter + 1
#find the total profit/loss
        total = total + int(row[1])
#find the change

#print results
print(change)
print("\n Financial Analysis \n--------------------------------")
print(f"\nTotal Months: ", months_counter)
print(f"\nTotal: ${total}")