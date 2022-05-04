class BankAccount:
    bank_name = "Doge Inc."

    def __init__(self, interest_rate, balance):
        self.balance = 0
        self.interest_rate = .01

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, minus_amount):
        if self.balance < minus_amount:
            self.balance += (-5)
            print( "Insufficient funds: Charging a $5 fee" )
        elif self.balance >= minus_amount:
            self.balance += (-minus_amount)
        return self

    def display_account_info(User):
        print(f'Balance = ${User.account.balance}')
        return User

    def yield_interest(self):
        current_balance = self.balance
        if current_balance > 0:
            self.balance += current_balance*self.interest_rate
        return self

# ------------------------------------------------------------------------- #

class User:
    bank_name = "First National Dojo"

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount (.01 , 0)

    def make_deposit(self, amount):
        self.account.balance += amount

    def make_withdrawal(self, minus_amount):
        self.account.balance += (-minus_amount)
    
    def display_user_balance(self):
        print(f'{self.name} - Balance = ${self.account.balance}')
    
    def display_user_information(self):
        print(f'{self.name} - Email address: {self.email} - Balance: ${self.account.balance} ')


guido = User("Guido van Russom","guido@python.com")
monty = User("Monty Python","monty@python.com")
JoJo = User("Jojo Burst","jj@python.com")


guido.account.deposit(10).withdrawal(11)


guido.display_user_balance()
print('------------------------------------------------')
guido.display_user_information()