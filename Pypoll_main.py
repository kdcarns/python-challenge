import os
import csv 

pypoll_file = os.path.join("Resources", "03-Python_Homework_PyPoll_Resources_election_data.csv")

with open(pypoll_file, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)
    
    csv_header = next(csvreader)
    
    print(f"CSV Header: {csv_header}")

    num_rows = 0

    for row in open(pypoll_file):
        num_rows += 1

        khan_count = 0
    
    if row[3] == ('Khan'):
        khan_count += 1
        khan_percent = khan_count/num_rows
        khan_percentage = "{:.0%}".format(khan_percent)

    print("Election Results")
    print("---------------------------------------------")
    print("Total Votes: " + str(num_rows))
    print("---------------------------------------------")
    print("Khan: " + str(khan_percentage) + ("(") + str(khan_count) + (")")




