#Bank challenge

#import os so file paths can be read across operating systems, import the module for reading CSV files
import os
import csv

#create the relative path to the CSV file we want to work in
csvpath = 'PyBank\Resources/budget_data.csv'

#Open the file for reading only, specify a comma as a delimiter
with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip he first row of data with column headers for all future calculations
    next(csvreader, None)

#Make and store 2 lists in python of the data from the CSV file
#I took this approach because in programing this, executing each data pull needed me to reopen the csv file before every pull. This lets me pull and store what I need once for all future pulls.
    date =[]
    profit_loss =[]
    for row in csvreader:
        date.append(row[0])
        profit_loss.append(row[1])

#First output: Total Months
#Find the number of months using the date list
row_count: int
row_count = len(date)

#Second output: Total $
#Calculate the total sum of profit and loss. First convert all values in the profit loss list to integers. Then sum the list and create a new variable.
profit_loss = [eval(i) for i in profit_loss]
total_sum=sum(profit_loss)

#Third output: Average Change
#Make a new list for the profit changes from month to month
pl_change_list=[]
i=0
#Use a while loop to go through the profit/loss list of data and subtract the next value in the list from the value before it, this will itterate one less than the total row count so there is not an excess value at the end 
while i < row_count-1:
    pl_change_list.append(int(profit_loss[i+1])-int(profit_loss[i]))
    i +=1
#Calc the average change in profit / loss using the new list
pl_change= sum(pl_change_list[:])/len(pl_change_list)

#Fourth and fith output: Greatest increase and decrease in profits
#make a new list called date_change. This will copy the values in the date list and then remove the first entry. Now each date will correctly correspond to when changes in profit occured.
date_change=list(date)
date_change.pop(0)
#find the min and max values for profit increases and decreases using the profitability change list.
max_profit=max(pl_change_list)
min_profit=min(pl_change_list)

#set the row index for each min and max value
max_index=pl_change_list.index(max(pl_change_list))
min_index=pl_change_list.index(min(pl_change_list))
#set the dates of each change based on the index number
max_date=date_change[max_index]
min_date=date_change[min_index]

#print all outputs into the terminal.   
print("Financial Analysis" +
      "\n" +
      "----------------------------"
      "\n"
      "Total Months: " + str(row_count) +
      "\n" +
      "Total: $" + str(total_sum) +
      "\n" +
      "Average Change: $" + str(round(pl_change,2)) +
      "\n" +
      "Greatest Increase in Profits: " + max_date +" ($" + str(max_profit) + ")" +
      "\n" +
      "Greatest Decrease in Profits: " + min_date + " ($" + str(min_profit) + ")")

#Export a text file of the written output, that exports to the Analysis folder in PyBank
with open('PyBank/Analysis/financial_analysis.txt','w') as f:
    f.write("Financial Analysis" +
            "\n" +
            "----------------------------"
            "\n"
            "Total Months: " + str(row_count) +
            "\n" +
            "Total: $" + str(total_sum) +
            "\n" +
            "Average Change: $" + str(round(pl_change,2)) +
            "\n" +
            "Greatest Increase in Profits: " + max_date +" ($" + str(max_profit) + ")" +
            "\n" +
            "Greatest Decrease in Profits: " + min_date + " ($" + str(min_profit) + ")")
            
