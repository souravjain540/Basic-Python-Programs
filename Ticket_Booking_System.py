import random
from tabulate import tabulate
import mysql.connector as con

# Connect to the database
dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
co = dbo.cursor()

# NEW USER REGISTRATION SECTION
def new_user():
    dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
    co = dbo.cursor()
    pid = random.randint(0, 1000) * 10
    print("----------------------------------------------------------------------")
    print(" \n Welcome to our reservation system \n Register Yourself here to use our system")
    uid = input("Enter your user id: ")
    name = input("Enter your name: ")
    pno = input("Enter your phone no: ")
    eid = input("Enter your email_id: ")
    pwd = input("Enter your password: ")
    co.execute("insert into user values ('{}', {}, '{}', {}, '{}', '{}')".format(uid, pid, name, pno, eid, pwd))
    print("************* Congratulations!!! Your id is successfully created **************")
    print("----------------------------------------------------------------------")
    dbo.commit()

# FORGET USER ID
def forgot_user_id():
    dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
    co = dbo.cursor()
    email = input("Enter your registered email: ")
    co.execute("select user_id from user where email_id like '{}'".format(email))
    emel = co.fetchall()
    for i in emel:
        print("Your user_id is: ", (i[0]))

# OLD USER LOGIN
def old_user():
    dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
    co = dbo.cursor()
    print("\n---------------------------------------------------------------\n")
    uid = input("Enter your user id: ")
    co.execute("select user_id from user where user_id like '{}'".format(uid))
    b = co.fetchall()
    c = len(b)
    if c == 0:
        print("---------------- Your given id is not registered -----------------")
        print("\n------------------------------------------------------------------\n")
        print("1. Try again")
        print("2. Forgot user id")
        print("3. Register as a new user")
        choose = int(input("Choose an option from above: "))
        if choose == 1:
            old_user()
        elif choose == 2:
            forgot_user_id()
        elif choose == 3:
            new_user()
    else:
        pas = input("Enter your password: ")
        co.execute("select password from user where password like '{}'".format(pas))
        n = co.fetchall()
        for i in n:
            if pas == (i[0]):
                print("\n---------------------------------------------------------------\n")
                print("-----------Welcome back sir/ma'am what's your plan Today??---------\n")
                passenger_panel(uid)

# USER PANEL
def user_panel():
    print(" 1. Register")
    print(" 2. Login")
    print(" 3. Back")
    out = int(input("Enter your choice: "))
    if out == 1:
        new_user()
    elif out == 2:
        old_user()
    elif out == 3:
        main_menu()

# ADMIN PASSWORD FUNCTION
def adminpassword():
    password = (input("Enter your password: "))
    if password == "CLASS12CS":
        print("******************Access Granted********************")
        print("---------------------------------------------------------------------")
        admin_panel()
    else:
        print("***************ACCESS NOT GRANTED ENTER CORRECT PASSWORD************")
        print("---------------------------------------------------------------------")
        adminpassword()

# ADD TRAIN
def add_train():
    dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
    co = dbo.cursor()
    print("---------------------------------------------------------------------")
    a = int(input("Enter train no: "))
    b = input("Enter train name: ")
    c = input("Enter train origin: ")
    d = input("Enter train destination: ")
    e = int(input("Enter train journey distance: "))
    g = input("Enter train journey time: ")
    h = int(input("Enter no of seats in AC: "))
    i = int(input("Enter no of seats in SL: "))
    j = int(input("Enter no of seats in GEN: "))
    k = int(input("Enter price of AC: "))
    l = int(input("Enter price of SL: "))
    m = int(input("Enter price of GEN: "))
    n = input("Enter days available: ")
    print("---------------------------------------------------------------------")
    co.execute("insert into train_schedule values ({}, '{}', '{}', '{}', {}, '{}', {}, {}, {}, {}, {}, {}, '{}')".format(a, b, c, d, e, g, h, i, j, k, l, m, n))
    print("*********You have added a new train details successfully************")
    dbo.commit()

