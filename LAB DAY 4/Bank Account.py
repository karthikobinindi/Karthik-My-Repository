class BankAccount:

    # Parameterized Constructor
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print("Account created successfully")

    # Deposit Method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Invalid deposit amount")

    # Withdraw Method
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")

        elif amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Remaining Balance:", self.balance)

    # Destructor
    def __del__(self):
        print("Account object deleted")


# Creating object
acc1 = BankAccount(12345, 5000)

# Operations
acc1.deposit(2000)
acc1.withdraw(1000)
acc1.withdraw(8000)   # Invalid case
