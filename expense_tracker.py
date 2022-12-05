"""
Abdallah
Class: CS 521 - Summer 2
Date:
Final Project

This program has an ExpenseTracker class that keeps track of expenses and current balances. 

"""

#dict of months 
month_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",\
    7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

class ExpenseTracker:
    
    #constructor method
    def __init__(self, initialDeposit):
        ''' initializing the class with self and intial deposit and creating variables to be used to track expenses'''
        #setting intial deposit
        self.__balance = initialDeposit
        #creating an empty list of expenses in class
        self.expenses = []
        #creating a dict of expenses
        self.monthly_expenses = {}
        #creating a set of categories
        self.monthly_cat = {}
        #creating name and year and setting them to none to be used by user
        self.name = None
        self.year = None
    
    # creating a spend method using the expense class
    def spend(self, item):
        ''' creating a method to track how much the user spends'''
        #appending the items to the list of expenses
        self.expenses.append(item)
        # creating a private balance while subtracting the item's value
        self.__balance -= item.value
        # calling methods with item 
        self.__set_monthly_expenses(item)
        # calling methods with item
        self.__set_monthly_cat(item)

    def __set_monthly_expenses(self, item):
        '''creating a method to keep track monthly expenses'''
        # if item date is in monthly expenses dict  we will add the item value to the exisiting value
        if item.date in self.monthly_expenses:
            #magic method add 
            new_balance = self.monthly_expenses[item.date].__add__(item.value)
            self.monthly_expenses[item.date] = new_balance
        # create new month and with the value 
        else: 
            self.monthly_expenses[item.date] = item.value
    
    def __set_monthly_cat(self ,item):
        ''' method to show user what catergories user  expenses were'''
        # if item date is not in monthly cat
        #create empty catergory set 
        cat = set()
        if item.date not in self.monthly_cat:
            # add category to empty set
            cat.add(item.category)
            # set item date to cat set 
            self.monthly_cat[item.date] = cat

        else: 
            # if item date is in cat then cat = to item date
            cat = self.monthly_cat[item.date]
            # if item category is not in cat set
            if(item.category not in cat):
            #add category to cat set
                cat.add(item.category)


            
    def get_balance(self):
        '''create a method to get return balance'''
        #return balance - kept private
        return self.__balance
    
    def get_spending_per_month(self, month):
        ''' create method to keep track of spending per month'''

        if month in self.monthly_expenses: 
                # print how much was spent in a given month
                print(f'You have spent ${self.monthly_expenses[month]} in {month_dict[month]}')
        elif month >= 13 or month == 0:
                print(f'The {month}\'s month is not in the calender')
        else:
            # if the month was not entered yet print a message saying that user hasnt entered expense for month yet
            print(f'You haven\'t enterted an expense for {month_dict[month]} yet.')
                    
    def deposit(self, value):
        ''' method to keep track of deposit and updates __balance'''
        #balance kept private
        self.__balance += value

    
    def get_expenses(self):
        ''' method to get expenses for each item entered'''
        print('These are all the expenses you have entered so far:')
        print('-'*60)
        # loops through self.expenses
        for ex in self.expenses:
            #print how much was spent on a item on a given date
            print(f'You spent: ${str(ex.value)} on {ex.name} during the month of {str(ex.date)}/{self.year}.')
        print('-'*60)

    def set_account(self, base_info):
        ''' method to set account for user'''
        # name of user assigned 
        self.name = base_info[0] 
        # year for given expenses
        self.year = base_info[1]
        
    # string method 
    def __str__(self):
        ''' string method to return balance '''
        return (f'Hello {self.name}, your remaining balance for {self.year} is ${self.get_balance()}')