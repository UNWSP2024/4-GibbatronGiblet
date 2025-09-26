# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    ######################
    year_number = int(input("How many years of rainfall do you wish to average?"))
    month_number= year_number * 12
    rainfall_total = 0
    current_month = 0
    current_year = 0

    for month in range(year_number):
        current_year += 1
        for month in range(12):
            current_month %= 12
            current_month += 1
            monthly_rainfall = float(input(f"What is the average rainfall in inches for year {current_year} month {current_month}?"))
            while monthly_rainfall < 0:
                print("There is no such thing as negative rainfall. Please try again.")
                monthly_rainfall = float(input(f"What is the average rainfall in inches for year {current_year} month {current_month}?"))
            while monthly_rainfall > 370:
                record_rainfall = input(f"Whoa! There's never been that much monthly rainfall before. Is {monthly_rainfall} inches the correct amount? (y/n):")
                if record_rainfall == "n":
                    monthly_rainfall = float(input(f"What is the average rainfall in inches for year {current_year} month {current_month}?"))
                else:
                    break
            rainfall_total += monthly_rainfall


    print(f"You have calculated the monthly rainfall average for {month_number} months.")
    print(f"The total rainfall was {rainfall_total} inches.")
    print(f"The average monthly rainfall was {rainfall_total / month_number} inches.")

    #Written by Logan Gibson on 9/25/25. The program's name is "Average Rainfall Calculator"

    ######################    


if __name__ == '__main__':
    main()