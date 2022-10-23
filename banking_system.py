# TODO:
# Parent Class : User
# Holds details about an user
# Has function to show user details
# Child Class : Bank
# Stores details about the account balance
# Stores details about the amount
# Allows for deposit, withdraw and view balance

# Parent Class
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print(f"""
                Personal Details
            -------------------------
                Name   : {self.name}
                Age    : {self.age}
                Gender : {self.gender}
                """)
        
# arjun = User('Arjun',20,'Male')
# print(arjun)
# arjun.show_details()

# Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance += self.amount
        print(f"Successfully Deposited : ${self.amount}")
        print(f"Current Balance : ${self.balance}")
        print()
        
    def withdraw(self,amount):
        self.amount = amount
        if self.amount < self.balance:
            self.balance -= self.amount
            print(f"Successfully  Withdrawn ${self.amount}")
            print(f"Current Balance : ${self.balance}")
            print()
        else:
            print("Not Enough Balance!!!") 
            print(f"Current Balance : ${self.balance}")
            print()
            
    def view_balance(self):
        self.show_details()
        print("            -------------------------")
        print(f"              Current Balance : ${self.balance}")
        print()

#--------------------------------------------------

sbi = Bank('Akshay',20,'Male')
print(sbi)
# sbi.show_details()
# sbi.view_balance()
# sbi.deposit(100)
sbi.deposit(1000)
sbi.withdraw(100)
# sbi.withdraw(1100)
