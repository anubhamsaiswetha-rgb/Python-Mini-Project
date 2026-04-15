class bankaccount:
    def __init__(self, name, balance):
        self.name=name
        self.__balance=balance #pvt variable
#getter
    def get_balance(self):
        return self.__balance
#setter
    def deposit(self, amount):
        if amount >0:
            self.__balance +=amount
            print("Amount Deposited:",amount)
        else:
            print("invalidd amount")
#withdraw
    def withdraw(self,amount):
        if amount <=self.__balance:
            self.__balance -=amount
            print("amount withdrawed:",amount)
        else:
            print("insufficient balance")
        
#inheritence
class ATM(bankaccount):
    def show_details(self):
        print("\n---Account Details---")
        print("name:", self.name)
        print("balance:", self.get_balance())
#test
acc = ATM("sai swetha",1300)
acc.show_details()
acc.deposit(300)
acc.withdraw(400)
acc.show_details()
