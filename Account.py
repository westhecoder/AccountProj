# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:30:07 2020

@author: pc
"""

class Account:
    '''
    Inputs: Account Number, Name, Surname, TimeZome,Balance >= 0,
    '''
    mir = 1.05 #Monthly interest rate
    
    def __init__(self, name, surname, account_num, timezone = 'CAT', balance = 0):
        self._name = name
        self._surname = surname
        self._account_num = account_num
        self._tmz = timezone
        self._balance = balance
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def surname(self):
        return self._surname
    
    @surname.setter
    def surname(self, value):
        self._surname = value
    
    @property
    def account_number(self):
        return self._account_num
    
    @property
    def tmz(self):
        return self._tmz
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, value):
        if value >= 0:
            self._balance = self._balance + value 
            
    def withdraw(self, amount):
        print("Withdrawing money...")
        if amount > self._balance:
            print(f"DECLINED!!, {amount} is unavailable")
        else:
            self._balance = self._balance - amount
            print(f"Successful!! New Balance is: {self._balance}")
            
    def interest(self):
        return self._balance * self.mir
        
    
    def __repr__(self):
        return f'Name: {self._name} {self._surname} \nAccount Number: {self._account_num}\nAccount Balance: {self._balance} \nTime Zone: {self._tmz}'

a = Account('Wesley', 'Musekiwa', 23454, 'EAT', 34)
b = Account('Ucal', 'Musekiwa', 23455, 'CAT', 50)

print('#'*25)
print(a)
print('#'*25)

print('#'*25)
print(b)
print('#'*25)

a.deposit(50)
print(a.balance)

a.withdraw(100)

print(a.balance)

print(a.interest())























































