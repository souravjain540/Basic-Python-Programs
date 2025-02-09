import csv
import datetime as dt
import pickle as p
import time
from os import system, name
#Variable List==========================
MonStart = False
INC = []	#Income
BAL= 0		#Current Balance
OEXP = 0	#Other Expences
TEXP = 0	#Total Expences
LIAB = {}	#Liabilities
TRAN = []
t = dt.datetime.now()
YEAR = 0
MONTH = 0

#=======================================
        
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def date():
    Time = t
    return Time

def save():
    fin = open("Save.dat","wb")
    global INC,BAL,OEXP,TEXP,TRAN,YEAR,MONTH,MonStart,LIAB
    Finance = {"MonStart":MonStart,"INC":INC,"BAL":BAL,"OEXP":OEXP,"TEXP":TEXP,"TRAN":TRAN,"YEAR":YEAR,"MONTH":MONTH,"LIAB":LIAB}
    p.dump(Finance,fin)
    fin.close()
    print("Data Saved Successfully")

def load():
    Finance = {}
    try:
        fout = open("Save.dat","rb")
        Finance = p.load(fout)
        fout.close()
    except EOFError:
        fout.close()
    except:
        f = open("Save.dat","wb")
        f.close()
        load()
    if Finance != {}:
        global INC,BAL,OEXP,TEXP,TRAN,YEAR,MONTH,MonStart,LIAB
        INC = Finance["INC"]
        BAL = Finance["BAL"]
        OEXP = Finance["OEXP"]
        TEXP = Finance["TEXP"]
        TRAN = Finance["TRAN"]
        YEAR = Finance["YEAR"]
        MONTH = Finance["MONTH"]
        MonStart = Finance["MonStart"]
        LIAB = Finance["LIAB"]
        print("Data Loaded Successfully")
    else:
        print("Data Not Found, Starting Newly")

def newLoan():
    LOAN = input("Name Your New Loan: ")
    AMT = intInput("Enter Amount of Loan Taken: ")
    l = [LOAN,AMT]
    LIAB[len(LIAB)+1] = l
    print(f"New Loan: {LOAN}, issued for Rs {AMT}, added to Liabilities")

def install():
    for x,y in LIAB.items():
        print(f"{x} => {y[0]} = {y[1]}")
    NAME = ""
    while True:
        LOAN = intInput("Enter the SERIAL NUMBER of the Loan paid:")
        if LOAN > len(LIAB):
            print("Please Enter In Range")
        else:
            break
    INS = intInput("Enter Amount Paid as Instalment: ")
    for x,y in LIAB.items():
        if x == LOAN:
            NAME = y[0]
            y[1] -= INS
            Left = y[1]
            break 
    global TEXP
    global BAL
    BAL -= INS
    TEXP += INS
    disc = f"'{NAME}' Liability Installment Paid"
    Day = input("Enter Date of Trasaction: ")
    Date = f"{Day}/{MONTH}/{YEAR}"
    l = [INS,disc,Date]
    global TRAN
    TRAN.append(l)
    print(f"Instalment of Rs{INS} paid in {NAME}, Rs{Left} left to be paid")

def expns():
    Amt = intInput("Enter Amount Spent: ")
    disc = input("Enter Description of Transaction: ")
    Day = intInput("Enter Date of Transaction:  ")
    Date = f"{Day}/{MONTH}/{YEAR}"
    global BAL
    BAL -= Amt
    global OEXP
    global TEXP
    TEXP += Amt
    OEXP += Amt
    global TRAN
    l = [Amt,disc,Date]
    TRAN.append(l)
    print(f"Amount of Rs{Amt} deducted from Balace")

def expchrt():
    print("Initialising Process...")
    global MonStart
    x = dt.datetime(YEAR,MONTH,1)
    FName = f'{x.strftime("%B")} {x.year}.csv'
    File = open(FName,"a",newline="")
    print(f"New File {FName} created")
    writer = csv.writer(File)
    writer.writerow([f"Finance of the Month{x.strftime('%B')} in Year {x.year}",'','',''])
    writer.writerow("")
    print("Adding Income Data")
    writer.writerow(["Income Data",'','',''])
    writer.writerow(["Sr. No.","Amount","Description","Date of Transaction"])
    n = 1
    for i in INC:
        i.insert(0, n)
        writer.writerow(i)
        n += 1
    print("Income data Added \n Adding Expance Data")
    writer.writerow("")
    writer.writerow(["Expance Data",'','',''])
    writer.writerow(["Sr. No.","Amount","Description","Date of Transaction"])
    n = 1
    for i in TRAN:
        i.insert(0, n)
        writer.writerow(i)
        n += 1
    writer.writerow("")
    print("Expance Data Added \n Adding Liabilities")
    writer.writerow(["Pending Liabilities",'','',''])
    writer.writerow(['Sr. No.','Name','Amount'])
    for i in LIAB:
        l = [i,LIAB[i][0],LIAB[i][1]]
        writer.writerow(l)
    writer.writerow("")
    print("Liabilities Added")
    print(f"File Created and Data Loaded Successfully, File Name: {FName}")
    time.sleep(5)
    print("Thank You for Using This Program, See You Next Month")
    time.sleep(3)
    File.close()
    MonStart = False
    save()


