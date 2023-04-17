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
candidate_col = 2 # Column C

#-----------------------------------------

def analyze_votes(election_data):

    # List of variables created in the code
    global candidate_list
    global total_votes
    global candidate_votes

    candidate_list = list()
    candidate_votes = {}
    total_votes = 0
    candidate_0_count = 0
    candidate_1_count = 0
    candidate_2_count = 0

    # Loop through the table
    for row in election_data:

        # Set the row's candidate
        current_candidate = row[candidate_col]

        # Check if the candidate is on our set
        is_candidate_in_list = current_candidate in candidate_list

        # If not in list, add candidate to list
        if is_candidate_in_list == False:
            # Add candidate to list
            candidate_list.append(current_candidate)
            # Add candidate to dictionary for votes
            candidate_votes[current_candidate] = 0
        # If on list, skip
        else:
            # Candidate already exists on list and in votes dictionary
            pass

        # Now that we are compiling the candidates, start tally for each candidate
        # Total number of votes each candidate won
        candidate_votes[current_candidate] += 1

        # Total number of votes cast
        # Each row is 1 vote
        total_votes += 1

    return candidate_list, candidate_votes, total_votes

# Run function on data
with open(CSV_PATH) as csv_file:
    election_data = csv.reader(csv_file)
    header = next(election_data) # Skip header row
    analyze_votes(election_data)

# Winner of the election based on popular vote, see support documents on finding max
winner = max(key for key, value in candidate_votes.items() if value == max(candidate_votes.values()))

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidate_list:
    print(f"{candidate}: {candidate_votes[candidate]/total_votes:.3%} ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# Export a text file with the results
# Specify the file to write to
output_path = os.path.join("Analysis", "election_results.txt")
with open(output_path, "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-------------------------\n")
    for candidate in candidate_list:
        text_file.write(f"{candidate}: {candidate_votes[candidate]/total_votes:.3%} ({candidate_votes[candidate]})\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("-------------------------\n")