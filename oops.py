class Bank_Account ():
    def __init__(self, name, age, adress, type, balance):
        self.name = name
        self.age = age
        self.adress = adress
        self.type = type
        self.balance = balance
    def withdraw (self):
        q1 = int(input("How much would you like to withdraw?"))
        if self.balance >= q1:
            self.balance -= q1
        print (f"The balance has been subtracted: ${self.balance}")
    def deposit(self):
        q2 = int(input("How much would you like to deposit?"))
        self.balance += q2
        print (f"The balance has been added: ${self.balance}")
    def change_details(self):
        q3 = int(input("What detail would you like to change? 1. Name, 2. Age, 3. Adress"))
        if q3 == 1:
            self.name = (input("Enter your new name."))
        elif q3 == 2:
            self.age = (input("Enter your new age."))
        elif q3 == 3:
            self.adress = (input("Enter you new adress."))
Bank_Acc_1 = Bank_Account ("Rithvik", 15, "10845 238th Terrace Ave", "savings", 0)
print (Bank_Acc_1.balance)
Bank_Acc_1.deposit ()