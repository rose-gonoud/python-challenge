import os
import csv

csvPath = os.path.join("..","budget_data.csv")

with open(csvPath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    monthsTotal = 0
    netProfitLosses = 0
    avgChngProfitLoss = 0
    greatestIncProfit = 0
    greatestDecLoss = 0

    for row in csvreader:
        monthsTotal = monthsTotal + 1

        netProfitLosses = netProfitLosses + int(row[1])



    #output_file = os.path.join("PyBank.txt")
    #with open(output_file, "w", newline="") as datafile:
     #   writer = text.writer(datafile)
      #  writer.writerow(["Total Months", "Total", "Average Change", "Greatest Increase in Profits", "Greatest Decrease in Losses"])
       # writer.writerows(roster)

print(monthsTotal)
print(netProfitLosses)