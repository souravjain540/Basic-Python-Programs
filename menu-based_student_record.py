singlerecord=[]
studList=[]
choice='y'
while choice.lower()!='n':
    studName=input('enter your name ')
    Rollno=input('enter your Rollno ')
    cgpa=int(input('cgpa :'))
    singlerecord.append(studName)
    singlerecord.append(Rollno)
    singlerecord.append(cgpa)
    studList.append(singlerecord)
    singlerecord=[]
    choice=input('enter your choice [y/n]')

#append
def appendStudent():
    global studList
    singlr = []
    studName=input('enter your name')
    Rollno=input('enter your Rollno')
    cgpa=int(input('cgpa :'))
    singlr.append(studName)
    singlr.append(Rollno)
    singlr.append(cgpa)
    studList.append(singlr)
    
    
# remove existing record by rollno
def removeRecord():
    global studList
    rolln=int(input("enter student's rollno:"))
    for record in studList:
        if rolln in record:
            studList.remove(record)

# view student by name:
def viewRecord():
    name=input("enter student's name:")
    for record in studList:
        if name in record:
            print(record)

# copy
def copyList():
    print("what to do??")

#remove all
def removeAll():
    studList.clear()

flag = 'y'
while (flag == 'y'):
    find = int(input("Enter \n option 1 : Append student \n option 2: remove student by Rollno\n option 3: view student by name\n option 4: copy list\n option 5: remove all students option \n 6: exit"))
    if (find == 1):
        appendStudent()
    elif (find == 2):
        removeRecord()
    elif (find == 3):
        viewRecord()
    elif (find == 4):
        copyList()
    elif (find == 5):
        removeAll()
    elif (find == 6):
        exit
    else:
        print("enter correct option !!")
    flag = input("do u want to continue ? say y or n : \n")
