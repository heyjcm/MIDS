#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 13:05:41 2021

@author: Christian Montecillo
"""

import datetime
import os

class HUD:
    '''Heads up Display for Player so they know the status within the game
    Takes in Stash and TrenchCoat object to display those attributes. Also
    takes a neighborhood name to display that
    '''
    def __init__(self, stash_obj, trench_coat_obj, hood_name):
        self.stash_obj = stash_obj
        self.trench_coat_obj = trench_coat_obj
        self.hood_name = hood_name
        self.current_date = datetime.date.fromisoformat("2021-07-01")

    def show_display(self):
        os.system('cls' if os.name=='nt' else 'clear')

        print(
            '',
            '|' + 70 * '=' + '|\n',
            '| Date: ' + f'{self.current_date}'.ljust(20) + f'Hood: {self.hood_name}'.ljust(25) + f'Capacity: {self.trench_coat_obj.capacity}'.ljust(18) + '|\n',
            '|'.ljust(71) + '|\n',
            '|' + 'Stash'.rjust(10).ljust(50) + 'Trench Coat'.ljust(20) + '|\n',
            '| Cocaine: ' + f'{self.stash_obj.drugs_list[0].quantity}'.rjust(6).ljust(39) + 'Cocaine:' + f'{self.trench_coat_obj.drugs_list[0].quantity}'.rjust(6).ljust(13) + '|\n',
            '| Heroin: ' + f'{self.stash_obj.drugs_list[1].quantity}'.rjust(7).ljust(40) + 'Heroin:' + f'{self.trench_coat_obj.drugs_list[1].quantity}'.rjust(7).ljust(14) + '|\n',
            '| MDMA: ' + f'{self.stash_obj.drugs_list[2].quantity}'.rjust(9).ljust(42) + 'MDMA:' + f'{self.trench_coat_obj.drugs_list[2].quantity}'.rjust(9).ljust(16) + '|\n',
            '| LSD: ' + f'{self.stash_obj.drugs_list[3].quantity}'.rjust(10).ljust(43) + 'LSD:' + f'{self.trench_coat_obj.drugs_list[3].quantity}'.rjust(10).ljust(17) + '|\n',
            '| Shrooms: ' + f'{self.stash_obj.drugs_list[4].quantity}'.rjust(6).ljust(39) + 'Shrooms:' + f'{self.trench_coat_obj.drugs_list[4].quantity}'.rjust(6).ljust(13) + '|\n',
            '| Adderall: ' + f'{self.stash_obj.drugs_list[5].quantity}'.rjust(5).ljust(38) + 'Adderall:' + f'{self.trench_coat_obj.drugs_list[5].quantity}'.rjust(5).ljust(12) + '|\n',
            '|'.ljust(71) + '|\n',
            '| Bank:' + f'${self.stash_obj.bank}'.rjust(10).ljust(43) + 'Guns:' + f'{self.trench_coat_obj.guns}'.rjust(9).ljust(16) + '|\n',
            '| Debt:' + f'${self.stash_obj.debt}'.rjust(10).ljust(43) + 'Cash:' + f'${self.trench_coat_obj.cash}'.rjust(9).ljust(16) + '|\n',
            '|' + 70 * '=' + '|\n',
            )

    def increment_date(self):
        self.current_date += datetime.timedelta(days=1)

    def change_hood(self, new_hood):
        self.hood_name = new_hood