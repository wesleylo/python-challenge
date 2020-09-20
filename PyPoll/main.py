import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv') # ./Resources/election_data.csv

numrows = 0
candidates = []
votecounts = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    headers = next(csvreader) # Store the header row
    print(headers)

    for row in csvreader:
        currentcandidate = row[2]
        numrows += 1 # Iterate numrows
        if not currentcandidate in candidates: 
            candidates.append(currentcandidate)
            votecounts.append(0)

        votecounts[candidates.index(currentcandidate)] += 1 # Find index of current candidate and iterate corresponding votecount
        
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(numrows))
print("-------------------------")
for candidate in candidates:
    numvotes = votecounts[candidates.index(candidate)]
    print(candidate + ": " + str(round(float(numvotes)/float(numrows)*100, 3)) + "% (" + str(numvotes) + ")") # Calculate vote percentage
print("-------------------------")
print("Winner: " + str(candidates[votecounts.index(max(votecounts))])) # Display candidate with matching index to the max votecount
print("-------------------------")