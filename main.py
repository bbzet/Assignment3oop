from PersonalAccount import PersonalAccount

if __name__ == '__main__':
    account1 = PersonalAccount(123456, 'Baiastan Zamirbekov')
    account1.deposit(1000)
    account1.withdraw(500)
    account1.print_transaction_history()
    print(account1.get_balance())

    print(f'Account number: {account1.get_account_number()}')
    account1.set_account_number('987652')
    print(f'After changing the account number {account1.get_account_number()}')

    print(f'Account holder: {account1.get_account_holder()}')
    account1.set_account_holder('Baiastan')
    print(f'After changing account holder: {account1.get_account_holder()}')

    account1.__str__()

    account1.__add__(200)

    account1.__sub__(100)

    print(account1.get_balance())


