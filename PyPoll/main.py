
# Imports Listing
import os
import csv
import numpy as np

#filepath where csv file resides
csvfilepath = 'C:\GitRepos\python-challenge\PyPoll\Resources\election_data.csv'



# Set up lists to store CSV Data split out
VoterIDList = []
CountyList = []
CandidateList = []

with open(csvfilepath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)

         # Add VoterID
         VoterIDList.append(row[0])

         # Add County
         CountyList.append(row[1])

         # Add County
         CandidateList.append(row[2])    

# # Review Split out Lists
# print(VoterIDList)
# print(" ")    
# print(CountyList)
# print(" ")
# print(CandidateList)
# print(" ")
# print(" ")

# #Convert List to Integers
# ProfitLosses = list(map(int, ProfitLosses))


######################
# Calculate Values
######################

#Find Count of Total Votes - GOOD 
CountofVotes = len(VoterIDList)

#Find Distinct Candidates in Candidate List  - GOOD
DistinctCandidateList = []
for x in CandidateList:
    if x not in DistinctCandidateList:
        DistinctCandidateList.append(x)
#print(DistinctCandidateList)


#Cacluate Total Votes for each candidate - GOOD 
KhanVotes = CandidateList.count('Khan')
CorreyVotes = CandidateList.count('Correy')
LiVotes = CandidateList.count('Li')
OTooleyVotes = CandidateList.count("O'Tooley")

CandidateVoteCounts = [KhanVotes,CorreyVotes,LiVotes,OTooleyVotes]

# #Identify Highest Vote Count  - GOOD
HighestVoteCount = max(CandidateVoteCounts)

WinnerListing = {'Khan': KhanVotes, 'Correy': CorreyVotes, 'Li': LiVotes, 'OTooley': OTooleyVotes}
winner = max(WinnerListing, key=WinnerListing.get)
print(winner, 'won')

#Calculate Percentage for each Candidate
KhanPercent = str(round(((KhanVotes/(CountofVotes))*100.00), 2))
CorreyPercent = str(round(((CorreyVotes/(CountofVotes))*100.00), 2))
LiPercent = str(round(((LiVotes/(CountofVotes))*100.00), 2))
OTooleyPercent = str(round(((OTooleyVotes/(CountofVotes))*100.00), 2))






######################
# Print To Terminal
######################
#Print Variables to Terminal 
print(f"------------------------------")
print(f"Total of Votes: {CountofVotes}")
print(f"------------------------------")
print (f"Khan: {KhanPercent}%     Votes:  {KhanVotes}")
print (f"Correy: {CorreyPercent}%   Votes:  {CorreyVotes}")
print (f"Li: {LiPercent}%       Votes:  {LiVotes}")
print (f"O'Tooley: {OTooleyPercent}%  Votes:  {OTooleyVotes}")
# print(" ")
# print(" ")
print(f"------------------------------")
print(f"Winner: {CountofVotes}")
print(f"------------------------------")


######################
# Generate Text File
######################

#Setting Filepath manually due to issues 
#print(os.path.abspath(os.getcwd()))
currentpath=(os.path.abspath(os.getcwd()))
resultfilepath=(currentpath+'\Analysis\Results.txt')
print(f"Writing file to following location: {resultfilepath} ")

f = open(resultfilepath, 'w')
f.write(f"------------------------------")
f.write('\n')
f.write(f"Total of Votes: {CountofVotes}")
f.write('\n')
f.write(f"------------------------------")
f.write('\n')
f.write('\n')
f.write(f"Khan: {KhanPercent}%    Votes:  {KhanVotes}")
f.write('\n')
f.write(f"Correy: {CorreyPercent}%  Votes:  {CorreyVotes}")
f.write('\n')
f.write(f"Li: {LiPercent}%      Votes:  {LiVotes}")
f.write('\n')
f.write(f"O'Tooley: {OTooleyPercent}%  Votes:  {OTooleyVotes}")
f.write('\n')
f.write(f"------------------------------")
f.write('\n')
f.write(f"Winner: {winner}")
f.write('\n')
f.write(f"------------------------------")
f.write('\n')
f.close()
