import os
import csv
import numpy

headers = []
VoterID = []
County = []
Candidate = []

#Create a variable for the path to the CSV
PollPath = os.path.join('Resources', 'election_data.csv').replace("\\","/")

#Read the CSV and store the headers and the data into lists
with open(PollPath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader)
    for row in csvreader:
        #add voters to list
        VoterID.append(row[0])
        #add counties to list
        County.append(row[1])
        #add candidates to list
        Candidate.append(row[2])

#Store Candidate names and county names. Also calcuates votes per county... for fun (because gerrymandering is real)
Candidate_Names = list(set(Candidate))
Candidate_Names = sorted(Candidate_Names)
County_Names = list(set(County))
County_Ranges = []
CountyVotes = []
for CN in County_Names:
    CountyIndex = []
    for i in range(len(County)):
        if County[i] == CN:
            CountyIndex.append(i)
    
    Start = min(CountyIndex)
    End = max(CountyIndex)
    County_Ranges.append(CN)
    County_Ranges.append(Start)
    County_Ranges.append(End)

    
    CountyVotes.append(CN)
    for CD in Candidate_Names:
        Add = 0
        for i in range(Start, End):
            if Candidate[i] == CD:
                Add = Add + 1
        CountyVotes.append(CD)
        CountyVotes.append(Add)

#Calculates the winner and creates the report
Winner = 0    
Report = "Election Results \n\n---------------------------\n\n"\
"Total Votes: " + str(len(Candidate)) + "\n\n---------------------------\n\n"

for i in range(len(Candidate_Names)):
    VotePerc = Candidate.count(Candidate_Names[i])/len(Candidate)*100
    RndVt = round(VotePerc,3)
    Report += Candidate_Names[i] + ": " + str(RndVt) + "% " +"(" + str(Candidate.count(Candidate_Names[i])) + ")\n\n"
    
    #Determines the winner
    if Candidate.count(Candidate_Names[i]) > Winner:
        Winner = Candidate.count(Candidate_Names[i])
        WinnerRep = "Winner: " + Candidate_Names[i]

Report += "\n\n---------------------------\n\n" + WinnerRep + "\n\n---------------------------\n\n"

#Print to terminal
print(Report)

#Create the txt file and write the text
txt_file_path = os.path.join('analysis','text-file.txt').replace("\\","/")

with open(txt_file_path, 'w') as file:
    file.write(str(Report))
