'''class BankAccount:

    def __init__(self, name, balance):
        self.balance = balance
        self.name = name
acc1= BankAccount("Pappu",10000)
acc1.balance=1000000
print(acc1.name, acc1.balance)
'''

class BankAccount:

    def __init__(self, name, balance):
        self.__balance = balance # making it private veriable 
        self.name = name

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        if  amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdraw")

acc1= BankAccount("Pappu",10000)
print("1st deposit- ",acc1.get_balance())
acc1.__balance=100000
acc1.deposit(5000)
print("depost-5000",  acc1.get_balance())
acc1.withdraw(3000)
print("after withdraw-3000", acc1.get_balance())
print(acc1.name, acc1.get_balance())


#data & methon bind togheter in class 
#restrict direct accessing 

#public 
#self.balence

#restrict
#self._balence

#Private
#self.__balence

