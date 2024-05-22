import random
from abc import ABC

class User(ABC):
    def __init__(self, name, email, adress) -> None:
        self.name = name
        self.email = email
        self.adress = adress

class Customer(User):
    def __init__(self, name, email, adress, accountType) -> None:
        super().__init__(name, email, adress)
        self.accountType = accountType
        self.balance = 0
        self. transaction_history = []
        self.account_number = random.randint(1,112)+99

    def history(self):
        print("------Transaction_History------")
        for info in self.transaction_history:
            for key, val in info.items():
                print(f'{key} : {val}')
        print()

    def deposit(self, amount, bank):
        bank.bank_balance += amount
        self.balance += amount
        self.transaction_history.append(
                {"Operation": "Deposit", 
                "Amount" : amount}
            )
        print(f'Deposit {amount} tk Successfully')


    def withdraw(self, amount, bank):
        if bank.bankrpt == False:
            if self.balance > amount:
                self.balance -= amount
                bank.bank_balance -= amount
                self.transaction_history.append(
                    {"Operation": "Withdraw", 
                    "Amount" : amount}
                )
                print(f'Whithdraw {amount} tk Successfully')
            else: 
                print(f'Wihdrawal amount exceeded')
        else:
            print("Bankrupt no transaction is possible.")


    def check_balance(self):
        print(f'your current balance is {self.balance}')

    def take_loan(self, amount, bank):
        loan_count = 2
        if loan_count > 0:
            if bank.bank_balance > amount:
                if bank.loan:
                    if bank.bankrpt == False:
                        bank.total_loan += amount
                        self.balance += amount
                        loan_count -= 1
                        self.transaction_history.append(
                            {"Operation": "loan", 
                            "Amount" : amount}
                            )
                        print(f'You took {amount} tk loan from bank.')
                    else:
                        print("Bankrupt no transaction is possible.")
                else:
                    print("Sorry currently loan status is off.")
            else:
                print("Invalid request!!!")
        else:
            print("You have already used your max loan attempt.")

    def send_money(self, to_email, amount, bank):
        bank.transfer_balance(self.email, to_email, amount)

class Admin(User):
    def __init__(self, name, email, adress) -> None:
        super().__init__(name, email, adress)

    def create_admin(self, admin_info, bank):
        bank.create_admin_account(admin_info)

    def view_customer_list(self, bank):
        bank.user_list()

    def view_admin_list(self, bank):
        bank.admin_list()

    def remove_user(self, user_email, bank):
        bank.delete_account(user_email)

    def check_bank_balances(self, bank):
        bank.bank_balances()

    def check_total_bank_loan(self, bank):
        bank.loan_balance()

    def set_loan_status(self, status, bank):
        bank.loan_status(status)

    def set_bankrupt_status(self, status, bank):
        bank.bankrpt_status(status)
    
