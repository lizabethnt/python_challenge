#main script for PyBank challenge
#Totals number of months of data, amount of profit/losses, greatest increase and greatest decrease among bank records

import os
import csv

#declare variables
total = 0
prev_row_profit = 0
avg_change = 0
greatest_increase = 0
greatest_decrease = 0
months_counter = 0
change = []
dates = []
change_counter = 0

#get csv file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#use csv file to calculate number of months of data, total profit/loss, 
#AVG profit/loss, greatest profit and greatest decrease in profits
with open(budget_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csv_reader:

#find the number of months
        months_counter = months_counter + 1

#find the total profit/loss
        total = total + int(row[1])

#find the changes for each month
        change.append(int(row[1]) - prev_row_profit)

#setup for next row's calculation
        prev_row_profit = int(row[1])

#store the dates column as a list
        dates.append(row[0])

#find the greatest increase and associated date
for value in change:
        if value > greatest_increase:
                greatest_increase = value
                greatest_increase_date = dates[change_counter]

        if value < greatest_decrease:
                greatest_decrease = value
                greatest_decrease_date = dates[change_counter]
        
        change_counter += 1
        
#find the average change:first remove initial month's change list entry as it should be N/A
del change[0]
avg_change = sum(change)/(len(change))

#print results
print("\n Financial Analysis \n------------------------")
print(f"\nTotal Months: ", months_counter)
print(f"\nTotal: ${total}")
print(f"\nAverage Change: ${round(avg_change,2)}")
print(f"\n\nGreatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"\n\nGreatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Set variable for output file
output_file = os.path.join("python_challenge_final.txt")

#  Open the output file
with open(output_file, "w") as textfile:
    textfile.write("Financial Analysis \n\n------------------------")
    textfile.write(f"\n\nTotal Months: {months_counter}")
    textfile.write(f"\n\nTotal: ${total}")
    textfile.write(f"\n\nAverage Change: ${round(avg_change,2)}")
    textfile.write(f"\n\nGreatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    textfile.write(f"\n\nGreatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

