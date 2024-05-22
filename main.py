from users import Customer, Admin
from bank import Bank

is_bank = Bank("Islami Bank")
Manager = Admin("Alam", "alam@gmail.com", "Dhaka")
Manager.create_admin(Manager, is_bank)


def admin_menu():

    while True:
        print(f"Welcome To Admin Dashboard")
        print("1 : Create New Admin")
        print("2 : Remove User")
        print("3 : View Admins")
        print("4 : View User")
        print("5 : Bank Stock")
        print("6 : Loan Balance")
        print("7 : Set Loan Status")
        print("8 : Set Bankrpt Status")
        print("9 : Exit")

        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            adminName = input("Type Name : ")
            adminEmail = input("Type Email : ").lower()
            adminAddress = input("Type Address : ")
            if is_bank.find_admin(adminEmail):
                print("Sorry This Email Allready Exist")
            else:
                newAdmin = Admin(adminName, adminEmail, adminAddress)
                Manager.create_admin(newAdmin, is_bank)

        elif choice == 2:
            userEmail = input("Type User Email ")
            Manager.remove_user(userEmail, is_bank)
        elif choice == 3:
            Manager.view_admin_list(is_bank)
        elif choice == 4:
            Manager.view_customer_list(is_bank)
        elif choice == 5:
            Manager.check_bank_balances(is_bank)
        elif choice == 6:
            Manager.check_total_bank_loan(is_bank)
        elif choice == 7:
            print(f"Loan Status : ")
            status = input("type on or off : ").lower()
            Manager.set_loan_status(status, is_bank)
        elif choice == 8:
            print(f"Bankrupt Status : ")
            status = input("type on or off : ").lower()
            Manager.set_bankrupt_status(status, is_bank)
        elif choice == 9:
            break
        else:
            print("Invalid Input")


def user_menu(customer):

    while True:
        print(f"Welcome To User Dashboard")
        print("1 : Deposite")
        print("2 : Withdraw")
        print("3 : Check Balance")
        print("4 : Take Loan")
        print("5 : Send Money")
        print("6 : History")
        print("7 : Exit")

        choice = int(input("Enter your choice : "))
        if choice == 1:
            amount = int(input("Enter Your Amount For Deposite = "))
            customer.deposit(amount, is_bank)
        elif choice == 2:
            amount = int(input("Enter Your Amount For Withdraw = "))
            customer.withdraw(amount, is_bank)
        elif choice == 3:
            customer.check_balance()
        elif choice == 4:
            amount = int(input("Enter Your Amount For Take Loan = "))
            customer.take_loan(amount, is_bank)
        elif choice == 5:
            re_email = input("Reciever Email : ")
            amount = int(input("Amount = "))
            customer.send_money(re_email, amount, is_bank)
        elif choice == 6:
            customer.history()
        elif choice == 7:
            break
        else:
            print("Invalid Input")


def admin_login():
    while True:
        print(f"Login First")
        email = input("Enter Your Email : ")
        if is_bank.find_admin(email):
            admin_menu()
            break
        else:
            print("Admin Does Not Exist")
            return


def customer_login():
    while True:
        print("1 : Login")
        print("2 : Sign Up")
        print("3 : Exit")

        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            email = input("Enter Your Email ")
            if is_bank.find_customer(email) is not None:
                user_menu(is_bank.find_customer(email))
            else:
                print("User Does Not Exist")
        elif choice == 2:
            userName = input("Name : ").lower()
            userEmail = input("User Email : ").lower()
            userAddress = input("User Address : ").lower()
            print("Account Type : Savings/Current")
            accountType = input("Account type : ").lower()
            if is_bank.find_customer(userEmail) is not None:
                print(f"Sorry {userEmail} Already Exist")
            else:
                customer = Customer(userName, userEmail, userAddress, accountType)
                is_bank.create_user_account(customer)
                user_menu(customer)
        elif choice == 3:
            break
        else:
            print("Invalid Input !!")


while True:
    print(f"Wellcome To {is_bank.name}")
    print("1 : Admin")
    print("2 : User")
    print("3 : Exit")
    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        admin_login()
    elif choice == 2:
        customer_login()
    elif choice == 3:
        break
    else:
        print("Invalid Input")
