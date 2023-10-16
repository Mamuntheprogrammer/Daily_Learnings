from abc import ABC, abstractclassmethod
class User(ABC):
    acc = 0
    acconuts = {}
    total_blance = 0
    loan = 0
    count_loan = 0

    def __init__(self,name,email,address,type) -> None:
        User.acc +=1
        self.name = name
        self.email  = email
        self.address = address
        self.type = type
        self.accNumber = User.acc
        self.current_balance = 0
        self.transaction_history = []


    #deposit function
    def deposit(self,amount):
        if amount >= 0:
            self.current_balance =+ amount
            User.total_blance += amount
            self.transaction_history.append(f'congratulations {self.name}  {amount} deposited successfull..')
            print(f'{self.name} your deposite balance successfully ..., your current balance {self.current_balance} taka')


    #withdraw functionality

    def withdraw(self, amount):
        if User.total_blance == 0:
            print('The bank is bankrupt')
        elif amount < self.current_balance:
            self.current_balance -= amount
            self.transaction_history.append(f'congratulations {self.name}  {amount} withdraw balance  successfull..')
            print(f'{self.name} your withdraw balance successfully ..., your current balance {self.current_balance} taka')

        else:
            print('Withdrawal amount exceeded')


    #check balance functionality
    def check_available_balance(self):
        print(f'{self.name} your available balance is {self.current_balance} taka')


    #show transaction history
    def history(self):
        for statement in self.transaction_history:
            print(statement)

    #loan functionaly
    def loan_balance(self,amount):
        if Admin.status_loan == 1:
            if User.count_loan < 2:
                self.current_balance += amount
                User.loan += amount
                User.count_loan += 1
                self.transaction_history.append(f'congratulations {self.name}  {amount} loan successfull..')
                print(f'{self.name} your loan balance successfully ..., your current balance {self.current_balance} taka')
            else:
                print(f'{self.name} you can not loan more than only  tow time available') 
        else:
            print('loan from the bank at most two times')
     
    #money transfer functionality
    def transfer(self,recipient_acc_N0,amaount):
        print(str(recipient_acc_N0) in User.acconuts.keys())
        if str(recipient_acc_N0) in User.acconuts.keys():
            print('acces 1')
            recipient = User.acconuts[recipient_acc_N0]
            if amaount > 0 and self.current_balance >= amaount:
                self.current_balance -= amaount
                print('acces 2')
                recipient.transaction_history.append(f'Receivrd {amaount} from {self.name}')
                self.transaction_history.append(f'Transfer {amaount} to {recipient.name}')
                print(f'{self.name} you transfer {amaount} take to {recipient.name} Your current balance is {self.current_balance} taka ')
               
            else:
                print('Insufficient balance ')
        else:
            print('Recipient account does not exits or Invaild')


class Admin:
    status_loan = 1

    #create account functionality
    def acc_create(self,name,email,address,acc_type):
        user = User(name,email,address, acc_type)
        User.acconuts[user.accNumber] = user
        print(f'Accounnt Create Successfully')

    #delete account functionality

    def det_account(self,account_no):
        if account_no in User.acconuts:
            del User.acconuts[account_no]
            print(f'{account_no} delete successfully')
    #sell all list account
    def all_acc_list(self):
        for accoun_number , user in User.acconuts.items():
            print('------------')
            print(f'Account number :',accoun_number)
            print(f'name : {user.name}')
            print(f'email : {user.email}')
            print(f'address: {user.address}')
            print(f'account type : {user.type}')
    #check total available balance        
    def total_balance(self):
        print(f'total  balance is {User.total_blance}')
    #total al loan amount
    def total_loan_amount(self):
        print(f'total loan balance is {User.loan}')

    #loan status
    def loan_status(self, status):
        if status == 1 or status== 0:
            Admin.status_loan = status
        else:
            print('Invaild use(True or False)')
