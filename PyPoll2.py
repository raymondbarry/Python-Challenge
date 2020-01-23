import os
import csv

PyPollcsv = os.path.join("PyPoll","Resources", "election_data.csv")

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next (csvreader)
    for row in csvreader:
        count = count + 1
        candidatelist.append(row[2])
    for x in set(candidatelist):
        unique_candidate.append(x)
        y = candidatelist.count(x)
        vote_count.append(y)
        z = (y/count)*100
        vote_percent.append(z)
    
    winning_vote_count = max(vote_count)
        # candidatelist = row["Candidate"]
        # if row["Candidate"] not in candidatelist:
        #     candidatelist.append(row["Candidate"])
        #     candidate_votes[row["Candidate"]] = 1

        # else:
        #     candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total vote_count :" + str(count))    
print("-------------------------")
print("-------------------------")

for n in vote_count:
    vote_percent.append(round(n/vote_count*100, 1))

clean_data = list(zip(candidatelist, vote_count, vote_percent))

winner_list = []

for name in clean_data:
    if max(vote_count) == name[1]:
        winner_list.append(name[0])

winner = winner_list[0]

print("The winner is: " + str(winner))
print("-------------------------")
# for candidate in vote_count:
#     print(Candidate + " " + str(round(((vote_count[candidate]/vote_count)*100))) + "%" + " (" + str(vote_count[candidate]) + ")")
#     candidate_results = (candidate + " " + str(round(((vote_count[candidate]/vote_count)*100))) + "%" + " (" + str(vote_count[candidate]) + ")")
#     Winner = sorted(vote_count.items(), key=itemgetter(1), reverse=True
 # winning_vote_count = max(vote_count)
    # winner = unique_candidate[vote_count.index(winning_vote_count)]


# for i in range(len(unique_candidate)):
#     print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")

# PyPollcsv = os.path.join("PyPoll","Resources", "election_data.csv")
import os
electionresultstxt = os.path.join("PyPoll", "Resources", "electionresults.txt")
with open(electionresultstxt, "w") as text:
    text.write("Election Results")
    text.write("\n")
    text.write("-------------------------")
    text.write("\n")
    #text.write(candidate + " " + str(round(((candidate_votes[candidate]/vote_count)*100))) + "%" + " (" + str(candidate_vote_count[candidate]) + ")")
    text.write("\n")
    text.write("-------------------------")
    text.write("\n")
    text.write("Winner: " + winner)
    text.write("\n")
    text.write("Total Votes " + str(winning_vote_count))
# with open('election_results.txt', 'w') as text:

#     text.write("Election Results\n")

#     text.write("---------------------------------------\n")

#     text.write("Total Vote: " + str(count) + "\n")

#     text.write("---------------------------------------\n")

#     for i in range(len(set(unique_candidate))):

#         text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")

#     text.write("---------------------------------------\n")

#     text.write("The winner is: " + winner + "\n")

#     text.write("---------------------------------------\n")

