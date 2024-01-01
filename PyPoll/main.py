#main file for PyPoll challenge
import os
import csv

#declare and initialize variables
votes = 0
candidates = []
percentage_votes = []
candidate_votes = []
winner = " "

#get CSV file
election_data_csv = os.path.join("Resources", "election_data.csv")

#open CSV file
with open(election_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        for candidate in candidates:
            if row[2] == candidate:
                candidates.append(row[2])
