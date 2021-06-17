class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self.acnt = acnt
        self.customer = customer
        self.bank = bank
        self.limit = limit
        self.balance = 0
    def __repr__(self):
        return f'CreditCard->{self.customer} {self.bank} {self.acnt} {self.limit} {self.balance}'
    @staticmethod
    def is_numeric(value):
        return type(value) == type(1) or type(value) == type(1.0)
    def get_customer(self):
        return self.customer
    def get_bank(self):
        return self.bank
    def get_account(self):
        return self.acnt
    def get_limit(self):
        return self.limit
    def get_balance(self):
        return self.balance
    def charge(self, price):
        if not self.is_numeric(price):
            raise TypeError('price must be int or float')
        self.balance += price
    def make_payment(self, amount):
        if not self.is_numeric(amount):
            raise TypeError('price must be int or float')
        if amount < 0:
            raise ValueError('Amount cannot be negative')
        self.balance -= amount

if __name__ == '__main__':
    card = CreditCard('Hendri','BCA','12123123332',112)
    card.make_payment(-332)