import os                                                                       # Create file path across os 
import csv                                                                      # Read CSV files
election_data = os.path.join("Resources", "election_data.csv")                  # Read csv file by using pathlib.Path

with open(election_data) as csvfile:                                            # Continue by using with open() as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')                              # Use CSV reader ('r') to specify delimiter 
    csv_header = next(csvreader)                                                # Read the header row first --> CSV Header: ['Voter ID', 'County', 'Candidate']

    incremental_votes = {}                                                      # make dictionary to calculate incremental votes for each person

# Use the For Loop to read each row of data after csv_header
    for row in csvreader:                                             
        candidates_name = row[2]
        if candidates_name in incremental_votes:
            incremental_votes[candidates_name] += 1                             # Add 1 to 
        else:
            incremental_votes[candidates_name] = 1

# A complete list of candidates who received votes
    candidates = list(incremental_votes.keys())                                 # prints --> dict_keys(['Khan', 'Correy', 'Li', "O'Tooley"])
    vote_counts = list(incremental_votes.values())                              # prints --> dict_values([2218231, 704200, 492940, 105630])
    
# The total number of votes each candidate won
    total_votes = sum(vote_counts)                                              # prints --> 3521001
    total_votes_fm = '{:,}'.format(total_votes)                                 # formats --> 3,521,001
    votes_pct = [vote / total_votes for vote in vote_counts]                    # loops equation to receive 
    votes_pct_fm = ['{:.0%}'.format(votes_pct) for votes_pct in votes_pct]      # loops equation to format to %
    
# The winner of the election based on popular vote
    Election_Winner = candidates[votes_pct.index(max(votes_pct))]               # grab max % in votes_pct >>> find its index >>> apply to candidates to find name

#save as txt file
with open('Poll_Data_Analysis.txt', 'w') as txtfile:
  
    # save information as textfile 
    output =  ("Election Results\n"
        "----------------------------\n"
        f"Total Votes: {total_votes_fm}\n"
        "----------------------------\n")
    txtfile.write(output)
    print(output)

    for candidate in (candidates):
        txtfile.write(f"{candidate}: {votes_pct_fm[candidates.index(candidate)]} ({vote_counts[candidates.index(candidate)]})\n")
        print(f"{candidate}: {votes_pct_fm[candidates.index(candidate)]} ({vote_counts[candidates.index(candidate)]})\n")

    output_2 = ("----------------------------\n"
        f"Winner {Election_Winner}\n"
        "----------------------------\n")

    txtfile.write(output_2)
    print(output_2)