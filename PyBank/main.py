
 # import modules
import os; import csv

# load up the required file
budgetpath = os.path.join("Resources", "budget_data.csv")

#output the file
outputFile = os.path.join("Analysis", "BudgetAnalysis.txt")

#variables
totalMonth = 0
totalNet = 0
change = []
date = []

#open the file and read it
with open(budgetpath, 'r') as budgetFile:

    #create a reader
    csvreader = csv.reader(budgetFile)

    #read header row
    header = next(csvreader)

    #move to first row
    firstrow = next(csvreader)    

    #increment total month count
    totalMonth += 1

    # add on to the total budget
    totalNet += float(firstrow[1])

    #establish initial budget
    initialbudget = float(firstrow[1])

    
    for row in csvreader:
        #increment total month count
        totalMonth += 1

        # add on to the total budget
        totalNet += float(row[1])

        #calculate net change
        netchange = float(row[1]) - initialbudget
        # add on to the change list
        change.append(netchange)

        # add the first month a change occured
        date.append(row[0])


        #update initial budget
        initialbudget = float(row[1])

#average net change per month
averagechange = sum(change) / len(change)

greatestIncrease = [date[0], change[0]]
greatestDecrease = [date[0], change[0]]

# use loop to calculate the index of the greatest and least changes
for m in range(len(change)):
    #calculate greatest increase & decrease
    if (change[m] > greatestIncrease[1]):
        # if the value is greater than the greatest increase, it becomes new increase
        greatestIncrease[1] = change[m]
        #update the month
        greatestIncrease[0] = date[m]
    
    if (change[m] < greatestDecrease[1]):
        # if the value is less than the greatest decrease, it becomes new decrease
        greatestDecrease[1] = change[m]
        #update the month
        greatestDecrease[0] = date[m]

#start generating the output
output = (
    f"\nFinancial Data Analysis \n"
    f"----------------------------\n"
    f"Total Months: {totalMonth}\n"
    f"Total Budget: ${totalNet:.2f}\n"
    f"Average Change: ${averagechange:.2f}\n"
    f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]:.2f})\n"
    f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]:.2f})"
)

#print output
print(output)

#export to text file
with open(outputFile, 'w') as textFile:
    textFile.write(output)



        

