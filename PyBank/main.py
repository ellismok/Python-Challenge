# Create file path across os 
import os
# Read CSV files
import csv
# Read csv file by using pathlib.Path
csvpath = os.path.join("Resources", "budget_data.csv")
    
# Lists to store column data 
months = []
balance = []
difference_balance = []

# Continue by using with open() as csvfile:
with open(csvpath) as csvfile:
    # Use CSV reader ('r') to read csv and specify delimiter
    bank_data = csv.reader(csvfile, delimiter=',')
    # print (bank_data)

    # Read the header row first --> this allows us to skip the first row 
    csv_header = next(bank_data)    # print(f"CSV Header: {csv_header}") --> CSV Header: ['Date', 'Profit/Losses']
    # Create first_row to calculate change_balance in the future --> x[-1] cannot be read bc in [2,3,4] cannot be 2 minus nothing. 
    first_row = next(bank_data)     # print(f"First Row: {first_row}") --> First Row: ['Jan-2010', '867884']
    
    # Use .append() to add months column = first_row[0] to months list = months [] WHEREAS first_row[1] to Prfoit/Losses column = balance []
    months.append(first_row[0])
    balance.append(int(first_row[1])) # Use int() to make integer

    # Use the For Loop to read each row in our data
    for row in bank_data:
        # print(row) # For Loop starts from ['Feb-2010', '984655'] NOT ['Jan-2010', '867884']
        months.append(row[0]) # Starts at ['Feb-2010', '-']
        previous_balance = balance[-1] # Prints starting with ['-', '867884'] NOT header bc balance.append(int(first_row[1])) is defined
        balance.append(int(row[1])) # Starts at ['-', '984655']
        # print("I'm currently appending " + row[1]) # I'm currently appending 984655, I'm currently appending 322013
        # print(balance) # [867884, 984655], [867884, 984655, 322013]
        # print("Last loop I appended " + row[1]) # Last loop I appended 984655, Last loop I appended 322013
        difference_balance.append(int(row[1])-previous_balance)  # Current appended - last appended

# Find the "total number of months" included in the dataset 
    Total_Months = len(months)

    Difference_Total_Months = len(months) - 1 
    
#the net total amount of "Profit/Losses" over the entire period
    Total_Balances = sum(balance)
    Format_Total_Balances = "${:,}".format(Total_Balances)

    Difference_Total_Balances = sum(difference_balance)

#the average of the changes in "Profit/Losses" aka "Balance" over the entire period
    Net_Total = Difference_Total_Balances / Difference_Total_Months
    Format_Net_Total = "${:,.2f}".format(Net_Total)

# the greatest increase in profits (date and amount) over the entire period
    Max_Difference_Balance_Amount = max(difference_balance) # find the max() in difference_balance
    Max_Difference_Balance_Index = difference_balance.index(Max_Difference_Balance_Amount) # find the spot/index of max(difference_balance) using .index()
    Format_Max_Difference_Balance_Amount = "${:,}".format(Max_Difference_Balance_Amount)

    Max_Balance_Date = months[Max_Difference_Balance_Index + 1] # use the new found index + 1 to find the date in the column: months[x]

# #the greatest decrease in losses (date and amount) over the entire period
    Min_Difference_Balance_Amount = min(difference_balance) # find the min() in difference_balance
    Min_Difference_Balance_Index = difference_balance.index(Min_Difference_Balance_Amount) # same as line 54
    Format_Min_Difference_Balance_Amount = "${:,}".format(Min_Difference_Balance_Amount)

    Min_Balance_Date = months[Min_Difference_Balance_Index + 1] # same as line 56

# save file as textfile
output = ("Financial Analysis\n"
"----------------------------\n"
f"Total Months: {Total_Months}\n"
f"Total: {Format_Total_Balances}\n"
f"Average Change: {Format_Net_Total}\n"
f"Greatest Increase in Profits: {Max_Balance_Date} ({Format_Max_Difference_Balance_Amount})\n"
f"Greatest Decrease in Profits: {Min_Balance_Date} ({Format_Min_Difference_Balance_Amount})\n")

print(output)
#save as txt file
with open('Bank_Data_Analysis.txt', 'w') as txtfile:
    txtfile.write(output)