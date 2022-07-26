#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 08:13:24 2021

@author: Christian Montecillo
"""

import random


class Drug:
    '''
    Description:
    Drug class that gets created for each drug that gets passed to it.

    Parameters:
    drug_name - the name of the drug
    low_price and high_price - range of prices of the drug (if high_price < low_price: function switches the parameters)
    '''
    def __init__(self, drug_name, low_price, high_price):
        if low_price < high_price:
            self.low_price = low_price
            self.high_price = high_price
        else:
            self.low_price = high_price
            self.high_price = low_price
        self.drug_name = drug_name
        self.market_price = random.randint(low_price, high_price)
        self.quantity = 0

    @property
    def name_and_price(self):
        '''getter method for returning the drug_name and market_price
        in a tuple format
        '''
        return (self.drug_name, self.market_price)

    @property
    def name_and_quantity(self):
        '''getter method for returning the drug_name and drug quantity'''
        return (self.drug_name, self.quantity)

    def __str__(self):
        return f'{self.drug_name}'.rjust(10).ljust(11) + f'${self.low_price}-${self.high_price}'

    def __repr__(self):
        return f'Drug({self.drug_name}, low price: ${self.low_price}, high price: ${self.high_price}, market price: ${self.market_price}, quantity: {self.quantity})'


def make_drugs():
    '''Makes all the drugs using the list_of_drugs'''
    # make all the drugs!
    # (name, low price, high price)
    list_of_drugs = [
        ('Cocaine', 15000, 30000),
        ('Heroin', 5000, 14000),
        ('MDMA', 1000, 4500),
        ('LSD', 300, 900),
        ('Shrooms', 70, 250),
        ('Adderall', 10, 60)
        ]

    return [Drug(name, low, high) for name, low, high in list_of_drugs]