admin = Admin()
while True:
    print('choice your option admin or users')
    print('1 Admin')
    print('2 User')
    print('3 Exit')
    op=int(input('Please Enter your any Option: '))
    
    if op==1:
        while True:
            print('choice your option from below :')
            print('1 create an new account')
            print('2 delete an account')
            print('3 sell all user list')
            print('4 check the total balance of the bank')
            print('5 check the total loan amount')
            print('6 on or off the loan features this bank')
            print('7 exit')
            choice = int(input('Please Enter your Option :'))
            if choice == 1:
                name = input('Enter your name:')
                email = input('Enter your email address: ')
                address = input('Enter your address:')
                acc_type = input('Enter your accunt type sv or cr:')

                admin.acc_create(name,email,address,acc_type)
               

            elif choice == 2:
                delete_acc_no = int(input('Enter Your delete account number:'))
                admin.det_account(delete_acc_no)
            elif choice ==3:
                admin.all_acc_list()
            elif choice == 4:
                admin.total_balance()
            elif choice == 5:
                admin.total_loan_amount()
            elif choice == 6:
                status = int(input('Enter your status True = 1 or Flase = 0'))
                admin.loan_status(status)
            elif choice == 7:
                break
            else:
                print('Invaild choice. please try again')
    elif op == 2:
        currnent_user = None
        while True:
            if currnent_user == None:
                print('Currently no users')
                print('1 create account:')
                print('2 Deposit')
                print('3 Withdraw:')
                print('4 cheak available balance:')
                print('5 check check transaction history')
                print('6 Take a loan')
                print('7 transfer the amount ')
                print('8 Exit')

                choice = int(input('Enter your choice:'))
                if choice == 1:
                    
                    name = input('Enter your name:')
                    email = input('Enter your email address: ')
                    address = input('Enter your address:')
                    acc_type = input('Enter your accunt type (sv or cr:)')
                    currnent_user=User(name,email,address,acc_type)
                    print(f'Congratulations ! {name} your {acc_type}account create successful' )
                elif choice == 2:
                    amount=int(input('Enter your Deposit amount:'))
                    currnent_user.deposit(amount)
                elif choice == 3:
                    amount = int(input('Enter your Withdraw amount:'))
                    currnent_user.withdraw(amount)
                elif choice == 4:
                    currnent_user.check_available_balance()
                elif choice == 5:
                    currnent_user.transaction_history()
                elif choice == 6:
                    amount = int(input('Enter bank loan amount:'))
                    currnent_user.loan(amount)
                elif choice == 7:
                    amount = int(input('Enter your  transfer amount:'))
                    currnent_user.transfer(amount)
                elif choice == 8:
                    break
                else:
                    print('Invalid choice please try again')
                    break
            else:
                print(f'...Currently user is {currnent_user.name}....')
                print('Your option is below :')
                print('1 create account:')
                print('2 Deposit')
                print('3 Withdraw:')
                print('4 cheak available balance:')
                print('5 check check transaction history')
                print('6 Take a loan')
                print('7 transfer the amount ')
                print('8 Exit')

                choice = int(input('Enter your choice:'))
                if choice == 1:
                    
                    name = input('Enter your name:')
                    email = input('Enter your email address: ')
                    address = input('Enter your address:')
                    acc_type = input('Enter your accunt type (sv or cr:)')
                    currnent_user = User(name,email,address,acc_type)
                    print(f'Congratulations ! {name} your {acc_type}account create successful' )
                elif choice == 2:
                    amount=int(input('Enter your Deposit amount:'))
                    currnent_user.deposit(amount)
                elif choice == 3:
                    amount = int(input('Enter your Withdraw amount:'))
                    currnent_user.withdraw(amount)
                elif choice == 4:
                    currnent_user.check_available_balance()
                elif choice == 5:
                    currnent_user.history()
                elif choice == 6:
                    amount = int(input('Enter bank loan amount:'))
                    currnent_user.loan_balance(amount)
                elif choice == 7:
                    repicient = int(input('Enter your id  for repicient:'))
                    amount = int(input('Enter your  transfer amount:'))
                    currnent_user.transfer(repicient,amount)
                elif choice == 8:
                    break
                else:
                    print('Invalid choice please try again')
                    break
    elif op == 3:
        break

 