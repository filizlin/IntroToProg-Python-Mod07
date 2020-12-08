# ------------------------------------------------------------------------ #
# Title: Assignment 07_Structured Error Handling
# Description: Demonstration of how structured error handling can be used
# ChangeLog (Who,When,What):
# <YLin>,<12.04.2020>,Create Script
# ------------------------------------------------------------------------ #

# Data-------------------------------------------------------------------- #
# Declare variables and constants #
strchoice = None


# Processing------------------------------------------------------------- #

class RangeError(Exception):
    """The number input is out of range"""
    def __str__(self):
        return "Please enter a number between 1 and 5"

# Presentation (Input/Output)  ------------------------------------------ #
while(True):
    print('''
        Please choose on of the following options:
        1) open file
        2) add data to file
        3) remove data from file
        4) save file
        5) Exit the program
        ''')
    try:
        strChoice = input("Please enter your choice: ")
        if '1' <= strChoice <= '5':
            print("proceeding with your request")
        elif strChoice.isnumeric() == False:
            raise Exception("Please enter a numeric value [9 instead of nine]")
        elif '1' >= strChoice or strChoice >= '5':
            raise RangeError()


    except Exception as e:
        print("An error has occur")
        print("Built-In Python error info: ")
        print(e, e.__doc__, sep='\n')




