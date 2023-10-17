class Account:
    accounts = []
    transactionHistory = []
    loanTimes = 0
    onLoan = True
    def __init__(self, name, email, address, accountType):
        self.name = name
        self.email = email
        self.address = address
        self.accountType = accountType
        self.balance = 0
        self.totalLoan = 0
        self.accNo = name+email
        Account.accounts.append(self)

    def deposit(self, amount):
        if amount >=0:
            self.balance += amount
            print(f'You deposited {amount}')
            self.transactionHistory.append(f'You depogited {amount} ')
        else:
            print(f'You can not deposit negative amount')

    def withdraw(self, amount):
        if amount < 0:
            print(f'You can not withdraw negative amount')
        elif amount < self.balance and amount > 0:
            self.balance -= amount
            print(f'You withdrawed {amount}')
            self.transactionHistory.append(f'You withdrawed {amount}')
        else:
            print(f'Withdrawal amount exceeded')
    def checkBalance(self):
        print(f'Your total balance is {self.balance}')
    def checkTransactionHistory(self):
        print(f'Your transaction history')
        for history in self.transactionHistory:
            print(f'Transaction: {history}')
    def takeLoan(self, loanAmount):
        if loanAmount <= self.balance:
            if self.onLoan == True:
                if loanAmount >=0 and self.loanTimes < 2 :
                    self.loanTimes +=1
                    self.balance +=loanAmount
                    self.totalLoan += loanAmount
                    print(f'You took loan {loanAmount}')
                    self.transactionHistory.append(f'You took loan {loanAmount} ')
                elif loanAmount < 0:
                    print(f'You can not take negative amount of loan')
                else:
                    print(f'You can not take loan more than 2 twice')
            else:
                print('Loan is not available at tme moment')
        else: 
            print(f'Bank does not have {loanAmount} money')
    def transferMoney(self, accNo, transferAmount):
        flag = 0
        for i in range(0, len(self.accounts)):
            if accNo == self.accounts[i].accNo:
                flag = 1
                if self.balance >= transferAmount:
                    print(f'Transtered {transferAmount} to {self.accounts[i].accNo} account number')
                    self.transactionHistory.append(f'You transfered {transferAmount} ')
                    self.accounts[i].balance += transferAmount
                    self.balance -= transferAmount
                else:
                    print(f'You do not have {transferAmount} balance in your account')
        if flag == 0:
            print(f'Account does not exist')


class SavingsAccount(Account):
    def __init__(self, name, email, address):
        super().__init__(name, email, address, 'savings')
class CurrentAccount(Account):
    def __init__(self, name, email, address):
        super().__init__(name, email, address, 'current')

class Bank:
    total_balance = 0
    totalLoan = 0
    def create_account(self, name, email, address):
        account = SavingsAccount(name, email, address)
        Bank.accounts.append(account)
    
    def delete_account(self, accNo):
        # if len(Account.accounts) > 0:
        for i in range(0, len(Account.accounts)):
            if accNo == Account.accounts[i-1].accNo:
                Account.accounts.remove(Account.accounts[i-1])
                print(f'Deleted account No {accNo}')
                return
        else:
            print("account not found")

    def show_users(self):
        if len(Account.accounts) > 0:
            for account in Account.accounts:
                print(f'Name: {account.name} Email: {account.email} Address: {account.address} AccNo: {account.accNo}')
        else:
            print("No user found")

    def show_total_balance(self):
        for account in Account.accounts:
            self.total_balance += account.balance
        print(f'Total balance: {self.total_balance}')
    
    def total_loan(self):
        for account in Account.accounts:
            self.totalLoan += account.totalLoan
        print(f'Total loan: {self.totalLoan}')

    def loan_offOn(self, status):
        if status == 'T':
            Account.onLoan = True
        elif status == 'F':
            Account.onLoan = False

user = None
currentUser = None
while True:
    print(f'Log in as admin or user (a/u)')
    ch=input("Enter option: ")
    if ch=='a':
        while True:
            user = 'Admin'
            print(f"Welcome {user}")
            print("1. Create an account")
            print("2. delete any user account")
            print("3. see all user accounts list ")
            print("4. check the total available balance ")
            print("5. Total loan ")
            print("6. Off/On loan ")
            print("7. Quit")
            choice=input("Enter option: ")
            if choice=='1':
                name=input("Name: ")
                email=input("Email: ")
                address=input("Address: ")
                type = input('Enter type Savings/Current (s/c)')
                if type == 's':
                    currentUser = SavingsAccount(name, email, address)
                elif type == 'c':
                    currentUser = CurrentAccount(name, email, address)
                else:
                    print('Invalid option')
                    break
            elif choice=='2':
                if len(Account.accounts) > 0:
                    accNo = input("Enter Account Number: ")
                    Bank().delete_account(accNo)
                else:
                    print('No user found')
            elif choice == '3':
                Bank().show_users()
            elif choice == '4':
                Bank().show_total_balance()
            elif choice == '5':
                Bank().total_loan()
            elif choice == '6':
                status = input('Loan option off and on (F / T)')
                if status == 'T' or status == 'F':
                    Bank().loan_offOn(status)
                else:
                    print('Invalid option')
            elif choice == '7':
                break
            else:
                print('Invalid option')
                break

    elif ch == 'u':
        while True:
            user = 'User'
            print(f"Welcome {user}")
            print("1. Create an account")
            print("2. deposit")
            print("3. withdraw")
            print("4. check available balance")
            print("5. check transaction history")
            print("6. take loan")
            print("7. Transfer amount to another")
            print("8. Quit")

            choice=input("Enter option: ")
            if choice=='1':
                name=input("Name: ")
                email=input("Email: ")
                address=input("Address: ")
                currentUser = SavingsAccount(name, email, address)
                
            elif choice == '2':
                if currentUser is not None:
                    amount = int(input("Enter amount: "))
                    currentUser.deposit(amount)
                else:
                    print('No current user found')

            elif choice == '3':
                if currentUser is not None:
                    amount = int(input("Enter amount: "))
                    currentUser.withdraw(amount)
                else:
                    print('No current user found')

            elif choice == '4':
                if currentUser is not None:
                    currentUser.checkBalance()
                else:
                    print('No current user found')
                
            elif choice == '5':
                if currentUser is not None:
                    currentUser.checkTransactionHistory()
                else:
                    print('No current user found')

            elif choice == '6':
                if currentUser is not None:
                    amount = int(input("Enter amount: "))
                    currentUser.takeLoan(amount)
                else:
                    print('No current user found')
                
            elif choice == '7':
                if currentUser is not None:
                    accNO = input("Account Number: ")
                    amount = int(input("Enter amount: "))
                    currentUser.transferMoney(accNO, amount)
                else:
                    print('No current user found')

            elif choice == '8':
                break
            else:
                print('Invalid option')
                break
                #OK
