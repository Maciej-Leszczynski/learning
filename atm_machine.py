from datetime import datetime

class Atm:
    """
    Simple class to represent ATM machine where you can
    check balance or history of transactions, deposit and
    withdraw money.
    """

    # history_of_transactions = []

    def __init__(self, name, pin):
        self.balance = 0
        self.loged = False
        self.history_of_transactions = []
        self.name = name
        # Pin number must be a string of 4 digits
        if len(pin) == 4 and pin.isdecimal():
            self.pin = pin
        else:
            raise ValueError("Invalid pin number.")

    def check_balance(self):
        """
        Method to check current balance of the account
        """
        if self.loged == False:
            return "You must to log in."
        return f"Your current balance is {self.balance}."

    def deposit(self, amount):
        """
        Method to deposit money in ATM. You can deposit
        maximum of $1k. You can't deposit negative amount.
        """
        if self.loged == False:
            return "You must to log in."        
        if amount > 1000 or amount < 0:
            raise ValueError("Amount of deposit must be positive value not higher than $1000.")
        self.balance += amount
        self.history_of_transactions.append({"Deposit":[datetime.now().strftime("%d/%m/%y %H:%M"), str(amount)]})

    def withdrawal(self, amount):
        """
        Method to withdraw money from ATM. You can withdraw
        maximum of $500.
        """        
        if self.loged == False:
            return "You must to log in."        
        if amount > self.balance:
            raise ValueError(f"Sorry you don't have enough money on your account to withdraw ${amount}.")
        elif amount > 500:
            raise ValueError("You can withdraw maximum of $500 in one transaction.")
        self.balance -= amount
        self.history_of_transactions.append({"Withdrawal":[datetime.now().strftime("%d/%m/%y %H:%M"), f"-{amount}"]})

    def get_history_of_transactions(self):
        """
        Method to check transactions of the user.
        """
        if self.loged == False:
            return "You must to log in."        
        for transaction in self.history_of_transactions:
            for key, value in transaction.items():
                print(f"{key} at: {value[0]}, amount {value[1]}")


class Customer(Atm):
    """Simple class to represent ATM machine customers"""

    def get_name(self):
        """
        Method to check name of the loged in user.
        """        
        if self.loged == False:
            return "You need to log in to get name."
        return f"Your customer name is {self.name}."
    
    def get_pin(self):
        """
        Method to check pin code of the loged in user.
        """
        if self.loged == False:
            return "You need to log in to get pin code."
        return f"Your pin code is {self.pin}."

    def change_pin(self, new_pin):
        """
        Method that alows user to change pin code.
        """
        if self.loged == False:
            return "You need to log in to change pin code."        
        elif len(new_pin) == 4:
            self.pin = new_pin
            return "Pin code changed."
        else:
            raise ValueError("Invalid pin number.")

    def log_in(self, pin):
        """
        Method that alows user to log in.
        """
        if pin == self.pin:
            self.loged = True
            return f"Welcome to your Virtual ATM {self.name}."
        else:
            return "Invalid pin code."
 