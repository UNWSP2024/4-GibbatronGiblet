# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 0.0         #initialize for while loop
    total = 0.0

    ######################
    item_number = 1
    item_cost = 1
    budget = float(input("What is your monthly budget in dollars?"))
    while True:
        item_cost = float(input(f"How much, in dollars, did you spend on budget item {item_number}? Enter 0 to exit the loop."))
        if item_cost > 0:
            spent += item_cost
            item_number += 1
        elif item_cost == 0:
            break
        else:
            print("You did not enter a valid item value. Try again.")
            
    difference = budget - spent
    if difference > 0:
        print(f"You are ${difference:.2f} under budget this month. Nice work!")
    elif difference < 0:
        print(f"You are ${-difference:.2f} over budget this month. You need to follow your budget more closely.")
    else:
        print("You are exactly on budget. Don't spend anymore!")

        # Written by Logan Gibson on 9/25/25. The program's name is "Budget Calculator"
    ######################


if __name__ == '__main__':
    main()