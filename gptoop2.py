class BankAccount:
    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self.account_balance = balance
        self.start_balance = balance
        if self.account_balance < 0:
            raise ValueError('Рахунок не може мати таке значення!')
        
    def deposit(self, deposit_value):
        self.account_balance += deposit_value
    
    def withdraw(self, withdraw_value):
        self.account_balance -= withdraw_value
        if self.account_balance < 0:
            self.account_balance = self.start_balance
            raise ValueError('Недостатньо коштів')
            
    def transfer(self,another_account, transfer_value):
        self.withdraw(transfer_value)
        if self.account_balance < 0:
            self.account_balance = self.start_balance
            raise ValueError('Недостатньо коштів')
        another_account.deposit(transfer_value)
    def get_balance(self):
        return self.account_balance
        
try:
    user_account_01 = BankAccount('Ірина', 1000)
    user_account_02 = BankAccount('Єлизавета', 2000)
    user_account_01.transfer(user_account_02, 500)
    print(user_account_01.get_balance(), user_account_02.get_balance())
except ValueError as e:
    print(e)