# Import needed libraries
import os
import csv

#variables and lists needed to be established before loop
total_months = 0
net_total = 0
net_change_list = []
month_of_change =[]
greatest_increase = ["",0]
greatest_decrease = ["",0]

# Files to load and output (need to be changed if directory is changed)
csvpath = os.path.join("Resources", "budget_data.csv")

txtoutput = os.path.join("Resources", "Analysis.txt")

#opens and reads csv data
with open (csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # This accounts for moving the first row to second in order to calcualate the first average change within the following loop
    start_offset_for_changecal = next(csvreader)
    total_months += 1
    net_total += int(start_offset_for_changecal[1])
    prev_pl = int(start_offset_for_changecal[1])
    
    #loop through rows in csv
    for row in csvreader:

        #ID csv header contents
        date = str(row[0])
        profit_loss = int(row[1])

        #calculations for total months and total
        total_months += 1
        net_total += profit_loss

        #calculations for average net change and add amounts to lists
        net_change = (profit_loss - prev_pl)
        prev_pl = profit_loss
        net_change_list += [net_change]
        month_of_change += [date]

        average_change = sum(net_change_list) / len(net_change_list)

        # calculations for greatest increase and decrease
        if net_change > greatest_increase[1]:
            greatest_increase[0] = date
            greatest_increase[1] = net_change
        
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = date
            greatest_decrease[1] = net_change

#variable for output to save space            
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} $({greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} $({greatest_decrease[1]})\n")

#show results of Analysis
print(output)

#Export analysis to txt file
with open(txtoutput, "w") as txt_file:
    txt_file.write(output)