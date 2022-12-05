"""
Abdallah
Class: CS 521 - Summer 2
Date:8/20/22
Final Project
This is the Expense class that will get the user name,value,date, and catergory of what they spend
"""
class Expense:
    ''' class Expense'''
    def __init__(self, name, value, date, category):
        ''' initializing the class, and adding name, value, data, and category'''\
        #returning true if value is str
        if isinstance(value, str):
            # evaluating if value is larger or equal  to 0 
            if eval(value) >= 0:
                # defining class variables name, value, date, and category
                self.name = name
                self.value = eval(value)
                self.date = date
                self.category = category
        # if type of value is int and bigger or equal to 0
        elif type(value) == int and value >= 0:
            # defining class variables name, value, date, and category
            self.name = name
            self.value = value
            self.date = date
            self.category = category
        # raising value error if entered value is invalid
        else:
            raise ValueError
