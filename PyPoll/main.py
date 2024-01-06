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

#fill the percentage_votes list with percentages of each candidate
for candidate in candidate_votes:
    percentage_votes.append(candidate_votes[candidate] / votes)
#find the winner
    if candidate_votes[candidate] > greatest_votes:
        greatest_votes = candidate_votes[candidate]
        winner = str(candidate)

#print all results in the same formatting as demonstrated in the assignment from bootcamp
print(f"Election Results\n -------------------------------")
print(f"\nTotal Votes: {votes} \n ------------------------------")     

#iterate printing the votes and percentage for each candidate
counter = 0
for candidate in candidate_votes:
    print(f"\n{list(candidate_votes.keys())[counter]}: {round(percentage_votes[counter] * 100, 3)}% ({candidate_votes[candidate]})")
    counter += 1

print(f"\n ------------------------------")
print("\nWinner: ", winner)
print(f"\n ------------------------------")

# Set variable for output file
output_file = os.path.join("analysis", "PyPoll_analysis.txt")

#  Open the output file and write all results to it
with open(output_file, "w") as textfile:
    textfile.write(f"Election Results\n -------------------------------\n")
    textfile.write(f"\nTotal Votes: {votes} \n ------------------------------\n")
    counter = 0
    for candidate in candidate_votes:
        textfile.write(f"\n{list(candidate_votes.keys())[counter]}: {round(percentage_votes[counter] * 100, 3)}% ({candidate_votes[candidate]})\n")
        counter += 1
    textfile.write(f"\n ------------------------------")
    textfile.write(f"\nWinner: {winner}")
    textfile.write(f"\n ------------------------------")
