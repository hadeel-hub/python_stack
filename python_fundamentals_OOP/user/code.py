class User:
    def __init__(self,name):
        self.name= name
        self.account_balance=0
        
    def make_deposit(self,amount):
        self.account_balance+= amount
    def make_withdrawl(self,amount):
        self.account_balance-= amount
        
rabab=User("Rabab")
hadeel=User("Hadeel")
maryam=User("Maryam")
rabab.make_deposit(1000)
rabab.make_deposit(1000)
rabab.make_deposit(1000)
hadeel.make_deposit(300)
hadeel.make_deposit(400)
hadeel.make_withdrawl(100)
hadeel.make_withdrawl(1000)
print(rabab.account_balance) 
print(hadeel.account_balance)
print(rabab.account_balance)

    