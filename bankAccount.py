class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon

# increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount

#decreases the account balance by the given amount if there are sufficient funds;
#if there is not enough money, 
#print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if self.withdraw < balance:
            print(f"Insufficient Funds: Charging a ${5} fee")
            self.balance -= {5}
        
        self.balance -= amount

#print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print(self.int_rate)
        print(f"Balance: {self.balance}")

#increases the account balance by the current balance * the interest rate 
#(as long as the balance is positive)
    def yield_interest(self):
        self.yield_interest = balance * (1-amount)

#create 2 accounts
Checkings = BankAccount("Checkings", 1% , 100)
Savings = BankAccount("Savings", 1% , 10,000)

Checkings.display_account_info().deposit().deposit().deposit().withdraw().yield_interest().balance().display_account_info()
Savings.display_account_info().deposit().deposit().withdraw().withdraw().withdraw().withdraw().yield_interest().balance().display_account_info()
