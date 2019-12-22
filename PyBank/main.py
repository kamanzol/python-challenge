import os
import csv

csvpath = os.path.join('/Users/kamanzol/Desktop/python-challenge/PyBank/budgetdata.csv')

TotalMonths = []
TotalProfLoss = []
ProfitChange = [] 

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",") 

    header = next(csvreader)  

    for row in csvreader: 

        TotalMonths.append(row[0])
        TotalProfLoss.append(int(row[1]))

    for i in range(len(TotalProfLoss)-1):
        
        ProfitChange.append(TotalProfLoss[i+1]-TotalProfLoss[i])
        
GreatestIncrease = max(ProfitChange)
GreatestDecrease = min(ProfitChange)

HighestMonth = ProfitChange.index(max(ProfitChange)) + 1
LowestMonth = ProfitChange.index(min(ProfitChange)) + 1 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(TotalMonths)}")
print(f"Total: ${sum(TotalProfLoss)}")
print(f"Average Change: {round(sum(ProfitChange)/len(ProfitChange),2)}")
print(f"Greatest Increase in Profits: {TotalMonths[HighestMonth]} (${(str(GreatestIncrease))})")
print(f"Greatest Decrease in Profits: {TotalMonths[LowestMonth]} (${(str(GreatestDecrease))})")
