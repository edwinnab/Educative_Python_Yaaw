#implement a Banking Acoount
class Account:
    def __init__(self, title = None, balance = 0):
        self.title = title
        self.balance = balance
        #calculates witdrawal
    def withdrawal(self, amount):
        self.amount = amount
        self.balance = self.balance - self.amount
        #calculates deposits
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
    #gets current balance
    def getBalance(self):
        return self.balance

#child class
class SavingsAccount(Account):
    def __init__(self, title = None, balance = 0, intrestRate = 0):
        super().__init__(title, balance)
        self.intrestRate = intrestRate
    #calculates interest rate
    def interestAmount(self):
        return ((self.intrestRate * self.getBalance())/100)
#object
client_one = SavingsAccount("Edwinna", 2300, 5)
print(client_one.interestAmount())
client_one.withdrawal(500)
print(client_one.getBalance())
client_one.deposit(3000)
print(client_one.getBalance())

    