import os
import csv

csvPath = os.path.join("..","budget_data.csv")

with open(csvPath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    monthsTotal = 0
    netProfitLosses = 0
    lastMonthPL = 0
    avgChngProfitLoss = 0
    profitLossDiffs = 0
    greatestIncProfit = 0
    currentHighestProfit = 0
    greatestDecLoss = 0
    currentLoss = 0

    for row in csvreader:
        monthsTotal = monthsTotal + 1
        netProfitLosses = netProfitLosses + int(row[1])
      
        # Once there's been more than one month, we can take this diff,
        #   otherwise one counts the jump from 0 to the first month's profit.
        if monthsTotal > 1:
            profitLossDiffs = profitLossDiffs + (lastMonthPL - int(row[1]))

        # This makes last month's profits, defined at first as 0, reflect the row that
        #   just passed thru the profitLossDiffs eq. Allows one to access previous row easily.
        lastMonthPL = int(row[1])

        if int(row[1]) > greatestIncProfit:
            greatestIncProfit = int(row[1])
            date1 = row[0]

        if int(row[1]) < greatestDecLoss:
            greatestDecLoss = int(row[1])
            date2 = row[0]

    # Writing this outside of the loop to not waste time computing avgs for each line.
    avgChngProfitLoss = round(profitLossDiffs/monthsTotal, 2)
    

    output = "Financial Analysis \n\n"
    output += "---------------------------------- \n"

    output += f"Total Months: {monthsTotal} \n"
    output += f"Total: ${netProfitLosses} \n"
    output += f"Average Change: ${avgChngProfitLoss} \n"

    output += f"Greatest Increase in Profits: {date1} (${greatestIncProfit}) \n"
    output += f"Greatest Decrease in Losses: {date2} (${greatestDecLoss}) \n"
    output += "----------------------------------"

    print(output)

    f = open("PyBank.txt", "w")
    f.write(output)
    f.close()