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
        Profit.append(int(row[1]))

#Loop through the Profit List and calculate the difference values then store them
for i in range(len(Profit) - 1):
    Diff = Profit[i+1] - Profit[i]
    Difference.append(int(Diff))


#Calculate Results
Total_Months = len(Date)
Total = sum(Profit)
Great_Inc = max(Difference)
Great_Inc_Pos = Difference.index(Great_Inc)
Great_Inc_Dt = Date[Great_Inc_Pos + 1]
Great_Dec = min(Difference)
Great_Dec_Pos = Difference.index(Great_Dec)
Great_Dec_Dt = Date[Great_Dec_Pos + 1]
Avg_Chg = round(np.mean(Difference),2)

#store the text for the output into a variable
Report = "Financial Analysis" + "\n\n-------------------\n\n" \
"Total Months: " + str(Total_Months) +"\n\n" \
"Total: $" + str(Total) + "\n\n" \
"Average Change: $" + str(Avg_Chg) + "\n\n" \
"Greatest Increase in Profits: " + str(Great_Inc_Dt) + " ($"+ str(Great_Inc) + ")" + "\n\n" \
"Greatest Increase in Profits: " + str(Great_Dec_Dt) + " ($"+ str(Great_Dec) + ")"

#print to terminal
print(Report)

#Create the txt file and write the text
txt_file_path = os.path.join('analysis','text-file.txt').replace("\\","/")

with open(txt_file_path, 'w') as file:
    file.write(str(Report))