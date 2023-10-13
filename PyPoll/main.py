# Import modules
import os
import csv

# Set variables
total_votes = 0
total_candidates = []
unique_candidates = []
votes_per_candidate = []
votes_percentage = []

# Set csv path
csvpath = 'Resources/election_data.csv'

# Open CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Read header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# Total number of votes cast
# List of candidates who received votes
    for row in csvreader:
        total_votes += 1
        total_candidates.append(row[2])
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2])
# Total number of votes each candidate won
    for candidate in unique_candidates:
        votes_per_candidate.append(total_candidates.count(candidate))
   
# Percentage of votes each candidate won
    for votes in votes_per_candidate:
        percentage = round(((votes/sum(votes_per_candidate))*100), 3)
        votes_percentage.append(percentage)

# Winner of the election based on popular vote
    highest_votes = max(votes_per_candidate)
    highest_votes_index = votes_per_candidate.index(highest_votes)
    winner = unique_candidates[highest_votes_index]

# Print analysis to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for i in range(len(unique_candidates)):
    print(f"{unique_candidates[i]}: {votes_percentage[i]}% ({votes_per_candidate[i]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export text file with results
# Save output file path
# Open text file for writing
output_file = 'Analysis/election_results.txt'

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("-------------------------\n")
    for i in range(len(unique_candidates)):
        text.write(f"{unique_candidates[i]}: {votes_percentage[i]}% ({votes_per_candidate[i]})\n")
    text.write("-------------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write("-------------------------\n")