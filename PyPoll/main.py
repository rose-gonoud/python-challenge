import os
import csv

csvPath = os.path.join("..","election_data_copy.csv")

with open(csvPath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    votesCast = 0
    candidates = []

    for row in csvreader:
        votesCast += 1

        matched_candidate = False
        for candidateDict in candidates: 
            if row[2] in dict.values(candidateDict):
                matched_candidate == candidateDict
                # candidateDict[Votes] == candidateDict.get(Votes) + 1
                # how do I increment the value of "Votes" once for each loop thru?
            else:
                candidates.append({"Candidate": row[2],
                                    "Votes": 1})

        # this should take care of the first case in which there is no dict yet.
        if not(matched_candidate): 
            candidates.append({"Candidate": row[2],
                                    "Votes": 1})
    print(votesCast)
    print(candidates)

        #for candidateDict in candidates: 
            #for Candidate, Votes in candidateDict.items(): 
                #if Candidate == row[2]:
                    #matched_candidate = candidateDict
                #else:
                    #candidates.append({"Candidate": row[2],
                                        #"Votes": 1})

        # write a searcher fn, for each row check if cand is already in cand list
        # if not add
        # if yes increment cand vote total by 1.

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