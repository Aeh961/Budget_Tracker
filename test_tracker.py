"""
Abdallah
Class: CS 521 - Summer 2
Date:
Final Project


"""

# import modules needed

import unittest
import expense_tracker
import expense

class TestExpenseTracker(unittest.TestCase):
    '''class to set up test'''
    def setUp(self):
        '''method to setup test'''
        #assign a variable to test
        self.et = expense_tracker.ExpenseTracker(100)
    def test_initial_balance(self):
        ''' intital balance test to see if it works'''
        # assigning actual balance 
        actual_balance = self.et.get_balance()
        #assert actual balance to 100 to test
        assert actual_balance == 100

    def test_spend_update_the_balance(self):
        '''method to try a second test'''
        #calling Expense class with certain paramters 
        item = expense.Expense('qfc', 50, 7, 'food')
        #calling function with spend item from Expense class
        self.et.spend(item)
        # assigning get balance to actual balance
        actual_balance = self.et.get_balance()
        # asserting actual balance to 50
        assert actual_balance == 50

    def test_negative_spending(self):
        ''' testing if negative amount spent '''
        # try calling expense with -1500$ spent
        try:
            expense.Expense('rent', -1500, 7, 'rent')
        except ValueError:
            pass
        else:
            self.fail('unexpected exception raised')