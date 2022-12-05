"""
Abdallah
Class: CS 521 - Summer 2
Date: 8/20/2022
Final Project

this page reads the txt file of expenses
takes user input to perform desired tasks 
"""

#importing modules 
import sys
import expense_tracker
import expense

# variable expense tracker class instance 
expenseTracker = None
try:
    with open("program_demo.txt", "r") as f: 
        for line in f:
            if "initial" in line:
                value = int(line.split(":")[1])
                #instanciating a variable of ExpenseTracker class
                expenseTracker = expense_tracker.ExpenseTracker(value)
                #creating a tuple with name and year
                base_info = ("Abdallah", 2022)
                #building on an account on the ExpenseTracker 
                expenseTracker.set_account(base_info)
            elif "deposit" in line:
                #taking the value from the line after splitting it
                value = int(line.split(":")[1])
                #building a deposit value on te ExpenseTracker
                expenseTracker.deposit(value)
            else:
                #splitting the line by ','and striping the \n
                ex = line.rstrip("\n").split(",")
                # setting each item from expense module and Expense class 
                item = expense.Expense(ex[0], ex[1], int(ex[2]), ex[3])
                #building a spending value on te ExpenseTracker
                expenseTracker.spend(item)
#print error if file not found
except FileNotFoundError:
    print("There was an error reading the file!")
except IndexError:
    print('You have entered a wrong index')
except ValueError:
    print('You entered a wrong value')
except OSError:
    raise

else:
    
    # print options for user and take input 
    print(f'Hello {expenseTracker.name}!')
    print(f'Welcome to your expense tracker portal for the year {expenseTracker.year}!')
    #tracker question to see if user wants to continue use the program
    tracker_question = input('Would you like to check your expense tracker? Enter Y/N  ')
    
while tracker_question.upper() == 'Y':
    try:
    
        print('Enter 1 for your balance')
        print('Enter 2 for all your expenses')
        print('Enter 3 for your catergories of spending for each month')
        print('Enter 4 for spending per month')
        answer = int(input('Enter your response here: '))
        #if user entered 1 print __str__
        if answer  == 1:
            print(expenseTracker)
            tracker_question = input('Would you like to check your expense tracker Y/N?  ')
        # if user entered 2 print expenses and promt with tracker qustion
        elif answer == 2:
            expenseTracker.get_expenses()
            tracker_question = input('Would you like to check your expense tracker Y/N?  ')
        # if user entered 3 enter expenes with categories for each month 
        #and promt with tracker qustion
        elif answer ==3:
            for month,categories in expenseTracker.monthly_cat.items():
            #print spendings per month
                print(f'Your spending categories in {month}/{expenseTracker.year} were:')
                for cat in categories: # loop through catogeries
                    #print category 
                    print(cat, end ='--')
                print('\n')
            tracker_question = input('Would you like to check your expense tracker Y/N?  ')
        # if user entered 4 print expenses for given month
        elif answer == 4:

            month_of_choice = int(input('Enter the month you want to explore: '))
            #if month between 1 and 12 print spending of that month and promt tracker qestions again
            if 0 < month_of_choice or month_of_choice >= 12:
                expenseTracker.get_spending_per_month(month_of_choice)
                tracker_question = input('Would you like to check your expense tracker Y/N?  ')
            #catch invalid entries and promt with tracker qustion
            else:
                print('invalid entry please try again ')
                tracker_question = input('Would you like to check your expense tracker Y/N?  ')

        # else print invalid input if user entered wrong value 
        else:
            print('Invalid Entry please try again.')
            break
    # printing error if value entered is invalid
    except ValueError:
        print('You entered a wrong value, please run the program again.')
        sys.exit()
# print exiting message while answer is N
if tracker_question.upper() == 'N':
    print('You exited the program, goodbye!')
    sys.exit()
# printing else statement if user entered anything besides Y/N
else: 
    print('You entered a wrong value, Please try again.')
            
