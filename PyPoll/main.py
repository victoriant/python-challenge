# Election Data

import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# total_votes = 0

# candidate_options = []
# candidate_votes = {}

# winning_candidate = ""
# winning_count = 0
# winning_percentage = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    total_votes = -1

    Charles_count = 0
    Diana_count = 0 
    Raymon_count = 0

    Charles_percent = Diana_percent = Raymon_percent = 0


    for row in csvreader:

        total_votes += 1

        if row[2] == "Charles Casper Stockham":
            Charles_count += 1
        elif row[2] == "Diana DeGette":
            Diana_count += 1 
        elif row[2] == "Raymon Anthony Doane":
            Raymon_count += 1

    Results = {"Charles Casper Stockham":Charles_count, "Diana DeGette":Diana_count, "Raymon Anthony Doane":Raymon_count}

    Charles_percent = round((Charles_count / total_votes) * 100, 3)
    Diana_percent = round((Diana_count / total_votes) * 100, 3)
    Raymon_percent = round((Raymon_count / total_votes) * 100, 3)

    Winner = max(Results, key=Results.get)

print("Election Results")

print("--------------------------")

# The total number of votes cast
print(f"Total Votes: {total_votes}")

print("--------------------------")

# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
print(f"Charles Casper Stockham: {Charles_percent}% ({Charles_count})")
print(f"Diana DeGette: {Diana_percent}% ({Diana_count})")
print(f"Raymon Anthony Doane: {Raymon_percent}% ({Raymon_count})")

# The winner of the election based on popular vote
print("-----------------------------")

print(f"Winner: {Winner}")

print("")

output =  ("Election Results\n"
f"----------------------------\n"
f"Total Votes: {total_votes}\n"
f"----------------------------\n"
f"Charles Casper Stockham: {Charles_percent}% ({Charles_count})\n"
f"Diana DeGette: {Diana_percent}% ({Diana_count})\n"
f"Raymon Anthony Doane: {Raymon_percent}% ({Raymon_count})\n"
f"----------------------------\n"
f"Winner: {Winner}\n"
f"-----------------------------\n")

output_file = os.path.join("election_data_final.csv")

with open(output_file, "w") as analysis:
    
    analysis.write(output)
