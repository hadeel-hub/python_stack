

from unicodedata import name


class BankAccount:
    def __init__(self,name,account_balance, int_rate):
      self.name= name
      self.account_balance=0
      self.int_rate=0.01
      
    def deposit(self,amount):
      self.account_balance+=amount
      return self
    def withdraw(self,amount):
      self.account_balance-=amount
      return self
    
    def displayAccountInfo(self):
      print(self.account_balance)
    def yield_interest(self):
      self.account_balance= self. account_balance+(self.account_balance* self.int_rate)
      print(self.account_balance)
      
      
aseel=BankAccount(name,0,0.01)
hadeel=BankAccount(name,0,0.01)

aseel.deposit(1000).withdraw(500).withdraw(40).displayAccountInfo()
hadeel.deposit(1500).withdraw(200).withdraw(70).displayAccountInfo()
  