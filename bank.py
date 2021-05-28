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
