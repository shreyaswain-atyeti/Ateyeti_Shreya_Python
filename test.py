class Bank:
    def __init__(self, account_holder, account_number, balance=0.0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited amount {amount} and the new balance is {self.balance}")
        else:
            print("Invalid depoist, the amount should be positive")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient fund")
        else:
            self.balance -=amount
            print(f"{amount} has been deducted  and the available check_balance is {self.balance}")

    def check_balance(self):
        print(f"The available balance is {self.balance}")

    def account_summary(self):
        print("---Account Summary---")
        print(f"Account holder's name is: {self.account_holder}")
        print(f"Account number is : {self.account_number}")
        print(f"Balance is: {self.balance}")

account1 = Bank("Shreya_Swain",1149,5000)
account2 = Bank("Riya_Swain", 2249, 4000)

account1.check_balance()
account2.check_balance()
account1.deposit(2000)
account2.deposit(1000)
account1.check_balance()
account2.check_balance()
account1.withdraw(1000)
account2.withdraw(1000)
account1.account_summary()
account2.account_summary()