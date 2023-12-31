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

#find the changes for each month
        change.append(int(row[1]) - prev_row_profit)

#setup for next row's calculation
        prev_row_profit = int(row[1])

#find the average change:need to first remove initial month's change list entry as it should be N/A
del change[0]
avg_change = sum(change)/(len(change))

#print results
print(change)
print("\n Financial Analysis \n------------------------")
print(f"\nTotal Months: ", months_counter)
print(f"\nTotal: ${total}")
print(f"\nAverage Change: ${round(avg_change,2)}")

# Set variable for output file
output_file = os.path.join("python_challenge_final.txt")

#  Open the output file
with open(output_file, "w") as textfile:
    textfile.write("Financial Analysis \n\n------------------------")
    textfile.write(f"\n\nTotal Months: {months_counter}")
    textfile.write(f"\n\nTotal: ${total}")
    textfile.write(f"\n\nAverage Change: ${round(avg_change,2)}")