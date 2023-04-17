# Import modules
import os
import csv

# Tell the script where the data is located
CSV_PATH = os.path.join("Resources", "election_data.csv")

# Change the working directory to the location of the script
os.chdir(os.path.dirname(os.path.realpath(__file__)))


def analyze_votes(election_data)
# Total number of votes cast


# Complete list of candidates who received votes

# Percentage of votes each candidate won

# Total number of votes each candidate won

# Winner of the election based on popular vote


# Run function on data
with open(CSV_PATH) as csv_file:
    election_data = csv.DictReader(csv_file)
    analyze_votes(election_data)


# Print the analysis to the terminal
print("Election Results")
# Export a text file with the results