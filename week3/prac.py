class BankAccount:
    no_of_acc = 0

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        self.history = []

        BankAccount.no_of_acc += 1

    def __str__(self):
        return f'{self.owner}"s account : balance = {self.balance}'

    def deposit(self,amount):
        if amount <= 0:
            print('Amount must be positive')
            return
        self.balance += amount
        self.history.append(f'Deposited: {amount}')

    def withdraw(self,amount):
        if amount < 0:
            print('Amount must be positive')
            return
        if amount > self.balance:
            print('Insufficient balance')
            return 
        self.balance -= amount
        self.history.append(f'Withdrew: {amount}')

    def transfer(self,other_acc,amount):
        if amount < 0:
            print('Amount must be positive')
            return
        if amount > self.balance:
            print('Insufficient balance')
            return 
        self.balance -= amount
        other_acc.balance += amount
        self.history.append(f'Transferred {amount} to {other_acc.owner}')
        other_acc.history.append(f'Recieved {amount} from {self.owner}')

    def show_details(self):
        for entries in self.history:
            print(entries)


acc1 = BankAccount('Raj', 20000)
acc2 = BankAccount('Priya', 30000)
acc3 = BankAccount('Rahul', 40000)
acc4 = BankAccount('Neha',10000)

acc1.deposit(200)
acc2.withdraw(40)
acc3.transfer(acc4, 3000)
acc4.deposit(70)


print(acc1.history)

print(acc2.history)

print(acc3.history)

print(acc4.history)   

        
