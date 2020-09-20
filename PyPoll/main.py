import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv') # ./Resources/election_data.csv

numrows = 0
total = 0

topprofit = ['', 0]
toploss = ['', 0]

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    headers = next(csvreader) # Store the header row
    print(headers)

    for row in csvreader:
        numrows += 1 # Iterate numrows
        
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(numrows))
print("-------------------------")