# UPDATE TRAIN DETAILS
def update_details():
    dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
    co = dbo.cursor()
    print("---------------------------------------------------------------------")
    print("******Welcome to update train system******")
    print("1. Update train no")
    print("2. Update train name")
    print("3. Update train origin")
    print("4. Update train destination")
    print("5. Update journey distance")
    print("6. Update available days")
    print("7. Update journey time")
    print("8. Update no of seats in AC")
    print("9. Update no of seats in SL")
    print("10. Update no of seats in GEN")
    print("11. Update price of AC")
    print("12. Update price of SL")
    print("13. Update price of GEN")
    print("14. Exit")
    x = int(input("Enter your choice to use: "))
    
    while True:
        if x == 1:
            print("---------------------------------------------------------------------")
            print("**********YOU ARE GOING TO UPDATE TRAIN NO***********")
            tname = input("Enter train name whose no you want to update: ")
            tno = int(input("Enter updated train no: "))
            co.execute("update train_schedule set train_no={} where train_name='{}'".format(tno, tname))
            print("*******UPDATED SUCCESSFULLY********")
            print("---------------------------------------------------------------------")
            dbo.commit()
            return
        elif x == 2:
            print("---------------------------------------------------------------------")
            print("**********YOU ARE GOING TO UPDATE TRAIN NAME***********")
            tno = int(input("Enter train no whose name you want to update: "))
            tname = input("Enter updated train name: ")
            co.execute("update train_schedule set train_name='{}' where train_no={}".format(tname, tno))
            print("*******UPDATED SUCCESSFULLY********")
            print("---------------------------------------------------------------------")
            dbo.commit()
            return
        # similar elif conditions for updating other train details
        # To Update fare price of GEN of that train
        elif x == 13:
            print("---------------------------------------------------------------------")
            print("**********YOU ARE GOING TO UPDATE FARE PRICE OF GEN***********")
            tno = int(input("Enter train no whose fare price of GEN you want to update: "))
            tfg = input("Enter updated fare price of GEN: ")
            co.execute("update train_schedule set gen_fare={} where train_no={}".format(tfg, tno))
            print("*******UPDATED SUCCESSFULLY********")
            print("---------------------------------------------------------------------")
            dbo.commit()
            return
        elif x == 14:
            print("**********YOU ARE NOW OUT OF UPDATE DETAILS SECTION***********")
            break

# CANCEL TRAIN
def cancel_train():
    dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
    co = dbo.cursor()
    ct = int(input("enter train no which you want to cancel: "))
    co.execute("delete from train_schedule where train_no={}".format(ct))
    dbo.commit()
    print("*********** Train cancelled Successfully ****************")

# ADMIN PANEL
def admin_panel():
    while True:
        try:
            print("---------------------------------------------------------------------")
            print("******Welcome to admin panel******")
            print("1. Add train")
            print("2. Update details")
            print("3. Cancel Train")
            print("4. Log out")
            opt = int(input("Choose your option: "))
            if opt == 1:
                add_train()
            elif opt == 2:
                update_details()
            elif opt == 3:
                cancel_train()
            elif opt == 4:
                print("**********You are out of admin panel***********")
                print("---------------------------------------------------------------------")
                main_menu()
        except:
            print("**********Choose a correct option***********")
            print("---------------------------------------------------------------------")

# TRAIN SEARCH
def Train_Search():
    dbo = con.connect(host="localhost", user="root", password="admin", database="train_reservation")
    co = dbo.cursor()
    o = input("Enter your origin: ")
    d = input("Enter your destination: ")
    co.execute("select * from train_schedule where origin like '%{}%' and destination like '%{}%'".format(o, d))
    a = co.fetchall()
    for i in a:
        print("Train no.: ", a[0][0])
        print("Train name: ", a[0][1])
        print("Origin: ", a[0][2])
        print("Destination: ", a[0][3])
        print("Journey distance: ", a[0][4])
        print("Journey time: ", a[0][5])
        print("Ac Seats available: ", a[0][6])
        print("Sl Seats available: ", a[0][7])
        print("Gen Seats available: ", a[0][8])
        print("Ac Price: ", a[0][9])
        print("Sl Price: ", a[0][10])
        print("Gen Price: ", a[0][11])
        print("Train Available On: ", a[0][12])

# MAIN MENU
def main_menu():
    while True:
        print("---------------------------------------------------------------")
        print("\n************WELCOME TO TRAIN RESERVATION SYSTEM**************")
        print("---------------------------------------------------------------")
        print(" 1. Admin Panel")
        print(" 2. User Panel")
        print(" 3. Search Train")
        print(" 4. Exit")
        x = int(input("Enter your choice: "))
        if x == 1:
            adminpassword()
        elif x == 2:
            user_panel()
        elif x == 3:
            Train_Search()
        elif x == 4:
            print("\n----------------Thank You for Using our System---------------")
            exit()

# Calling the main menu to start the program
main_menu()
