import os
import csv 

pybank_file = os.path.join("Resources", "03-Python_Homework_PyBank_Resources_budget_data (1).csv")

with open(pybank_file, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)
    
    csv_header = next(csvreader)
    
    print(f"CSV Header: {csv_header}")

    num_rows = 0
    total = 0


    for row in csvreader:
        num_rows += 1
        total += int(row[1])

        
print("Financial Analysis")
print("-------------------------------------")

Average_Change = int(total / num_rows)
Greatest_Increase = max(row[1])
Greatest_Decrease = min(row[1])
#Greatest_Increase_Month = Greatest_Increase(row[0])
#Greatest_Decrease_Month = Greatest_Decrease(row[0])


print("Total Months: " + str(num_rows))
print("Total: " + "$" + str(total))
print("Average Change: " + str(Average_Change))
print("Greatest Increase in Profits: " + str(Greatest_Increase))
print("Greatest Decrease in Profits: " + str(Greatest_Decrease))