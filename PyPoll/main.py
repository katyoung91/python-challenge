#Bank challenge

#import os so file paths can be read across operating systems, import the module for reading CSV files
import os
import csv

#import default ditionnary from collections that will be used to create a ditctionary of candidate names and their vote counts
from collections import defaultdict

#create the relative path to the CSV file we want to work in

csvpath = 'PyPoll\Resources/election_data.csv'

#Open the file for reading only, specify a comma as a delimiter
with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Skip he first row of data with column headers for all future calculations
    next(csvreader, None)

#Create a list using the last column from the CSV file that will be used to caluclate the votes by cadidate in the program
    candidates=[]
    for row in csvreader:
        candidates.append(row[2])

#First Output: Total Votes
total_vote=0
for row in candidates:
    total_vote +=1


#Second Output: Cadidates, their vote % and vote count
#Create a dictionnary with defaultdic that will store our candidate names and their vote counts
candidates_votes= defaultdict(int)

#For loop that cycles through the candidate list storing each candidate name and their total vote count
for person in candidates:
    candidates_votes[person]+=1    

#Create a string that will store the text output for the candidate names, % of vote and vote count
can_vote_str = ''

#Using a for loop, iterate through the dictionary and store in the string the name of each candidate, the calculated % of their vote and formatted out to 3 decimal places and their vote count
#Note that the last entry has a "\n" at the end, so one will not be needed in the later print out and text file export
for person in candidates_votes:
    can_vote_str= can_vote_str + (str(person) +": " + str(("%.3f" % (candidates_votes[person]/total_vote*100))) + "% (" + str(candidates_votes[person])+ ") \n")


#Third Output: Winner of the Election
#Find the max value in the candidates_votes dictionary and store the value
max_value=max(candidates_votes.values())
#Pull the key for the person with the most number of votes (max_value) using filter() and lambda
winner = list(filter(lambda x: candidates_votes[x] == max_value, candidates_votes))[0]
  

#print all outputs into the terminal.   
print("Election Results" +
      "\n"+
      "----------------------------"+
      "\n"+
      "Total Votes: " + str(total_vote) +
      "\n"+
      "----------------------------" +
      "\n"+
      str(can_vote_str)+
      "----------------------------"+
      "\n"+
      "Winner: "+ str(winner) +
      "\n"+"----------------------------")

#Export a text file of the written output that exports to the Analysis folder in PyPoll
with open('PyPoll/Analysis/election_results.txt','w') as f:
    f.write("Election Results" +
      "\n"+
      "----------------------------"+
      "\n"+
      "Total Votes: " + str(total_vote) +
      "\n"+
      "----------------------------" +
      "\n"+
      str(can_vote_str)+
      "----------------------------"+
      "\n"+
      "Winner: "+ str(winner) +
      "\n"+"----------------------------")