def loanList():
    for x,y in LIAB.items():
        print(f"{x}){y[0]} = Rs {y[1]}")

def intInput(get):
    while True:
        inp = input(get)
        if inp.isnumeric() == True or inp.isdecimal() == True:
            break
        else:
            print("Invalid Input, Enter a Number")
            continue
    return int(inp)

def monthStart():
    load()
    global INC,OEXP,TEXP,TRAN,YEAR,MONTH,MonStart
    if MonStart == False:
        while True:
            user = intInput('''1 - Start New Month Finance
2 - Total Reset 
3 - Exit Program
>>> ''')
            if user == 1:
                MonStart = True
                INC = []
                OEXP = 0
                TEXP = 0
                TRAN = []
                print("The Program is Adjusting for New Month")
                YEAR = intInput("Enter Year of Finance: ")
                while True:
                    inp = intInput("Enter Month of Finance(Number): ")
                    if inp in range(1,13):
                        MONTH = inp
                        break
                    else:
                        print("Invalid Input")
                x = dt.datetime(YEAR,MONTH,1)
                print("Welcoming",x.strftime("%B"),"in",x.year,", Let's Manage Your Finance")
                time.sleep(3)
                main()
                break
            elif user == 2:
                get = input("Do you really want to Reset whole Program? (All your data including your saved Liabilities and Balance will be Lost): (y/n)")
                if get.upper() == "Y":
                    global LIAB,BAL
                    MonStart = True
                    INC = []
                    BAL= 0
                    OEXP = 0
                    TEXP = 0
                    LIAB = {}
                    TRAN = []
                    YEAR = 0
                    MONTH = 0
                    print("The Program has been Totally Resetted")
                    YEAR = intInput("Enter Year of Finance: ")
                    while True:
                        inp = intInput("Enter Month of Finance(Number): ")
                        if inp in range(1,13):
                            MONTH = inp
                            break
                        else:
                            print("Invalid Input")
                    x = dt.datetime(YEAR,MONTH,1)
                    print("Welcoming",x.strftime("%B"),"in",x.year,", Let's Manage Your Finance")
                    time.sleep(3)
                    main()
                    break
                else:
                    continue 
            elif user == 3:
                print("Thank You For using This Program...")
                time.sleep(2)
                break
            else:
                print("Enter Invalid Input")
    elif MonStart == True:
        main()

def main():
    clear()
    global YEAR,MONTH,BAL
    while True:
        user = intInput('''
    Enter the SERIAL NUMBER of Action you want to Perform:
    1)Add Income
    2)View Balance
    3)Applied for New Loan
    4)Loan List
    5)Pay Loan Installment
    6)Regular Expense Add-In
    7)End Month and Get Transaction Chart
    8)Exit Program
    >>> ''')
        if user == 1:
            clear()
            inc = intInput("Enter the Amount of Income Recieved: Rs ")
            disc = input("Enter Description: ")
            Day = intInput("Enter Date of Transaction (Day of the Month): ")
            Date = f"{Day}/{MONTH}/{YEAR}"
            BAL += inc
            l = [inc,disc,Date]
            INC.append(l)
            print(f"Income of Rs {inc} has been added to your Balance")
        elif user == 2:
            clear()
            print(f"Current Bank Balance: Rs {BAL}")
        elif user == 3:
            clear()
            newLoan()
        elif user == 4:
            clear()
            if LIAB != {}:
                loanList()
            else:
                print("You have not applied for any Loan")
        elif user == 5:
            clear()
            if LIAB != {}:
                install()
            else:
                print("You have not applied for any Loan")
        elif user == 6:
            clear()
            expns()
        elif user == 7:
            clear()
            expchrt()
            break 
        elif user == 8:
            clear()
            save()
            print("Thank You For using This Program...")
            time.sleep(2)
            break
        else:
            print("Invalid Input")
            
        time.sleep(1)

monthStart()