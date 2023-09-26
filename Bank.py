
class Bank:
    def __init__(self):
        self.balance = 10000
        self.interest_rate = 0.03
    
    def deposit(self, inskudd):
        self.inskudd = inskudd
        self.balance = self.balance + inskudd

        if self.balance >= 10000000:
            print(f"Congratulations, because of your high income you get a higher interest!")
            self.interest_rate = 0.05
    
    def __str__(self):
        return str(self.balance)
    
    def withdrawl(self, withdrawl_money):
        self.withdrawl_money = withdrawl_money

        if withdrawl_money <= self.balance:
            self.balance -= withdrawl_money
            print(f'You withddrew: {withdrawl_money}')
        else: 
            print(f'You cannot withdraw so much money... ')
    
    def calculating_interest(self):
        return self.balance * self.interest_rate
    
    def interest_and_balance(self):
        self.balance = self.balance + Bank.calculating_interest(self)

        if self.balance <= 8000:
            self.interest_rate = 0.01
        
        return self.balance

class Fond(Bank):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return str(self.balance)

    def fond(self):
        self.rents = 1.30
        self.sum = self.balance * self.rents
        print(f'Your current bank account with fond: {self.sum}')
    
    def high_risk(self):
            
        if self.balance >= 10000000:
            self.rents = 2.0
            self.balance = self.balance * self.rents
            print(f'You get 2.0 in rent! Your current fond is: {self.balance}')
            
        elif self.balance <= 6000000:
            self.rents = 1.50
            self.balance = self.balance * self.rents
            print(f'You have 1.50 in rent. Your current fond is: {self.balance}')
         
        else: 
            self.rents = 1.30
            self.balance = self.balance * self.rents
            print(f'You have the same rent as before. Your current fond is: {self.balance}')
        
        return self.balance

class Sparing(Bank):

    def __init__(self):
        super().__init__()
        self.sparing_list = list()
        self.current_saving = 0
        self.sparing_vacation = list()
        self.current_vacation = 0

    
    def __str__(self):
        return str(self.balance)
    
    def sparing(self):

        if self.balance > 100000:
            self.current_saving += 10000
            self.sparing_list.append(self.current_saving)
            print(f'My savings account currently have: {self.sparing_list}')
        
        elif self.balance < 100000:
            self.current_saving += 1000
            self.sparing_list.append(self.current_saving)
            print(f'My savings account currently have: {self.sparing_list}')
        
    def vacation(self):

        if self.balance >= 8000:
            self.current_vacation += 8000
            self.sparing_vacation.append(self.current_vacation)
            print(f'You have enough money to go on vacation. Money to spend on vacation: {self.current_vacation}. Have a good trip!')
        else:
            print(f'You do not have enough money to go on vacation. Your current bank account is {self.balance}')
            

min_bank = Bank()
print(f'My bank account: {min_bank}')
min_bank.deposit(200)
print(f'My bank account after deposit: {min_bank}')
min_bank.withdrawl(100)
print(f'My current bank account after withdrawl: {min_bank}')
print(f'Your interest of current bank account: {min_bank.calculating_interest()}')
print(f'You bank account with interest: {min_bank.interest_and_balance()}')

mitt_fond = Fond()
mitt_fond.fond()
mitt_fond.high_risk()

min_sparing = Sparing()
min_sparing.sparing()
min_sparing.vacation()
