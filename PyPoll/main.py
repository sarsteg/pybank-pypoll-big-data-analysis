# Import modules
import os
import csv

#-----------------------------------------

# Tell the script where the data is located
CSV_PATH = os.path.join("Resources", "election_data.csv")

# Change the working directory to the location of the script
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#-----------------------------------------

# Define rows for dataset
candidate_col = 3

#-----------------------------------------

def analyze_votes(election_data):

# List of variables created in the code
global candidates
global total_votes
global candidate_0_count
global candidate_1_count
global candidate_2_count

candidates = ()
total_votes = 0
candidate_0_count = 0
candidate_1_count = 0
candidate_2_count = 0

# Loop through the table
for row in election_data:

    # Set the row's candidate
    current_candidate = row[candidate_col]

    # Who are the candidates?
    # Add candidate to set, sets only accept unique values
    # This will be used to find the complete list of candidates who received votes
    candidates.add(row[candidate_col])

    # Total number of votes cast
    # Each row is 1 vote
    total_votes += 1

    # Now that we are compiling the candidates, start tally for each candidate
    # Total number of votes each candidate won
    if candidates[0] == current_candidate:
        candidate_0_count += 1
    elif candidates[1] == current_candidate:
        candidate_1_count += 1
    elif candidates[2] == current_candidate:
        candidate_2_count += 1
    else:
        print("Error: Candidate not found")

    return candidates, total_votes, candidate_0_count, candidate_1_count, candidate_2_count

# Run function on data
with open(CSV_PATH) as csv_file:
    election_data = csv.reader(csv_file)
    analyze_votes(election_data)

# Now that the tally has been completed, create summary variables
# Calculate percent for each candidate
candidate_0_percent = candidate_0_count / total_votes
candidate_1_percent = candidate_1_count / total_votes
candidate_2_percent = candidate_2_count / total_votes

# Winner of the election based on popular vote
winner_votes = max(candidate_0_count, candidate_1_count, candidate_2_count)

# Match with the candidate
for candidate in candidates: 
    if candidate_0_count == winner_votes: 
        winner = candidates[0]
    elif candidate_1_count == winner_votes:
        winner = candidates[1]
    elif candidate_2_count == winner_votes:
        winner = candidates[2]
    else:
        print("Error: Candidate not found")

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{candidates[0]}: {candidate_0_percent:.3%} ({candidate_0_count})")
print(f"{candidates[1]}: {candidate_1_percent:.3%} ({candidate_1_count})")
print(f"{candidates[2]}: {candidate_2_percent:.3%} ({candidate_2_count})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export a text file with the results
# Specify the file to write to
output_path = os.path.join("Analysis", "election_results.txt")
