class Bank:
    def __init__(self,balance):
        self.__balance = balance   # ex. 100

    def __deposite(self,amount):
        self.__balance += amount   # ex. 100+200

    def get_balance(self):
        print(self.__balance)

    def add_money(self,amount):
        self.__deposite(amount)


    
# __balance is a private varible, if u call directly we will get an error
# __deposite is a private mathod(ecause while defining method we have used __methodname.),if u call directly we will get an error.
# get_balance and add_money are public methods(ecause while defining method we have not used __methodname.).