#LAB3

import csv

#function to read CSV data 
def read_csv(file_name):
    data = []
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

#implementing the serial search algorithm
def serial_search(data, target_date):
    for record in data:
        if record['Date'] == target_date:
            return f"Profit/Losses for {target_date}: {record['Profit/Losses']}"
    return f"Date {target_date} not found."

#main function
def main():
    #file name
    file_name = 'budget_data.csv'
    
    #read data from CSV
    data = read_csv(file_name)
    
    #get user input for the target date
    target_date = input("Enter the date")
    
    #perform the serial search
    result = serial_search(data, target_date)
    
    #output the result
    print(result)

main()
