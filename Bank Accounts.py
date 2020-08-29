class Account():
    
    def __init__(self,owner,balance):
        
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        
        return (f"Account owner: {self.owner} \nFunds Available: {self.balance}")
    
    def deposit(self, amount):
        
        self.balance = self.balance + amount
        return print("Deposit Successful")

    def withdrawal(self,amount):
        
         if self.balance < amount:
                return "Insufficient Funds!"
         else:
                self.balance = self.balance - amount
            
                return f"Withdrawal successful. New balance: {self.balance}"
            

my_account = Account("Diego",1000)

my_account.deposit(10000)

print(my_account.balance)


print(my_account.withdrawal(10000))



