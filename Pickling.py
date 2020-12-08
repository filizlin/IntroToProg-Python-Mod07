# ------------------------------------------------------------------------ #
# Title: Assignment 07_Pickling
# Description: Demonstration of pickling a data file
# ChangeLog (Who,When,What):
# <YLin>,<12.04.2020>,Create Script
# ------------------------------------------------------------------------ #

# Data-------------------------------------------------------------------- #
import pickle

#Declaring the list to pickle#
ToDoList = ["Homework","Lecture","Lab"]
Priority = ["Low", "High", "Low"]
Deadline = ["Soon", "1 week", "1 month"]
TimeEstimate = ["5 hours", "20 hours", "10 hours"]

#Storing the data as pickle#
DataFile = open("ToDoList", "wb")
pickle.dump(ToDoList, DataFile)
pickle.dump(Priority, DataFile)
pickle.dump(Deadline, DataFile)
pickle.dump(TimeEstimate, DataFile)
DataFile.close()

#opening the pickle file#
DataFile = open("ToDoList", "rb")
ToDoList = pickle.load(DataFile)
Priority = pickle.load(DataFile)
Deadline = pickle.load(DataFile)
TimeEstimate = pickle.load(DataFile)

#Unpickling the Data#



while(True):
    print('''Here is the list of data in the ToDoList.data: 
    1) To Do List
    2) Priority
    3) Deadline
    4) Time Estimate for the To Do List item
    5) Exit the Program
            ''')
    strChoice = input("Please select an item to retrieve from the File [1/2/3/4]: ")
    if str(strChoice).strip() == '1':
        print(ToDoList)
        continue

    elif str(strChoice).strip() == '2':
        print(Priority)
        continue

    elif str(strChoice).strip() == '3':
        print(Deadline)
        continue

    elif str(strChoice).strip() == '4':
        print(TimeEstimate)
        continue

    elif str(strChoice).strip() == '5':
        break

    else:
        print("Invalid entry.  Please enter a number between 1-5.")
        continue
