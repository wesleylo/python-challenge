import csv
import os

csvpath = os.path.join('Resources', 'budget_data.csv') # ./Resources/budget_data.csv

numrows = 0
total = 0

topprofit = ['', 0]
toploss = ['', 0]

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    headers = next(csvreader) # Store the header row

    for row in csvreader:
        current = int(row[1])

        numrows += 1 # Iterate numrows
        total += current # Sum total

        if current > topprofit[1]: # Calculate greatest increase in profits
            topprofit[0] = row[0]
            topprofit[1] = current

        if current < toploss[1]: # Calculate greatest decrease in profits
            toploss[0] = row[0]
            toploss[1] = current 

printlist = [
    "Financial Analysis",
    "----------------------------",
    "Total Months: " + str(numrows),
    "Total: $" + str(total),
    "Average Change: $" + str(round(float(total)/float(numrows), 2)), # Calculate float avg and round to 2 ndigits
    "Greatest Increase in Profits: " + topprofit[0] + " ($" + str(topprofit[1]) + ")",
    "Greatest Decrease in Profits: " + toploss[0] + " ($" + str(toploss[1]) + ")"
]
print(printlist)
for row in printlist:
    print(row)

# print("Financial Analysis")
# print("----------------------------")
# print("Total Months: " + str(numrows))
# print("Total: $" + str(total))
# print("Average Change: $" + str(round(float(total)/float(numrows), 2))) # Calculate float avg and round to 2 ndigits
# print("Greatest Increase in Profits: " + topprofit[0] + " ($" + str(topprofit[1]) + ")")
# print("Greatest Decrease in Profits: " + toploss[0] + " ($" + str(toploss[1]) + ")")


f = open(os.path.join('analysis', "anaysis.txt"), "w+")