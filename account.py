class Account:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance!")
        else:
            self.balance -= amount

    def check_balance(self):
        return self.balance


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account_number):
        account = self.find_account(account_number)
        if account:
            self.accounts.remove(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        print("Account not found.")
        return None


# create a new bank
my_bank = Bank("My Bank")

# prompt the user to add accounts
while True:
    account_number = int(input("Enter account number (0 to stop): "))
    if account_number == 0:
        break
    account_holder_name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))
    my_bank.add_account(Account(account_number, account_holder_name, balance))

# prompt the user to interact with accounts
account_number = int(input("Enter account number to interact with: "))
account = my_bank.find_account(account_number)

if account:
    print("Account holder name:", account.account_holder_name)
    print("Current balance:", account.check_balance())

    while True:
        action = input("Enter action (deposit/withdraw/stop): ")
        if action == "stop":
            break
        amount = float(input("Enter amount: "))

        if action == "deposit":
            account.deposit(amount)
        elif action == "withdraw":
            account.withdraw(amount)

        print("New balance:", account.check_balance())
else:
    print("Invalid account number.")
