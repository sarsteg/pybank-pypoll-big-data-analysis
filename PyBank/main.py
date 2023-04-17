# Import libraries
import os
import csv

#-----------------------------------------

# Tell the script where the data is located
CSV_PATH = os.path.join("Resources", "budget_data.csv")

# Change the working directory to the location of the script
#print(os.getcwd())
#print(__file__)
os.chdir(os.path.dirname(os.path.realpath(__file__)))
#print(os.getcwd())

#-----------------------------------------

def print_percentages(csv_reader):

    # Make variables global when needed
    first_row = True

    global change
    global count_months
    global net_total
    global count_changes
    global sum_changes
    global greatest_increase
    global greatest_increase_date
    global greatest_decrease
    global greatest_decrease_date

    change = 0
    count_months = 0
    net_total = 0
    count_changes = 0
    sum_changes = 0
    greatest_increase = 0
    greatest_increase_date = ""
    greatest_decrease = 0
    greatest_decrease_date = ""

    # Loop through the table
    for row in csv_reader:
        # Count the number of months included in the dataset
        count_months += 1

        # Calculate the net total amount of "Profit/Losses" over the entire period
        net_total += int(row["Profit/Losses"])

        # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        if first_row: #If row is the first row, then we need to skip b/c not possible to change without previous month
            previous_month = int(row["Profit/Losses"]) # Log previous month for prep
            first_row = False # Only skip the first row of the data
        else:
            current_month = int(row["Profit/Losses"])
            change = current_month - previous_month
            previous_month = current_month # Prep for next row
            #print(change)

            # Gather variables need to find the average
            count_changes += 1
            sum_changes += change
            # We will use these variables later when we have calculated everything to find the average change

        # Greatest increase in profits (date and amount) over the entire period
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = row["Date"]

        # Greatest decrease in losses (date and amount) over the entire period
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = row["Date"]

    return (count_months, net_total, sum_changes, count_changes, greatest_increase_date, greatest_increase, greatest_decrease_date, greatest_decrease)

#-----------------------------------------        

with open(CSV_PATH) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Keep header row becausing using DictReader
    # Note: The header row IS SAVED as the key for each row. 
    #header = next(csv_reader)
    #print(header)

    #row = next(csv_reader)
    #print(type(next(csv_reader)))

    # Run the function defined above with the csv file
    print_percentages(csv_reader)

#-----------------------------------------

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {count_months}") 
print(f"Total: ${net_total}")
print(f"Average Change: ${sum_changes/count_changes:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export a text file with the results
output_path = os.path.join("Analysis", "PyBank.txt")
with open(output_path, "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("----------------------------\n")
    text_file.write(f"Total Months: {count_months}\n")
    text_file.write(f"Total: ${net_total}\n")
    text_file.write(f"Average Change: ${sum_changes/count_changes:.2f}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

