
# Imports Listing
import os
import csv
import numpy as np

#filepath where csv file resides
csvfilepath = 'C:\GitRepos\python-challenge\PyBank\Resources\Budget_data.csv'


# Set up lists to store CSV Data split out
Date = []
ProfitLosses = []

with open(csvfilepath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)

        # Add Date Data
        Date.append(row[0])

        # Add Profit Loss Data
        ProfitLosses.append(row[1])

# Review Split out Lists
print(Date)
print(" ")    
print(ProfitLosses)
print(" ")
print(" ")

#Convert List to Integers
ProfitLosses = list(map(int, ProfitLosses))


######################
# Calculate Values
######################

#Find Count of Total Months - GOOD 
CountMonths = len(Date)

#Find Net Profit/Loss  - GOOD
TotalProfit = sum(ProfitLosses)

#Cacluate change in Profit/Loss for entire Period - GOOD 
  # Calculating change in profits month-to-month
Change_Profits = []
for x, y in zip(ProfitLosses[0::], ProfitLosses[1::]):
    Change_Profits.append(y-x)
      
# printing change in profits month-to-month
#print ("Change_Profits: ", str(Change_Profits))

#Change in Profits Month to month - GOOD
ChangeInProfit = sum(Change_Profits)

#Calculate Average Change in Profit/Loss - GOOD
AvgProfit = str(round((ChangeInProfit/(CountMonths-1)), 2))

#Identify Greatest Profit Increase  - GOOD
MaxProfit = max(ProfitLosses)

#Identify Greatest Profit Decrease  - GOOD
MinProfit = min(ProfitLosses)


######################
# Print To Terminal
######################
#Print Variables to Terminal 
print(f"Total Months: {CountMonths}")
print(f"Net Total Profit: {TotalProfit}")
print(f"Average Change: {AvgProfit}")
print(f"Greatest Increase In Profits: {MaxProfit}")
print(f"Greatest Decrease In Profits: {MinProfit}")
print(" ")
print(" ")


######################
# Generate Text File
######################

#Setting Filepath manually due to issues 
#print(os.path.abspath(os.getcwd()))
currentpath=(os.path.abspath(os.getcwd()))
resultfilepath=(currentpath+'\Resources\Results.txt')
print(f"Writing file to following location: {resultfilepath} ")

f = open(resultfilepath, 'w')
f.write(f"Total Months: {CountMonths}")
f.write('\n')
f.write(f"Net Total Profit: {TotalProfit}")
f.write('\n')
f.write(f"Average Change: {AvgProfit}")
f.write('\n')
f.write(f"Greatest Increase In Profits: {MaxProfit}")
f.write('\n')
f.write(f"Greatest Decrease In Profits: {MinProfit}")
f.close()