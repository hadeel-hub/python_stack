 class BankAccount:
    def __init__(self,name, account_balance, int_rate):
      self.name= name
      self.account_balance=account_balance
      self.int_rate=int_rate
      
    def deposit(self,amount):
      self.account_balance+=amount
      return self
    def withdraw(self,amount):
      self.account_balance-=amount
      return self
    
    def displayAccountInfo(self):
      print(self.account_balance)
    def yield_interest(self):
      self.account_balance=self. account_balance+(self.account_balance*self.int_rate)
      print(self.account_balance)

class User:
    def __init__(self,name):
        self.name= name
        self.account=BankAccount(int_rate=0.01, account_balance=0)

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self,amount):
        self.account.withdraw(amount)
        return self
    def displayUser_account_balance(self):
      self.account.displayAccountInfo()
      
     