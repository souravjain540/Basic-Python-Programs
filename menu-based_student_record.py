studList = []

def appendStudent():
    global studList
    singlr = []
    studName = input('Enter your name: ')
    
    while True:
        Rollno = input('Enter your Rollno: ')
        if Rollno.isdigit():
            Rollno = int(Rollno)
            break
        else:
            print("Rollno should be an integer. Please try again.")
    
    while True:
        try:
            cgpa = float(input('CGPA (decimal): '))
            break
        except ValueError:
            print("CGPA should be a decimal number. Please try again.")
    
    singlr.append(studName)
    singlr.append(Rollno)
    singlr.append(cgpa)
    studList.append(singlr)

# Remove existing record by rollno
def removeRecord():
    global studList
    while True:
        rolln = input("Enter student's Rollno: ")
        if rolln.isdigit():
            rolln = int(rolln)
            break
        else:
            print("Rollno should be an integer. Please try again.")
    
    found = False
    for record in studList:
        if rolln == record[1]:  # Comparing Rollno which is the second item in the list
            studList.remove(record)
            found = True
            break  # Exit the loop once the record is found and removed
    
    if not found:
        print("Student not found.")


# View student by name
def viewRecord():
    name = input("Enter student's name: ")
    found = False
    for record in studList:
        if name == record[0]:  # Comparing name which is the first item in the list
            print(record)
            found = True
            break
    if not found:
        print("Student not found.")


# Copy list (functionality can be implemented as needed)
def copyList():
    global studList
    copiedList = studList.copy()
    print("Copied list:", copiedList)

# View all students
def viewAllRecords():
    if not studList:
        print("No students in the list.")
    else:
        for record in studList:
            print(record)

# Remove all records
def removeAll():
    global studList
    studList.clear()
    print("All records removed.")

# Show menu
def showMenu():
    print("Enter:")
    print("Option 1: Append student")
    print("Option 2: Remove student by Rollno")
    print("Option 3: View student by name")
    print("Option 4: Copy list")
    print("Option 5: View all Students ")
    print("Option 6: Remove all students")
    print("Option 7: Exit")

# Main program loop
def main():
    flag = 'y'
    while flag.lower() == 'y':
        showMenu()
        try:
            find = int(input("Enter your choice: "))
            if find == 1:
                appendStudent()
            elif find == 2:
                removeRecord()
            elif find == 3:
                viewRecord()
            elif find == 4:
                copyList()
            elif find == 5:
                viewAllRecords()
            elif find == 6:
                removeAll()
            elif find == 7:
                print("Exiting the program.")
                break
            else:
                print("Enter correct option !!")
        except ValueError:
            print("Please enter a valid number.")
        
        while True:
            flag = input("Do you want to continue? (y/n): ").lower()
            if flag in ['y', 'n']:
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

# When the code is run, the main function will be executed first to give options to the user.
if __name__ == "__main__":
    main()

