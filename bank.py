from datetime import datetime, time
class Bank:
    name= "Bank of Africa"

    def __init__(self,id,accountNumber,accountType,branch):
        self.id= id
        self.accountNumber= accountNumber
        self.accountType= accountType
        self.branch= branch
        self.transaction= [];

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
        self.transactions= [];


    def deposit(self,amount):
        try:
            11+ amount
        except TypeError:
            return f"The amount must be in figures"    
        if amount<=0:
            return f"Amount must be greater than 0."  
        else:
            self.balance+=amount
            transaction= {"amount": amount,
                      "balance": self.balance,
                      "time": datetime.now(),
                      "narration": "Deposited"}
            self.transactions.append(transaction)
       
            return f"Dear {self.name} you have deposited {amount},your new balance is KSH{self.balance}"
    def show_balance(self):
        return self.balance
    def withdraw(self,amount):

        try:
            11+ amount
        except TypeError:
            return f"The amount must be in figures" 

        if amount<=0:
            return f"Dear {self.name} the amount to be withdrawn must be greater than zero"
        elif amount>self.balance:
            return f"Dear {self.name} You can not withdraw KES {amount}, your balance of {self.balance} is insufficient"
        else:
            self.balance-=amount
            return f" Dear {self.name}, you have withdrawn {amount} ,your balance is KES{self.balance}"

    def borrow(self,amount):

        try:
            11+ amount
        except TypeError:
            return f"The amount must be in figures" 
             
        if amount<=self.loan_limit:
            self.loan+=amount
            self.balance+=self.loan
            return f"Dear {self.name}, you have borrowed KES{amount}.Your loan of {self.loan} is due December 21st, your balance is KES{self.balance}"
        else:
            return f"Your loan request of KES{amount} is unsuccessful because your loan limit is {self.loan_limit} "

    def get_statement(self):
        for transaction in self.transactions:
            narration = transaction["narration"]
            amount = transaction["amount"]
            balance = transaction["balance"]
            time = transaction["time"]
            print(f'{time.strftime("%D")} date of transaction. {narration} to your account, is the amount {amount} and now your balance is {balance}')
            
  
    def repay_loan(self,amount):
        
        
          if amount < 0:
              return f"Dear {self.name} you have been loaned an amount of {amount} your new balance is {self.balance}"

          elif amount < self.loan:
              self.loan-=amount
              return f"Dear customer,you have paid your debt of {amount} your outstanding debt is {self.loan} "

          else:
              difference = amount-self.loan
              self.balance+=difference
              self.loan = 0
              return f"Dear customer, you have succesfully paid your loan of {self.loan}, your new balance is{self.balance}"


    def transfer(self,amount,account):
        try:
            11+ amount
        except TypeError:
            return f"The amount must be in figures" 
        fee= amount*0.05
        if amount< 0 :
            return f"the amount must be greater than zero"
        
        elif amount+fee>self.balance:
            return f"Your balance is {self.balance}, you need {amount+fee}"
        else:
            self.balance-=amount+fee
            account.deposit(amount)
            return f"Your new balance is {self.balance}"  


class MobilemoneyAccount(Account):
  def __init__(self, accountnumber, name, phone, loan_limit,service_provider):
      super().__init__(accountnumber, name, phone, loan_limit)
      self.service_provider=service_provider
      self.limit=300000
  def buy_airtime(self,amount):
    try:
           10+amount
    except TypeError:
        return f"The amount must be in figures" 
    if amount<0:
      return 'figures should not be positive' 
    elif amount>self.balance:
      return "You have insufficient credit to make purchase "
    else:
      self.balance-=amount
      return f"Dear {self.name}, you have bought {amount} worth of airtime. Your new balance is {self.balance}"       
        
        
         


            
         