class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.custo_account_list = []
        self.admin_account_list = []
        self.bank_balance = 0
        self.total_loan = 0
        self.loan = False
        self.bankrpt = False

    def find_customer(self, email): #no duplicate email is possible
        for acc in self.custo_account_list:
            if email == acc.email:
                return acc
        return None
    
    def find_admin(self, email):
        for acc in self.admin_account_list:
            if email == acc.email:
                return acc
        return None
    
    def transfer_balance(self, sender_email, to_email, amount):
        sender = self.find_customer(sender_email)
        reciever = self.find_customer(to_email)
        if sender is not None and reciever is not None:
            if self.bankrpt == False:
                if sender.balance > amount:
                    reciever.balance += amount
                    sender.balance -= amount
                    print(f'From {sender_email} to {to_email} total {amount} Tk transfered successfully')
                    sender.transaction_history.append(
                        {"Operation": "Send money", 
                        "Amount" : amount}
                        )
                    reciever.transaction_history.append(
                        {"Operation": "Recive money", 
                        "Amount" : amount}
                        )
                else:
                    print("Limit exited")
            else:
                print("Bankrupt no transaction is possible")
        else:
            print("Invalid User")

    def create_user_account(self, customer):
        self.custo_account_list.append(customer)
        print("Account created successfully.") 
    
    def create_admin_account(self, admin):
        self.admin_account_list.append(admin)
        print("Account created successfully.") 

    def delete_account(self, email):
        for acc in self.custo_account_list:
            if email == acc.email:
                self.custo_account_list.remove(acc)
                print("Account deleted successfully.")
            else:
                print("User not found")
    
    def user_list(self):
        for acc in self.custo_account_list:
            print(f'User name: {acc.name}\tUser Email: {acc.email}\tAccount Name: {acc.accountType}')

    def admin_list(self):
        for acc in self.admin_account_list:
            print(f'User name: {acc.name}\tUser Email: {acc.email}')

    def bank_balances(self):
        print(self.bank_balance)
    
    def loan_balance(self):
        print(self.total_loan)

    def loan_status(self, status):
        if status.lower() == "on":
            self.loan = True
            print(f'Loan Status On')
        elif status.lower()=="off":
            self.loan = False
            print(f'Loan Status Off')

    def bankrpt_status(self, status):
        if status.lower() == "on":
            self.bankrpt = True
            print(f'Loan Status On')
        elif status.lower()=="off":
            self.bankrpt = False
            print(f'Loan Status Off')

    