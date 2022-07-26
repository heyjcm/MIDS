#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 15:15:45 2021

@author: Christian Montecillo
"""

import os
import sys

'''The following helper_functions are for text for the game and for quitting
and ending the game. There is also a clear_screen function because I use the
os.system command enough times that it warranted its own easy-to-use/remember
function
'''

def mids_credits():
    print(
        'Millennial Into Drug Sales\n'
        'A game based on a game based on the New York Drug Market.\n\n'

        'By Christian Montecillo\n'
        'Inspired by the game "Drug Wars" by John E. Dell (1984)\n\n'

        'An emulator of the original game can be found here:\n'
        'https://classicreload.com/drug-wars.html\n'
        )

def instructions():
    clear_screen()
    print(
        'This is a game of buying and selling drugs\n'
        '(so you can afford to go to Berkeley).\n\n'

        'You\'re a small-time drug dealer wanting to change\n'
        'your profession by becoming a data scientist.\n\n'

        'Congratulations! You just got accepted to UC Berkeley\'s\n'
        'prestigious MIDS program!\n\n'

        'Today is July 1st, 2021 and your entire $75,000 tuition\n'
        'is due on August 1st for the Fall. With only $2,000 to your name\n'
        'and no hope of getting student loans, the odds seem\n'
        'impossible. Did I mention that you\'re also in debt to a loan\n'
        'shark because you\'ve made some quetsionable decisions in the past??\n\n'

        'To raise enough funds to pay tuition, you\n'
        'decide to do what you do best:\n\n\n'

        'Slangin\'!!!'
        )

    input('\nPress [Enter] key to continue ')
    clear_screen()

    print(
        'The objective of the game is to pay off your $5500 debt to\n'
        'the loan shark (who lives in The Bronx) while making enough money\n'
        'to pay off your tuition bill by the end of the month.\n\n'

        'Don\'t forget: the loan shark charges 10% interest\n'
        'per day and you already owe him $5500!!!\n\n'
        'Good luck!\n'
        )

def quitting():
    clear_screen()
    print(
        'Because you quit, you can\'t go to Berkeley.\n'
        'You decide not to be a data scientist.\n'
        '"Just as well", you say. "I don\'t understand classes and inheritance anyway."\n\n'
        'That\'s so sad for you!\n'
        )

def end_game():
    sys.exit()

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
