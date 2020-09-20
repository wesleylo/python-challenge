import csv
import os


csvpath = os.path.join('Resources', 'budget_data.csv')

print(csvpath)

numrows = 0
total = 0

topprofit = ['', 0]
toploss = ['', 0]

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    headers = next(csvreader)
    print(headers)

    for row in csvreader:
        print(row)
        
        current = int(row[1])

        numrows += 1
        total += current

        if current > topprofit[1]:
            topprofit[0] = row[0]
            topprofit[1] = current
            print(topprofit[0])

        if current < toploss[1]:
            toploss[0] = row[0]
            toploss[1] = current
            print(toploss[0])    

print("Total Months: " + str(numrows))
print("Total: $" + str(total))
print("Greatest Increase in Profits: " + topprofit[0] + " (" + str(topprofit[1]) + ")")
print("Greatest Decrease in Profits: " + toploss[0] + " (" + str(toploss[1]) + ")")