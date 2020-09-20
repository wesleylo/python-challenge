import csv
import os


csvpath = os.path.join('Resources', 'budget_data.csv')

print(csvpath)

numrows = 0
total = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    headers = next(csvreader)
    print(headers)

    for row in csvreader:
        print(row)
        
        numrows += 1
        total += int(row[1])

print("Total Months: " + str(numrows))
print("Total: " + str(total))