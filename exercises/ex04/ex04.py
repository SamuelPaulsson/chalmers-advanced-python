## Question 1: defining classes

class Account:
    # an account has a number and a balance
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance

    def get_balance(self):
        # return the actual balance
        return self.balance

    def get_number(self):
        return self.number

    def set_balance(self, b):
        # change the balance to b
        self.balance = b

def transfer(account1,account2,amount):
    balance1 = account1.get_balance()
    if amount > balance1:
        print('not enugh balance')
    else:
        account1.set_balance(balance1-amount)
        account2.set_balance(account2.ger_balance()+amount)

a = Account(1, 300)
b = Account(2,200)

transfer(a,b, 200)

    # transfer amount from account1 to account2
    # report "OK" if successful, i.e. account1 has the required amount
    # "not enough money" otherwise

## Question 2 and 3: trees
import sys
sys.path.append("../../examples")
from trees import *

class RecTree:
    def __init__(self, r, ts):
        self._root = r
        self._subtrees = ts

    def parts(self):
        return self._root, self._subtrees
    
    def edges(self):
        pass
    
    def to_tree(self):
        pass

    def to_valtree(self):
        pass

def atom(a):
    pass

import graphviz

def visualize_vals(graph):
    pass

## Question 4: function composition
