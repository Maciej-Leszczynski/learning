from datetime import datetime

class Atm:
    """ Simple class to represent ATM machine """

    history_of_transactions = []

    def __init__(self, name, pin):
        self.balance = 0
        self.name = name
        if len(pin) == 4:
            self.pin = pin
        else:
            raise ValueError("Invalid pin number.")

    def check_balance(self):
        if Customer.loged == False:
            return "You must to log in."
        return f"Your current balance is {self.balance}."

    def deposit(self, amount):
        if Customer.loged == False:
            return "You must to log in."        
        if amount > 1000 or amount < 0:
            raise ValueError("Amount of deposit must be positive value not higher than $1000.")
        self.balance += amount
        Atm.history_of_transactions.append({"Deposit":[datetime.now().strftime("%d/%m/%y %H:%M"), str(amount)]})

    def withdrawal(self, amount):
        if Customer.loged == False:
            return "You must to log in."        
        if amount > self.balance:
            raise ValueError(f"Sorry you don't have enough money on your account to withdraw ${amount}.")
        elif amount > 500:
            raise ValueError("You can withdraw maximum of $500 in one transaction.")
        self.balance -= amount
        Atm.history_of_transactions.append({"Withdrawal":[datetime.now().strftime("%d/%m/%y %H:%M"), f"-{amount}"]})

    def get_history_of_transactions(self):
        if Customer.loged == False:
            return "You must to log in."        
        for transaction in Atm.history_of_transactions:
            for key, value in transaction.items():
                print(f"{key} at: {value[0]}, amount {value[1]}")


class Customer(Atm):
    """Simple class to represent ATM machine customers"""

    loged = False

    def get_name(self):
        if Customer.loged == False:
            return "You need to log in to get name."
        return f"Your customer name is {self.name}."
    
    def get_pin(self):
        if Customer.loged == False:
            return "You need to log in to get pin code."
        return f"Your pin code is {self.pin}."

    def change_pin(self, new_pin):
        if Customer.loged == False:
            return "You need to log in to change pin code."        
        elif len(new_pin) == 4:
            self.pin = new_pin
            return "Pin code changed."
        else:
            raise ValueError("Invalid pin number.")

    def log_in(self, pin):
        if pin == self.pin:
            Customer.loged = True
            return f"Welcome to your Virtual ATM {self.name}."
        else:
            return "Invalid pin code."



if __name__ == "__main__":
    maciek = Customer("Maciek", '1234')
    print(maciek.check_balance())
    print(maciek.log_in('1234'))
    print(maciek.check_balance())
    print(maciek.get_pin())
    print(maciek.change_pin('4321'))
    print(maciek.get_pin())
    maciek.deposit(1000)
    maciek.withdrawal(40)
    maciek.withdrawal(110)
    maciek.withdrawal(35)
    maciek.get_history_of_transactions()  