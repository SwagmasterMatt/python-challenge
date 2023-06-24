import os
import csv
import numpy as np

#Create the initial lists
headers = []
Difference = []
Date = []
Profit = []

#Create a variable for the path to the CSV
BudgetPath = os.path.join('Resources', 'budget_data.csv').replace("\\","/")

#Read the CSV and store the headers and the data into lists
with open(BudgetPath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader)
    for row in csvreader:
        #add Dates to list
        Date.append(row[0])
        #add Profit to list
        Profit.append(row[1])

#Loop through the Profit List and calculate the difference values then store them
for i in range(len(Profit) - 1):
    Diff = int(Profit[i+1]) - int(Profit[i])
    Difference.append(int(Diff))
    #print(Difference[i]) - Delete Later


#Calculate Results
#Total = sum(int(Profit))
Great_Inc = max(Difference)
Great_Inc_Pos = Difference.index(Great_Inc)
Great_Inc_Dt = Date[Great_Inc_Pos]
Great_Dec = min(Difference)
Great_Dec_Pos = Difference.index(Great_Dec)
Great_Dec_Dt = Date[Great_Dec_Pos]
Avg_Chg = round(np.mean(Difference),2)
Total_Months = len(Date)

print("Financial Analysis" + "\n\n-------------------\n")
print("Total Months: " + str(Total_Months))
print("\n")
#print("Total: $" + str(Total))
print("\n")
print("Average Change: $" + str(Avg_Chg))
print("\n")
print("Greatest Increase in Profits: " + str(Great_Inc_Dt) + " ($"+ str(Great_Inc) + ")")
print("\n")
print("Greatest Increase in Profits: " + str(Great_Dec_Dt) + " ($"+ str(Great_Dec) + ")")