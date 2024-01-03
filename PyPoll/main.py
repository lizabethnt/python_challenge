#main file for PyPoll challenge
import os
import csv

#declare and initialize variables
votes = 0
candidates = []
percentage_votes = []
candidate_votes = {}
winner = " "
greatest_votes = 0

#get CSV file
election_data_csv = os.path.join("Resources", "election_data.csv")

#open CSV file
with open(election_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

#calculate total number of votes
    for row in csv_reader:
        votes += 1
#fill candidate_votes dictionary with unique candidate names and each canddiate's number of votes
        if str(row[2]) not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 0
        candidate_votes[row[2]] += 1

for candidate in candidate_votes:
    percentage_votes.append(candidate_votes[candidate] / votes)
    if candidate_votes[candidate] > greatest_votes:
        greatest_votes = candidate_votes[candidate]
        winner = str(candidate)

#todo:  print all results in the same formatting as shown in the assignment
print(f"Election Results\n -------------------------------")
print(f"\nTotal Votes: {votes} \n ------------------------------")     

#todo:  write a version of this which iterates for each candidate with votes
print(f"\n", list(candidate_votes.keys())[0], ":", percentage_votes[0], "(", percentage_votes[0],")")
print("\n",percentage_votes)
print("\n", winner)

#todo: copy all results to a text file
