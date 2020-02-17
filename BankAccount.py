import random

taken_acc_nums = []
time = 0
failwhale = True


class BankMain():
    def __init__(self):
        self.accounts = []

    def add_acc(self, account):
        self.accounts.append(account)

    def print_accs(self):
        print('\n List of all accounts:')
        for acc in self.accounts:
            print(acc)


class BankAccount():
    interest = 3.5

    def __init__(self, owner, currency, amount):
        if amount.count('.'):
            print('Smallest acceptable denominator is 1')
            return
        else:
            global failwhale
            failwhale = False

        random_num = random.randint(100000, 999999)
        while taken_acc_nums.count(random_num):
            random_num = random.randint(100000, 999999)
        self.acc_num = random_num
        taken_acc_nums.append(self.acc_num)
        self.owner = owner
        self.money = int(amount)
        self.currency = currency

    def add_that_dough(self, amount):
        self.money += int(amount)

    def withdrawing(self, amount):
        self.money -= int(amount)

    def __str__(self):
        return f'Account number: {self.acc_num}\n Owner: {self.owner}\n Savings: {self.currency}{round(self.money, 2)}'

    def interest_accumulation(self):
        rate = self.interest / 100
        self.money += self.money*(rate)


while failwhale:
    acc_1 = BankAccount(
        input('Name: '), input('Currency:'), input('Amount:'))

acc_1.add_that_dough(250)
acc_1.withdrawing(35)

failwhale = True
while failwhale:
    acc_2 = BankAccount(
        input('Name: '), input('Currency:'), input('Amount:'))


big_bank = BankMain()

big_bank.add_acc(acc_1)
big_bank.add_acc(acc_2)

while time < 3:
    for account in big_bank.accounts:
        account.interest_accumulation()
    time += 1


big_bank.print_accs()
