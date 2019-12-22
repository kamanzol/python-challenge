import os
import csv

csvpath = os.path.join('/Users/kamanzol/Desktop/python-challenge/PyPoll/electiondata.csv')

VotesCast = 0
Candidates = [] 
PercentageVotes = []
TotalVotes = []

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",") 

    header = next(csvreader) 

    for row in csvreader: 

        VotesCast = VotesCast + 1

        if row[2] not in Candidates:
            Candidates.append(row[2])
            index = Candidates.index(row[2])
            TotalVotes.append(1)
        else:
            index = Candidates.index(row[2])
            TotalVotes[index] += 1
    
    for x in range(len(Candidates)):
        PercentageVotes = round((TotalVotes[x]/VotesCast)*100,3)
    
    winner = max(TotalVotes)
    index = TotalVotes.index(winner)
    Winner = Candidates[index]

print("Election Results")
print("--------------------------")
print(f"Total Votes: {int(VotesCast)}")
print("--------------------------")
for i in range(len(Candidates)):
    print(f"{Candidates[x]}: {PercentageVotes}% ({TotalVotes[x]})")

print("--------------------------")
print(f"Winner: {Winner}")
print("--------------------------")

