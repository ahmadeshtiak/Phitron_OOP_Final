from datetime import datetime 
class Person:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password



class User(Person):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0
        self.transaction = []

    def check_balance(self):
        print(f"Your current balance is {self.balance} Taka")
    
    def deposit(self):
        amount = int(input("Enter the amount you want to deposit: "))
        if amount>0:
            self.balance += amount
            self.transaction.append(f"Deposited {amount} taka on  ----- {datetime.now().strftime('%c')}")
            print(f"Successfully {amount} taka added to your account!")
            Bank.available_balance += amount
        else:
            print("Please enter a valid amount")
    
    def withdraw(self):
        amount = int(input("Enter the amount you want to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance in your account")
        else:
            if amount > Bank.available_balance:
                print("Sorry! The bank is bankrupted")
            else:
                self.balance -= amount
                self.transaction.append(f"Withdrawn {amount} taka on  ----- {datetime.now().strftime('%c')}")
                print(f"Successfully {amount} taka withdrawn from your account!")
                Bank.available_balance -= amount
    
    def transfer(self):
        print("-----Showing available users to transfer amount-----")
        for user in Bank.total_users:
            if self!=user:
                print(user.name)
        nm = input("Enter the name you want to transfer: ")
        amount = int(input("Enter the amount you want to transfer: "))
        if amount > self.balance:
            print("Insufficient balance in your account")
        else:
            for user in Bank.total_users:
                if user.name == nm:
                    #got the user to transfer
                    user.balance += amount
                    self.balance -= amount
                    self.transaction.append(f"Transfered {amount} taka to {user.name} on  ----- {datetime.now().strftime('%c')}")
                    user.transaction.append(f"Transfered {amount} taka from {self.name} on  ----- {datetime.now().strftime('%c')}")
                    print("Successfully transfered amount")

    def check_transaction(self):
        print("-----------------Showing Transaction History-----------------")
        for trx in self.transaction:
            print(trx)
        print("-------------------------------------------------------------")

    def take_loan(self):
        l = int(input("Enter the loan amount you want to take: "))
        if l > self.balance * 2:
            print(f"You cannot take loan greater than {self.balance*2}")
        else:
            if Bank.loan_feature == "ON":
                self.balance += l
                print(f"Loan {l} taka taken successfully")
                Bank.available_balance -= l
                Bank.total_loan_taken += l
                self.transaction.append(f"Loan taken {l} taka on  ----- {datetime.now().strftime('%c')}")
            else:
                print("Bank's loan feature is currently off")




 



class Admin(Person):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
    
    def check_total_balance(self):
        print(f"Available total balance in the bank is {Bank.available_balance} taka")

    def check_total_loan(self):
        print(f"Total loan taken {Bank.total_loan_taken} taka")

    def loan_feature(self):
        print(f"Loan feature is currently {Bank.loan_feature}")
        inp = int(input("1. Turn ON feature\n2. Turn OFF feature\nPlease enter your choice: "))
        if Bank.loan_feature == "OFF" and inp==1:
            Bank.loan_feature == "ON"
            print("Successfully turned on the loan feature")
        elif Bank.loan_feature == "ON" and inp == 2:
            Bank.loan_feature == "OFF"
            print("Successfully turned off the loan feature")
        else:
            print("Please try again")



class Bank:
    total_users = []
    total_admins = []
    available_balance = 50000000
    total_loan_taken = 0
    loan_feature = "ON"
    
    def create_account(self):
        while True:
            n = int(input("1. Create account as User\n2. Create account as Admin\n3. Back to main menu\nPlease enter your choice: "))
            if n==1:
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                password = input("Enter a new password: ")
                new_user = User(name, email, password)
                self.total_users.append(new_user)
                print("Account created succesfully!")
            elif n==2:
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                password = input("Enter a new password: ")
                new_admin = Admin(name, email, password)
                self.total_admins.append(new_admin)
                print("Account created succesfully!")
            elif n==3:
                break
            else:
                print("Invalid Input! Please try again.")
    
    def login(self):
        while True:
            print("*****Loging in to your account*****")
            n = int(input("1. Login as User\n2. Login as Admin\n3. Back to main menu\nPlease enter your choice: "))
            if n==1:
                em = input("Enter your email: ")
                pas = input("Enter your password: ")
                for user in self.total_users:
                    if user.email == em and user.password == pas:
                        print(f"----------Welcome Back {user.name}----------")
                        #Implement the Users class todos here
                        while True:
                            print("1. Check balance\n2. Deposit\n3. Withdraw\n4. Transfer balance\n5. Transaction History\n6. Take loan\n7. Return to previous menu")
                            inp1 = int(input("Please enter your choice: "))
                            if inp1 == 1:
                                user.check_balance()
                            elif inp1 == 2:
                                user.deposit()
                            elif inp1 == 3:
                                user.withdraw()
                            elif inp1 == 4:
                                user.transfer()
                            elif inp1 == 5:
                                user.check_transaction()
                            elif inp1 == 6:
                                user.take_loan()
                            elif inp1 == 7:
                                break
                    else:
                        print("Wrong email or password. Please try again.")
            elif n==2:
                e = input("Enter your email: ")
                p = input("Enter your password: ")
                for admin in self.total_admins:
                    if admin.email == e and admin.password == p:
                        print(f"----------Welcome Back {admin.name}----------")
                        #Implement the Admin class todos here
                        while True:
                            print("1. Check total available balance in the bank\n2. Check total loan amount\n3. Turn ON/OFF loan feature\n4. Back to previous menu")
                            inp1 = int(input("Please enter your choice: "))
                            if inp1 == 1:
                                admin.check_total_balance()
                            elif inp1 == 2:
                                admin.check_total_loan()
                            elif inp1 == 3:
                                admin.loan_feature()
                            elif inp1 == 4:
                                break      
                    else:
                        print("Wrong email or password. Please try again.")
            elif n==3:
                break
            else:
                print("Enter a valid input!")


while True:
    Bappy_NGO = Bank()
    print("1. Create an account\n2. Login\n3. Exit")
    given_input = int(input("Please enter your choice: "))
    if given_input == 1:
        Bappy_NGO.create_account()                                                                                                                                                                                                                                                   
    elif given_input == 2:
        Bappy_NGO.login()
    elif given_input == 3:
        break
    else:
        print("Enter a valid input!")
