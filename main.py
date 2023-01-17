"""
 *Construct a class for bank accounts.
 *Have at least 3 variables
 *Have a constructor
 *Have at least 3 methods including a str, withdraw, deposit,steal
 *Create 3 objects and test the methods above
"""


class Bank:

    def __init__(self, name, identity: int, balance: int, checking: int):
        self.accountName = name
        self.accountID = identity
        self.amount = balance
        self.pocket = checking

    def __add__(self, deposit):
        self.amount += deposit

    def __withdraw__(self, withdrawal):
        self.amount -= withdrawal
        self.pocket += withdrawal

    def __steal__(self, stole):
        self.amount -= stole

    def __str__(self):
        return f"(Hi {self.accountName}, your account ID is {self.accountID}. Current Balance: {self.amount}. Current Checking Balance: {self.pocket})"

person1 = Bank("Wave", 12321, 50000, 0)
print(person1)
person1.__add__(50)
print(person1.amount)
person1.__withdraw__(1200)
print(person1.pocket)
person1.__steal__(500)
print(person1.amount)
person1.__add__(2800)
print(person1.amount)
person1.__withdraw__(200)
print(person1.pocket)
print(person1)
