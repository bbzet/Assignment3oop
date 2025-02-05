from Amount import Amount

class PersonalAccount:
    def __init__(self, account_number, account_holder):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print('To your balance deposited: ', amount)
            transaction = Amount(amount, "DEPOSIT")
            self.transactions.append(transaction)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print('From your balance withdrawn: ', amount)
            transaction = Amount(amount, "WITHDRAWAL")
            self.transactions.append(transaction)
        elif amount > self.__balance:
            print("Your balance is not enough.")
        else:
            print('Withdrawal amount must be positive.')

    def print_transaction_history(self):
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_account_holder(self):
        return self.__account_holder

    def set_account_holder(self, account_holder):
        self.__account_holder = account_holder

    def __str__(self):
        return f"Account {self.__account_number} - Holder: {self.__account_holder} - Balance: {self.__balance}"

    def __add__(self, amount):
        if amount > 0:
            self.__balance += amount
            print('To your balance added: ', amount)
        else:
            print('Deposit muct be positive')

    def __sub__(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print('From your balance substracted: ', amount)
        else:
            print('Your balance is not enough')