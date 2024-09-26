#LAB3

import csv

#function for the serial search
def serial_search(file_name, target_date):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for y in reader:
            if y[0] == target_date:
                #return profit/losses for the target date
                return y[1]
    #return None if the target date is not found         
    return None

#function for the binary search
def binary_search(file_name, target_date):
    #read the CSV file and sort the data
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for y in reader:
            data.append(y)
    #sort the data by date        
    data.sort(key=lambda x: x[0])  

    #binary search
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid][0] == target_date:
            #return profit/losses for the target date
            return data[mid][1]  
        elif data[mid][0] < target_date:
            low = mid + 1
        else:
            high = mid - 1
    #return None if the target date is not found        
    return None 

#main function
def main():
    file_name = 'budget_data.csv'
    target_date = input("Enter the target date: ")

    print("Serial Search:")
    result = serial_search(file_name, target_date)
    if result is not None:
        print(f'Profit/losses for {target_date}: {result}')
    else:
        print(f'{target_date} not found in the file')

    print("\nBinary Search:")
    result = binary_search(file_name, target_date)
    if result is not None:
        print(f'Profit/losses for {target_date}: {result}')
    else:
        print(f'{target_date} not found in the file')

main()