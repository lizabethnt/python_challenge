#main script for PyBank challenge
#Totals number of months of data, amount of profit/losses, greatest increase and greatest decrease among bank records

import os
import csv

#get csv file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#use csv file to calculate number of months of data, total profit/loss, 
#AVG profit/loss, greatest profit and greatest decrease in profits
with open(budget_data_csv) as csvfile:
#declare variables
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    monthscounter = 0
    total = 0
    prev_row_profit = 0
    avgchange = 0
    greatest_profit = 0
    greatest_decrease = 0

    for row in csv_reader:
#find the total profit/loss
        total = total + int(row[1])
#find the number of months
        monthscounter = monthscounter +1
#collect profit/loss differences
        profit_or_loss = [int(row[1]) - prev_row_profit for row in csv_reader]
        prev_row_profit = int(row[1])
#find the average profit/loss
avgchange = sum(profit_or_loss)/len(profit_or_loss)


#print results
print("\n Financial Analysis \n--------------------------------")
print(f"\nTotal Months: ", monthscounter)
print(f"\nTotal: ${total}")
print(f"\nAverage Change: ${avgchange}")

