# ------------------------------------------------------------------------ #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# RRoot,1.1.2030,Fixed bug by clearing the list before it was refilled
# Daylen Haines,11/11/2019,Modified code to complete assignment 6
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strChoice = ""  # Capture the user option selection
task = None
priority = None
keyToRemove = None
list_of_rows = None
# Data -------------------------------------------------------------------- #


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """ Processing the data to and from a text file """

    @staticmethod
    def ReadFileDataToList(file_name, list_of_rows):
        """
        Desc - Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "r")
        for line in file:
            data = line.split(",")
            row = {"Task": data[0].strip(), "Priority": data[1].strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def WriteListDataToFile(file_name, list_of_rows):
        objFile = open(file_name, "w")
        for dicRow in list_of_rows:  # Write each row of data to the file
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()

    @staticmethod
    def AddRowtoList(task, priority, list_of_rows):
        dicRow = {"Task": task, "Priority": priority}  # Create a new dictionary row
        list_of_rows.append(dicRow)  # Add the new row to the list/table

    @staticmethod
    def RemovingItemfromList(keyToRemove, list_of_rows):
        """ Removes a dictionary row from a list of rows
        :param keyToRemov: (string) with name to remove:
        :param lstTable: (list) with dictonary rows
        :return: (bool) value indicating function works"""
        # ToDo: Place processing code in a new function
        itemRemoved = False # Create boolean loop
        rowNumber = 0  # Create a counter to identify the current dictionary row in the loop
    # Step 3.3.b - Search though the table or rows for a match to the user's input
        while (rowNumber < len(lstTable)):
            if (keyToRemove == str(list(dict(lstTable[rowNumber]).values())[0])):  # Search current row column 0
                del lstTable[rowNumber]  # Delete the row if a match is found
            blnitemRemoved = True  # Set the flag so the loop stops
            rowNumber += 1  # Increase counter to get next row
        return itemRemoved

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ A class for perform Input and Output """

    @staticmethod
    def OutputMenuItems():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Remove an existing item.
        4) Save Data to File
        5) Reload Data from File
        6) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def InputMenuChoice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 6] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def ShowCurrentItemsInList(list_of_rows):
        """ Shows the current items in the list of dictionaries rows
        :param list_of_rows: (list) of rows you want to display
        :return: nothing"""
        print("******* The current items ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def UserInputTaskandPriority():
        """ Captures New Tasks and Priorities input by user
        :return: tuple(string, string) """
        task = str(input("What is the task? - ")).strip() #Get task from user
        priority = str(input("What is the priority? [high|low] - ")).strip() #Get priority from user
        print()  # Add an extra line for looks
        return (task, priority)


    # TODO: Create more functions that perform various IO tasks as needed

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
FileProcessor.ReadFileDataToList(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    IO.OutputMenuItems()  # Shows menu
    strChoice = IO.InputMenuChoice()  # Get menu option

    # Step 3 - Process user's menu choice
    # Step 3.1 Show current data
    if (strChoice.strip() == '1'):
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Step 3.2 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        # Step 3.2.a - Ask user for new task and priority
        # # ToDo: Place IO code in a new function
            #Converted to Function
                # strTask = str(input("What is the task? - ")).strip() # Get task from user
                # strPriority = str(input("What is the priority? [high|low] - ")).strip() #Get priority from user
                # # strTask = str(input("What is the task? - ")).strip()  # Get task from user
                # # strPriority = str(input("What is the priority? [high|low] - ")).strip()  # Get priority from user
                # print()  # Add an extra line for looks
        task, priority = IO.UserInputTaskandPriority()

        # Step 3.2.b  Add item to the List/Table
        # ToDo: Place processing code in a new function
            # Converted to Function
                # dicRow = {"Task": strTask, "Priority": strPriority}  # Create a new dictionary row
                # lstTable.append(dicRow)  # Add the new row to the list/table
        FileProcessor.AddRowtoList(task, priority, lstTable)


        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Step 3.3 - Remove a new item to the list/Table
    elif (strChoice == '3'):

        # Step 3.3.a - Ask user for item and prepare searching while loop
        keyToRemove = input("Which TASK would you like removed? - ")  # get task user wants deleted
        itemRemoved = False  # Create a boolean Flag for loop

        # # ToDo: Place processing code in a new function
        # intRowNumber = 0  # Create a counter to identify the current dictionary row in the loop
        #
        # # Step 3.3.b - Search though the table or rows for a match to the user's input
        # while (intRowNumber < len(lstTable)):
        #     if (strKeyToRemove == str(list(dict(lstTable[intRowNumber]).values())[0])):  # Search current row column 0
        #         del lstTable[intRowNumber]  # Delete the row if a match is found
        #         blnItemRemoved = True  # Set the flag so the loop stops
        #     intRowNumber += 1  # Increase counter to get next row
        FileProcessor.RemovingItemfromList(keyToRemove,list_of_rows)
        # Step 3.3.c - Update user on the status of the search
        if (itemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")
        print()  # Add an extra line for looks

        # Step 3.3.d - Show the current items in the table
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu
    # Step 3.4 - Save tasks to the ToDoFile.txt file
    elif(strChoice == '4'):

        #Step 3.4.a - Show the current items in the table
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table

        #Step 3.4.b - Ask if user if they want save that data
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):  # Double-check with user

            # # ToDo: Place processing code in a New function
            # Converted to Function
                # objFile = open(strFileName, "w")
                # for dicRow in lstTable:  # Write each row of data to the file
                #     objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
                # objFile.close()
            FileProcessor.WriteListDataToFile(strFileName, lstTable)

            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:  # Let the user know the data was not saved
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue  # to show the menu

    # Step 3.5 - Reload data from the ToDoFile.txt file (clears the current data from the list/table)
    elif (strChoice == '5'):
        print("Warning: This will replace all unsaved changes. Data loss may occur!")  # Warn user of data loss
        strYesOrNo = input("Reload file data without saving? [y/n] - ")  # Double-check with user
        if (strYesOrNo.lower() == 'y'):
            lstTable.clear()  # Added to fix bug 1.1.2030
            FileProcessor.ReadFileDataToList(strFileName, lstTable)  # Replace the current list data with file data
            IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        else:
            input("File data was NOT reloaded! Press the [Enter] key to return to menu.")
            IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Step 3.6 - Exit the program
    elif (strChoice == '6'):
        break   # and Exit

# Main Body of Script  ---------------------------------------------------- #