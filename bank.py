class Bank:
    name= "Bank of Africa"

    def __init__(self,id,accountNumber,accountType,branch):
        self.id= id
        self.accountNumber= accountNumber
        self.accountType= accountType
        self.branch= branch

    def withdraw(self):
        return f"I went to the bank and was told to provide my id which was {self.id} and my account number which was{self.accountNumber} they then asked me if I would like to open a {self.accountType} in the {self.branch} branch "
    def deposit(self):
        return f"She went to the bank branch in {self.branch} she was told to provide her account number which is{self.accountNumber} and her id which is {self.id} she was then told to open a{self.accountType}"
class Account: 
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0
        self.loan=0
        self.loan_limit=500

    def deposit(self,amount):
        if amount<=0:
            return f"Amount must be greater than 0."  
        else:
            self.balance+=amount
            return f"Dear {self.name} you have deposited {amount},your new balance is KSH{self.balance}"
    def show_balance(self):
        return self.balance
    def withdraw(self,amount):
        if amount<=0:
            return f"Dear {self.name} the amount to be withdrawn must be greater than zero"
        elif amount>self.balance:
            return f"Dear {self.name} You can not withdraw KES {amount}, your balance of {self.balance} is insufficient"
        else:
            self.balance-=amount
            return f" Dear {self.name}, you have withdrawn {amount} ,your balance is KES{self.balance}"

    def borrow(self,amount):
        if amount<=self.loan_limit:
            self.loan+=amount
            self.balance+=self.loan
            return f"Dear {self.name}, you have borrowed KES{amount}.Your loan of {self.loan} is due December 21st, your balance is KES{self.balance}"
        else:
            return f"Your loan request of KES{amount} is unsuccessful because your loan limit is {self.loan_limit} "
