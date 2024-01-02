#main file for PyPoll challenge
import os
import csv

#declare and initialize variables
votes = 0
candidates = []
percentage_votes = []
candidate_votes = {}
winner = " "
results = {}
#get CSV file
election_data_csv = os.path.join("Resources", "election_data.csv")

#open CSV file
with open(election_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        if str(row[2]) not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 0
        candidate_votes[row[2]] += 1
        votes += 1
print(candidate_votes)       
print(candidates)
print(votes)
