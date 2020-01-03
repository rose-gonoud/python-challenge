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

        # this should take care of the first case in which there is no dict yet.
        if not(matched_candidate): 
            candidates.append({"Candidate": row[2],
                                    "Votes": 1})

    print(votesCast)
    print(candidates)


    #output = "Election Results \n\n"
    #output += "---------------------------------- \n"

    #output += f"Total Votes: {votesCast} \n"
    #output += "---------------------------------- \n"

    #---

    #output += f"Total: ${netProfitLosses} \n"
    #output += f"Average Change: ${avgChngProfitLoss} \n"

    #output += f"Greatest Increase in Profits: {date1} (${greatestIncProfit}) \n"
    #output += f"Greatest Decrease in Losses: {date2} (${greatestDecLoss}) \n"
    #output += "----------------------------------"

    #print(output)

    #f = open("PyPoll.txt", "w")
    #f.write(output)
    #f.close()