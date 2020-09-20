import csv
import os

csvpath = os.path.join('Resources', 'budget_data.csv') # ./Resources/budget_data.csv

numrows = 0
total = 0

net_change = []
net_change_months = 0

topprofit = ['', 0]
toploss = ['', 0]

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    headers = next(csvreader) # Store the header row
    previous = 0

    first = next(csvreader)[1] # First profit/loss
    numrows += 1
    previous = int(first)
    total += previous

    for row in csvreader:
        current = int(row[1])
        
        numrows += 1 # Iterate numrows
        total += current # Sum total

        # The average of the changes in "Profit/Losses" over the entire period
        current_net = current - previous
        previous = current
        net_change.append(current_net)
        net_change_months += 1

        if current > topprofit[1]: # Calculate greatest increase in profits
            topprofit[0] = row[0]
            topprofit[1] = current_net

        if current < toploss[1]: # Calculate greatest decrease in profits
            toploss[0] = row[0]
            toploss[1] = current_net

printlist = [
    "Financial Analysis",
    "----------------------------",
    "Total Months: " + str(numrows),
    "Total: $" + str(total),
    "Average Change: $" + str("{:.2f}".format(float(sum(net_change)) / float(net_change_months))), # Calculate float avg and format to 2 ndigits
    "Greatest Increase in Profits: " + topprofit[0] + " ($" + str(topprofit[1]) + ")",
    "Greatest Decrease in Profits: " + toploss[0] + " ($" + str(toploss[1]) + ")"
]

f = open(os.path.join('analysis', "anaysis.txt"), "w+") # Open and overwrite or create file

for row in printlist:
    print(row)
    f.write(row + "\n")

f.close()