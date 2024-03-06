# Python Program Using OPP(Object Oriented Programming)
# Python program representing a bank. Including methods for managing customer accounts and transactions.

import pprint

class Bank:
    def __init__(self) -> None:
        self.customer: dict = {}

    def create_acount(
        self, account_holder: str, account_number: int, initial_balance: int
    ):
        if account_number in self.customer:
            pprint.pprint("Account is Already Created")
        else:
            self.customer[account_number] = {
                "account_holder": account_holder,
                "balance": initial_balance,
            }
            pprint.pprint(
                f"Congratulation {account_holder} your account is Created Successfully"
            )

    def make_deposit(self, account_number: int, amount: int):
        if account_number not in self.customer:
            pprint.pprint("Invalid Account Number")
        elif amount <= 0:
            pprint.pprint("Deposit must be greater than zero.")
        else:
            self.customer[account_number]["balance"] += amount
            pprint.pprint(f"Deposited Amount Successfully {amount}")

    def make_withdraw(self, account_number: int, amount: int):
        if account_number not in self.customer:
            pprint.pprint("Invalid Account Number")
        elif amount <= 0:
            pprint.pprint("Deposit must be greater than zero.")
        else:
            self.customer[account_number]["balance"] -= amount
            pprint.pprint(f"withdraw Amount Successfully {amount}")


    def check_balance(self, account_number: int) -> None:
        if account_number not in self.customer:
            pprint.pprint("Invalid Account Number")
        else:
            balance = self.customer[account_number]["balance"]
            pprint.pprint(f"The current balance of your account is :{balance}")


bank = Bank()
bank.create_acount(
    account_holder="Resheph Inayat", account_number=123, initial_balance=100
)
bank.make_deposit(account_number=123, amount=900)
bank.make_withdraw(account_number=123, amount=500)
bank.check_balance(account_number=123)
