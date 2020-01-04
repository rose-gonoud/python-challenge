import os
import csv

csvPath = os.path.join("..","election_data.csv")

with open(csvPath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    votesCast = 0
    candidates = []

    for row in csvreader:
        votesCast += 1

        matched_candidate = False
        for candidateDict in candidates:
            if row[2] == candidateDict["Candidate"]:
                matched_candidate = candidateDict
                candidateDict["Votes"] = candidateDict["Votes"] + 1

        # this should take care of the first case in which there is no dict yet
        # and any future case in which row[2] != candidateDict["Candidate"].
        if not(matched_candidate): 
            candidates.append({"Candidate": row[2],
                                    "Votes": 1})

    for candidateDict in candidates:
        percentVotes = round(((candidateDict["Votes"]/votesCast)*100), 0)
        candidateDict["Percentage of Votes"] = percentVotes
    
    highestVotes = 0
    electionWinner = []
    for candidateDict in candidates:
        if candidateDict["Votes"] > highestVotes:
            highestVotes = candidateDict["Votes"]
            electionWinner = candidateDict["Candidate"]

    output = "Election Results \n\n"
    output += "---------------------------------- \n"
    output += f"Total Votes: {votesCast} \n"
    output += "---------------------------------- \n"

    for candidateDict in candidates:
        output += f"{candidateDict['Candidate']} won {candidateDict['Votes']} (%{candidateDict['Percentage of Votes']}). "
        output += "\n"

    output += "---------------------------------- \n"
    output += f"Election Winner: {electionWinner} \n"
    output += "----------------------------------"

    print(output)

    f = open("PyPoll.txt", "w")
    f.write(output)
    f.close()