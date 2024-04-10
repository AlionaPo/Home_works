# 1. Write a test for the Bank class that we wrote in 14 lesson.
#    You should write a test for the open_account method.
#    Ensure that the account is opened and has balance.
account_number = 1234567
balance = 500
amount = 100

class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number
    
    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account_number
    
    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'
    
def test_account(self, account_balance, bank_account):
    account_balance = Account.get_balance()
    bank_account = Account.get_account_number()
    assert account_balance > 0 
    assert bank_account == account_number

# 2. Test update method. It should check that code added interest and 
#    sent a message (print function was called).

def test_update(self, new_balance):
    account = Account.create_account(account_number)
    origin_balance = account.get_balance()
    account.deposit(amount)
    new_balance = account.get_balance()
    assert new_balance > origin_balance
    print("Interest added successfully")

test_update(None, None)
