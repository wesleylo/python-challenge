import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv') # ./Resources/election_data.csv

numrows = 0
candidates = []
votecounts = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    headers = next(csvreader) # Store the header row

    for row in csvreader:
        currentcandidate = row[2]
        numrows += 1 # Iterate numrows
        if not currentcandidate in candidates: # currentcandidate does not appear in candidates
            candidates.append(currentcandidate)
            votecounts.append(0)

        votecounts[candidates.index(currentcandidate)] += 1 # Find index of current candidate and iterate corresponding votecount

printlist = [
    "Election Results",
    "-------------------------",
    "Total Votes: " + str(numrows),
    "-------------------------"
]
for candidate in candidates:
    numvotes = votecounts[candidates.index(candidate)]
    printlist.append(candidate + ": " + str(round(float(numvotes)/float(numrows)*100, 3)) + "% (" + str(numvotes) + ")") # Calculate vote percentage for each candidate
printlist.extend([
    "-------------------------",
    "Winner: " + str(candidates[votecounts.index(max(votecounts))]), # Display candidate with matching index to the max votecount
    "-------------------------"]
)

f = open(os.path.join('analysis', "anaysis.txt"), "w+")

for row in printlist:
    print(row)
    f.write(str(row) + "\n")

f.close()