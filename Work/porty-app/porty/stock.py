# stock.py
#
# Exercise 4.1

from .typedproperty import String, Integer, Float

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
    def __repr__(self):
        return f"Stock('{self.name}',{self.shares:d},{self.price:0.2f})"
    @property
    def cost(self):
        '''
        Return the cost as shares * price
        '''
        return self.shares * self.price
    def sell(self,units):
        '''
        Sell a number of shares and return the remaining number.
        '''
        self.shares -= units
