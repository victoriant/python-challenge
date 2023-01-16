#Budget Data Homework

import os
import csv

#Header
print("Financial Analysis")

#Spacing

print("-----------------------------------------------------------------")

csvpath = os.path.join('..', 'Resources', 'budget_data.csv') 

month_sum = []
profits = []
profit_change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        month_sum.append(row[0])

        profits.append(int(row[1]))    
    
# The total number of months included in the dataset

    print(f"Total Months: {len(month_sum)}")

# The net total amount of "Profit/Losses" over the entire period

    print(f"Total: ${sum(profits)}")

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
    for i in range(len(profits)-1):
        profit_change.append(profits[i+1]-profits[i])

    print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")

# The greatest increase in profits (date and amount) over the entire period

max_profits = max(profit_change)

max_increased_profits = profit_change.index(max(profit_change)) + 1

print(f"Greatest Increase in Profits: {month_sum[max_increased_profits]} (${(str(max_profits))})")

# The greatest decrease in profits (date and amount) over the entire period

min_profits = min(profit_change)

max_decreased_profits = profit_change.index(min(profit_change)) + 1

print(f"Greatest Decrease in Profits: {month_sum[max_decreased_profits]} (${(str(min_profits))})")

#  final script should both print the analysis to the terminal and export a text file with the results

output = ("Financial Analysis\n"
f"------------------------------------------\n"
f"Total Months: {len(month_sum)}\n"
f"Total: ${sum(profits)}\n"
f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}\n"
f"Greatest Increase in Profits: {month_sum[max_increased_profits]} (${(str(max_profits))})\n"
f"Greatest Decrease in Profits: {month_sum[max_decreased_profits]} (${(str(min_profits))})\n")

#print(output)

output_file = os.path.join("budget_data_final.csv")

with open(output_file, "w") as analysis:
    
    analysis.write(output)
