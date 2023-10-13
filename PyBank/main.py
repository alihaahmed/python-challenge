# Import modules
import os
import csv

# Set variables
total_months = 0
total_profit_loss = 0
monthly_profit_loss = []
monthly_change = []
date = []

# Set csv path
csvpath = 'Resources/budget_data.csv'

# Open CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Read header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# Total number of months included in the dataset
# Net total amount of "Profit/Loss" over the entire period
# Use for loop to iterate through rows to count months, sum the profit/loss over entire period and store each month's date and profit/loss in separate lists
    for row in csvreader:
        total_months += 1
        total_profit_loss += int(row[1])
        date.append(row[0])
        monthly_profit_loss.append(int(row[1]))

# Changes in "Profit/Loss" over the entire period and average of those changes
# Iterate through monthly_profit_loss list and use indexing to calculate change in profit/loss month over month; store monthly change in monthly_change list
# Calculate average change in profit/losses over entire period by summing each element in monthly_change list and dividing by length of monthly_change list
    for i in range(len(monthly_profit_loss)-1):
        change = monthly_profit_loss[i+1] - monthly_profit_loss[i]
        monthly_change.append(change)
    average_change = round((sum(monthly_change)/len(monthly_change)), 2)

# Use max() function to calculate greatest increase in profits (date and amount) over entire period
# Use .index() to determine index/position of greatest_increase value in monthly_change list; apply this index to date list to determine corresponding date
    greatest_increase = max(monthly_change)
    greatest_increase_date = date[monthly_change.index(greatest_increase)+1]
    
# Use min() function to calculate greatest decrease in profits (date and amount) over entire period
# Use .index() to determine index/position of greatest_decrease value in monthly_change list; apply this index to date list to determine corresponding date
    greatest_decrease = min(monthly_change)
    greatest_decrease_date = date[monthly_change.index(greatest_decrease)+1]

# Print analysis to terminal
# Loop through lines list to print analysis
lines = ["Financial Analysis", "----------------------------", f"Total Months: {total_months}", f"Total: ${total_profit_loss}", f"Average Change: ${average_change}", f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})", f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"]
for line in lines:
    print(line)

# Export text file with results
# Save output file path
# Open text file for writing
# Loop through lines list to write analysis to text file
output_file = 'Analysis/financial_analysis.txt'
with open('financial_analysis.txt', 'w') as text:
    for line in lines:
        text.write(line)
        text.write("\n")