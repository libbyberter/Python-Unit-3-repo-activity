import os
import csv

# Path to collect data from the Resources folder
graduation_csv = os.path.join("08-Par_GraduatingFunctions","Resources","graduation_data.csv")


# Define the function and have it accept the 'state_data' as its sole parameter
def print_percentages(state_data):
    #print(state_data[0])

# Find the total students
    total_students = int(row[1]) + int(row[3]) + int(row[5])
    #print(total_students)

# Find the total graduates
    total_grads = int(row[2]) + int(row[4]) + int(row[6])
    #print(total_grads)

# Find the public school graduation rate
    if int(row[1]) > 0:
        public_perc = round(int(row[2])/int(row[1])*100,2)
        #print(public_perc)

# Remember that some states do not have nonprofit or forprofit private schools
# Find the non-profit school graduation rate
    if int(row[3]) > 0:
        nonprofit_perc = round(int(row[4])/int(row[3])*100,2)
        #print(nonprofit_perc)

# Find the for-profit school graduation rate
    if int(row[3]) > 0:
        forprofit_perc = round(int(row[6])/int(row[5])*100,2)
        #print(forprofit_perc)

# Calculate the overall graduation rate
    total_rate = round(total_grads/total_students*100,2)
    #print(total_rate)
    if total_rate >= 50:
        text = "Graduation success!"
    else:
        text = "State needs improvement"

# Print out the state's name and its graduation rates
 
    print(f"The graduation rate for public schools is {public_perc}%,")
    print(f"non-profit schools is {nonprofit_perc}%,")
    print(f"and for-profit schools is {forprofit_perc}%")
    print()
    print(f"{row[0]} has an overall graduation rate of {total_rate}%  -->  {text} ")

# Read in the CSV file
with open(graduation_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what state they would like to search for
    state_to_check = input("What state do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the state's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if state_to_check == row[0]:
            print_percentages(row)
