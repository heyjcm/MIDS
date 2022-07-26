#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 13:13:15 2021

@author: Christian Montecillo
"""

import time
import random
import math
from helper import helper_functions as hf


class Container:
    '''Container class that is the base class for the TrenchCoat, Stash, and NewHood containers
    '''
    def __init__(self, container_name, drugs_list):
        self.drugs_list = drugs_list
        self.container_name = container_name


class TrenchCoat(Container):
    '''The TrenchCoat class keeps all the information about what the Player
    has with them as they travel through the different neighborhoods (e.g.,
    the type and quantity of drugs they have, and the cash on hand)
    '''
    def __init__(self, container_name, drugs_list):
        # when starting off, Player TrenchCoat has nothing but $2000
        # TrenchCoat can only hold 100 units of drug/gun items
        # A gun take up 5 TrenchCoat capacity
        super().__init__(container_name, drugs_list)

        self.capacity = 100
        self.guns = 0
        self.cash = 2000
        self.drugs_list = drugs_list


    def bought_drug(self, drug_element, quantity_to_buy, price):
        '''
        Description: Player buys drugs and stores into TrenchCoat
        Arguments:
        1. drug_element (maps to an index within the drug list)
        2. quantity they wish to buy
        3. price taken from current market price from the NewHood object
        '''
        self.drugs_list[drug_element].quantity += quantity_to_buy
        self.cash -= price * quantity_to_buy
        self.capacity -= quantity_to_buy

        print(f'\nYay! you bought {self.drugs_list[drug_element].drug_name}!!\n')
        time.sleep(2)

        # random chance events happen when buying drugs:
        # 1. nothing happens, everything goes smoothly
        # 2. some of the drugs are "bunk" and cannot be re-sold (e.g., buying
        # 5 units with 2 bunk = 3 drugs in your trench coat)
        # 3. the dealer accidentally gives you 1 to 3 extra units of drugs
        outcome = self.random_bought_event(quantity_to_buy)
        if outcome[0] == 0:
            print('You check your newly bought drugs and find that...\n')
            time.sleep(3)
            print('...all of it is in there! Score!')
            input('\nPress [Enter] key to continue ')
        elif outcome[0] == 1:
            verb_type = 'are' if outcome[1] > 1 else 'is'
            pronoun_type = 'them' if outcome[1] > 1 else 'that'
            time.sleep(3)
            print(f'...{outcome[1]} of them {verb_type} bunk and you can\'t sell {pronoun_type}! That sucks!!!')
            input('\nPress [Enter] key to continue ')
            self.drugs_list[drug_element].quantity -= outcome[1]
            self.capacity += outcome[1]

        else:
            time.sleep(3)
            print(f'...the dealer accidentally gave you {outcome[1]} extra! High five for bonus drugs (which don\'t affect your capacity)!!')
            input('\nPress [Enter] key to continue ')
            self.drugs_list[drug_element].quantity += outcome[1]

    def sold_drug(self, drug_element, quantity_to_sell, price):
        '''
        Description: Player sells drugs out of TrenchCoat
        Arguments:
        1. drug_element (maps to an index within the drug list)
        2. quantity_to_sell they wish to sell
        3. price taken from current market price from the NewHood object
        '''
        self.drugs_list[drug_element].quantity -= quantity_to_sell
        total_sale = price * quantity_to_sell
        self.cash += total_sale
        self.capacity += quantity_to_sell

        if self.capacity > 100:
            self.capacity = 100

        print(f'\nYay! you sold {self.drugs_list[drug_element].drug_name}!!\n')
        time.sleep(2)
        outcome = self.random_sold_event(price * quantity_to_sell)

        # random chance events happen when selling drugs (involved losing money):
        # 1. nothing happens, everything goes smoothly, you keep your money
        # 2. some % of Player's money blows away in the wind. The more money
        # is involved, the higher the percentage blows away in the wind
        # 3. Player gets tipped extra money due to good service
        if outcome[0] == 0:
            print('You count your money, when all of a sudden a big gust of wind...\n')
            time.sleep(3)
            print('...almost made you lose your cash! Luckily, you were holding it tightly.')
            input('\nPress [Enter] key to continue ')
        elif outcome[0] == 1:
            time.sleep(3)
            print(f'...blew away {int(outcome[1] * 100)}% of your sale!!! Bummer!!!')
            input('\nPress [Enter] key to continue ')
            self.cash -= math.ceil(total_sale * outcome[1])
        else:
            input('\nPress [Enter] key to continue ')
            self.cash += math.ceil(total_sale * outcome[1])

    def cash_trench_to_bank(self, deposit_amt):
        self.cash -= deposit_amt

    def withdraw_cash_from_bank(self, withdraw_amt):
        self.cash += withdraw_amt

    def cash_to_loan_shark(self, repay_amt):
        self.cash -= repay_amt

    def from_trench_coat(self, drug_element, quantity_to_stash):
        self.drugs_list[drug_element].quantity -= quantity_to_stash

    def from_stash(self, drug_element, quantity_to_pull):
        self.drugs_list[drug_element].quantity += quantity_to_pull

    def acquire_gun(self):
        '''I hope to implement this feature if I have time, but may have to
        wait until v2.0 release :)
        '''
        pass

    def random_bought_event(self, num_drugs_purchased):
        '''This function makes the game even more interesting by having a random
        chance event happen to Player with either negative or positive outcome
        when buying drugs
        '''
        probability = .25
        random_num_drugs = random.randint(1, 3) if num_drugs_purchased >= 3 else 1

        if random.random() < probability:
            choice = random.randint(1, 2)
            print('You check your newly bought drugs and find that...\n')
            # input('\nPress [Enter] key to continue ')
            return (choice, random_num_drugs)
        else:
            return (0, 0)

    def random_sold_event(self, total_sale):
        '''This function makes the game even more interesting by having a random
        chance event happen to Player with either negative or positive outcome
        when selling drugs
        '''
        probability = .6
        random_tip = random.randint(5, 10) if total_sale < 5000 else random.randint(1, 3)
        random_loss = random.randint(1, 3) if total_sale < 5000 else random.randint(5, 20)

        events = {
            1: 'You count your money, when all of a sudden a big gust of wind...\n',
            2: f'You gave such great service that you got a {random_tip}% tip from your buyer!\n'
            }

        if random.random() < probability:
            choice = random.randint(1, 2)
            print(events[choice])
            if choice == 1:
                return (choice, random_loss/100)
            else:
                return (choice, random_tip/100)
        else:
            return (0, 0)

    def __repr__(self):
        self.print_contents = []

        for i in range(0, len(self.drugs_list)):
            dn, qty = self.drugs_list[i].name_and_quantity
            self.print_contents.append(f'{dn}:'.ljust(12) + f'{qty}')
        return (
            f'{self.container_name}\n\n' +
            'Capacity:'.ljust(12) + f'{self.capacity}\n' +
            '\n'.join(self.print_contents) +
            '\n\n' +
            'Guns:'.ljust(12) + f'{self.guns}\n' +
            'Cash:'.ljust(12) + f'{self.cash}'
            )


class Stash(Container):
    '''Holds the Stash information including bank, debt, and the stashed drugs'''
    # when starting off, Player Stash has nothing but $5500 debt and a
    # drugs list consisting of Drug objects
    def __init__(self, container_name, drugs_list):
        super().__init__(container_name, drugs_list)

        self.bank = 0
        self.debt = 5500
        self.drugs_list = drugs_list

    def to_stash(self, drug_element, amount_to_stash):
        '''Initially Player's Trench Coat has a max capacity of 100 units of
        drugs. Player can decide to_stash() drugs away from Trench Coat which
        frees up units in Trench Coat for buying more (hopefully cheaper) drugs;
        however, Player does not have access to sell drugs from Stash until
        Player pulls drugs to_trench_coat().
        '''
        self.drugs_list[drug_element].quantity += amount_to_stash

    def to_trench_coat(self, drug_element, amount_to_send):
        '''Opposite of to_stash. Player can pull out drugs from their Stash
        so that they can free up space in their Trench Coat to buy more drugs
        '''
        self.drugs_list[drug_element].quantity -= amount_to_send

    def add_debt(self):
        '''As each day goes by, the debt increases by ~10% so Player should
        attempt to pay down debt quickly before saving for tuition
        '''
        self.debt = int(round(self.debt * 1.1, 0))

    def pay_loan_shark(self, cash_to_repay):
        '''pay down your debt to the loan shark'''
        self.debt -= cash_to_repay

    def deposit_cash(self, cash_to_deposit):
        '''Random chance encounter mitigation: sometimes Player can get mugged
        and lose a percentage of cash from their Trench Coat. Cash is safer in the
        Bank, but inaccessible until withdrawal. The Bank is only in The Bronx
        '''
        self.bank += cash_to_deposit

    def withdraw_cash(self, cash_to_withdraw):
        '''Random chance encounter mitigation: sometimes Player can get mugged
        and lose a percentage of cash from their Trench Coat. Cash is safer in the
        Bank, but inaccessible until withdrawal. The Bank is only in The Bronx
        '''
        self.bank -= cash_to_withdraw

    def __repr__(self):
        self.print_contents = []

        for i in range(0, len(self.drugs_list)):
            dn, qty = self.drugs_list[i].name_and_quantity
            self.print_contents.append(f'{dn}:'.ljust(12) + f'{qty}')
        return (
            f'{self.container_name}\n\n' +
            '\n'.join(self.print_contents) +
            '\n\n' +
            'Bank:'.ljust(12) + f'${self.bank}\n' +
            'Debt:'.ljust(12) + f'${self.debt}'
            )


class NewHood(Container):
    '''A NewHood object is created every time Player moves from one neighborhood
    to another (including when the game first starts).
    The NewHood takes in multiple objects to be able to manipulate the Player
    experience (e.g., HUD object, Stash object, TrenchCoat object). During
    game play, these objects are manipulated within the NewHood object for
    continuity as Player moves to other neighborhoods
    '''
    def __init__(self, container_name, hud_obj, stash_obj, trench_coat_obj, drugs_list):
        super().__init__(container_name, drugs_list)

        self.hood_name = container_name
        self.print_contents = []
        self.drugs_list = drugs_list
        self.hud_obj = hud_obj
        self.stash_obj = stash_obj
        self.trench_coat_obj = trench_coat_obj


    def negotiate(self):
        '''negotiate function controls what happens at each 'hood.
        '''
        self.print_contents = []

        for i in range(0, len(self.drugs_list)):
            drug_name, price = self.drugs_list[i].name_and_price
            self.print_contents.append(f'{i+1}. {drug_name}:'.ljust(13) + f'${price}')

        print(f'You find out that the prices of drugs in {self.hood_name} are:\n')
        self.market_price()

        choice = 0
        while choice != 3:
            if self.hood_name == 'The Bronx':
                choice = input(
                    '\nDo you want to:\n'
                    '[1] buy drugs\n'
                    '[2] sell drugs\n'
                    '[3] go to another hood?\n'
                    '[4] visit the loan shark\n'
                    '[5] go to your stash\n'
                    '[6] visit the bank\n'
                    '[0] quit the game\n'
                    '>> '
                    )
            else:
                choice = input(
                    '\nDo you want to:\n'
                    '[1] buy\n'
                    '[2] sell\n'
                    '[3] go to another hood?\n'
                    '[0] quit the game\n'
                    '>> '
                    )
            try:
                choice = int(choice)
            except ValueError:
                if self.hood_name == 'The Bronx':
                    print('That\'s not a choice between 1 - 6')
                else:
                    print('That\'s not a choice between 1 - 3')
                continue

            # these are possible choices that Player can choose to do [1-6, and 0]
            if choice == 1:
                hf.clear_screen()
                self.hud_obj.show_display()
                self.market_price()
                self.buy_drugs()

                # repaint the hud after buying drugs
                self.repaint_hud()
            elif choice == 2:
                hf.clear_screen()
                self.hud_obj.show_display()
                self.market_price()
                self.sell_drugs()

                # repaint the hud after selling drugs
                self.repaint_hud()

                # every time the user sells something, check if they've completed
                # the game (paid off debt and earned >= $75k)
                self.check_if_75k()
            elif choice == 3:
                print('\n\nYou want to go to another hood!')
                new_hood = self.which_hood()
                print(f'\nYou\'re going to {new_hood}!!!')
                time.sleep(2)
                return new_hood
            elif choice == 4 and self.hood_name == 'The Bronx':
                print('\n\nYou want to visit the loan shark!\n')
                hf.clear_screen()
                self.hud_obj.show_display()
                self.visit_loan_shark()

                # repaint the hud after repaying the loan shark
                self.repaint_hud()
            elif choice == 5 and self.hood_name == 'The Bronx':
                hf.clear_screen()
                self.hud_obj.show_display()
                self.visit_stash()

                # repaint the hud after buying drugs
                self.repaint_hud()
            elif choice == 6 and self.hood_name == 'The Bronx':
                print('\n\nYou want to go to the bank!')
                self.visit_bank()

                # repaint the hud after repaying the loan shark
                self.repaint_hud()
            elif choice == 0:
                hf.clear_screen()
                choice = input(
                    '\nAre you sure you want to quit?\n'
                    'Press "q" to quit or [Enter] to go back to the game. ')
                if choice == 'q':
                    hf.quitting()
                    # time.sleep(2)
                    hf.end_game()

                hf.clear_screen()
                self.hud_obj.show_display()
                self.market_price()

                # repaint the hud after buying drugs
                self.repaint_hud()
            else:
                print('That\'s not even an option, idiot! Learn to read!')


    def visit_bank(self):
        while True:
            try:
                choice = int(input(
                    'Bank Teller: "Welcome to Givus Yormoney and Trust Bank!\n'
                    'What would you like to do?\n'
                    '[1] Deposit Money\n'
                    '[2] Withdraw Money\n'
                    '>> '
                    ))
                if choice < 1 or choice > 2:
                    print('\nThat\'s not a choice between 1 or 2!!')
                    time.sleep(2)
                    hf.clear_screen()
                    self.hud_obj.show_display()
                    continue
                break
            except ValueError:
                print('\nThat\'s not a choice between 1 or 2!!')
                time.sleep(2)
                hf.clear_screen()
                self.hud_obj.show_display()
                continue

        if choice == 1:
            cash_to_deposit = int(input(
                '\nBank Teller: "How much money do you want to deposit?\n'
                '>> $'
                ))
            if cash_to_deposit > self.trench_coat_obj.cash:
                print(f'\nBank Teller: "You don\'t have ${cash_to_deposit} to deposit! Bye!!\n')
                time.sleep(2)
            elif cash_to_deposit < 0:
                print('\nBank Teller: "If you want to withdraw from your account,\n'
                      'please choose the withdraw option next time. Bye!\n')
                time.sleep(3)
            else:
                self.stash_obj.deposit_cash(cash_to_deposit)
                self.trench_coat_obj.cash_trench_to_bank(cash_to_deposit)
                print(f'\nThank you for your ${cash_to_deposit} deposit."')
                time.sleep(2)
        elif choice == 2:
            cash_to_withdraw = int(input(
                '\nBank Teller: "How much money do you want to withdraw?\n'
                '>> $'
                ))
            if cash_to_withdraw > self.stash_obj.bank:
                print(f'\nBank Teller: "You don\'t have ${cash_to_withdraw} to withdraw! Bye!!\n')
                time.sleep(2)
            elif cash_to_withdraw < 0:
                print('\nBank Teller: "If you want to deposit to your account,\n'
                      'please choose the deposit option next time. Bye!\n')
                time.sleep(3)
            else:
                self.stash_obj.withdraw_cash(cash_to_withdraw)
                self.trench_coat_obj.withdraw_cash_from_bank(cash_to_withdraw)
                print(f'\nThank you for your ${cash_to_withdraw} withdrawal."')
                time.sleep(2)


    def visit_stash(self):
        '''Player visits stash in order to hide drugs and make room in their Trench
        Coat or doesn't want their drugs stolen by a random chance event. Stash is
        located in The Bronx and can only be accessed when Player is there.
        Function manipulates both the Stash object and the TrenchCoat object using
        appropriate methods for each depending on if drugs are going to Stash from
        TrenchCoat or the opposite.
        '''
        while True:
            try:
                choice = int(input(
                    '\nYou\'re at your stash.\n'
                    'What would you like to do?\n'
                    '[1] Stash drugs\n'
                    '[2] Pull drugs out\n'
                    '>> '
                    ))
                if choice < 1 or choice > 2:
                    print(f'\n{self.random_insult_generator()}! That\'s not a choice between 1 or 2!!')
                    time.sleep(2)
                    hf.clear_screen()
                    self.hud_obj.show_display()
                    continue
                break
            except ValueError:
                print(f'\n{self.random_insult_generator()}! That\'s not a choice between 1 or 2!!')
                time.sleep(2)
                hf.clear_screen()
                self.hud_obj.show_display()
                continue

        hf.clear_screen()
        self.hud_obj.show_display()

        for i in range(0, len(self.drugs_list)):
            print(f'[{i+1}] {self.drugs_list[i].drug_name}')

        if choice == 1:
            drug_element = int(input(
                'Which drug do you want to stash?\n'
                '>> '
                )) - 1

            drug_amount = int(input(
                f'\nHow much {self.drugs_list[drug_element].drug_name} do you want to stash?\n'
                '>> '
                ))

            if drug_amount > self.trench_coat_obj.drugs_list[drug_element].quantity:
                print(f'\nYou don\'t have {drug_amount} units of {self.drugs_list[drug_element].drug_name} to stash! Bye!!\n')
                time.sleep(2)
            else:
                self.stash_obj.to_stash(drug_element, drug_amount)
                self.trench_coat_obj.from_trench_coat(drug_element, drug_amount)
                print(f'\nYou stashed {drug_amount} units of {self.drugs_list[drug_element].drug_name}.')
                time.sleep(2)
        elif choice == 2:
            drug_element = int(input(
                'Which drug do you want to pull out?\n'
                '>> '
                )) - 1

            drug_amount = int(input(
                f'\nHow much {self.drugs_list[drug_element].drug_name} do you want to pull out?\n'
                '>> '
                ))

            if drug_amount > self.stash_obj.drugs_list[drug_element].quantity:
                print(f'\nYou don\'t have {drug_amount} units of {self.drugs_list[drug_element].drug_name} to pull out! Bye!!\n')
                time.sleep(2)
            else:
                self.stash_obj.to_trench_coat(drug_element, drug_amount)
                self.trench_coat_obj.from_stash(drug_element, drug_amount)
                print(f'\nYou pulled out {drug_amount} units of {self.drugs_list[drug_element].drug_name}.')
                time.sleep(2)


    def visit_loan_shark(self):
        '''Player chooses to visit the loan shark to pay off debt (one of the requirements
        to beat the game). Function does error checking to make sure that Player has
        enough cash to pay. After function runs, checks to see if Player won.
        '''
        print('Loan Shark: "Well, well, well. Look who\'s back?')
        while True:
            try:
                pay_back_amt = int(input(
                    'How much money are you giving me?"\n\n'
                    f'You have ${self.trench_coat_obj.cash} in your Trench Coat.\n'
                    '>> $'
                    ))
                if isinstance(pay_back_amt, float):
                    print(f'\nLoan Shark: "{self.random_insult_generator()}! I only take whole dollars, pal!!"')
                    time.sleep(2)
                    hf.clear_screen()
                    self.hud_obj.show_display()
                    continue
                elif pay_back_amt < 0:
                    print('\nLoan Shark: "What is this? A joke? Get the f&%k outta here!"')
                    time.sleep(2)
                    hf.clear_screen()
                    self.hud_obj.show_display()
                    continue
                elif pay_back_amt > self.trench_coat_obj.cash:
                    print('\nLoan Shark: "You don\'t have that kind of money, pal!!"')
                    time.sleep(2)
                    hf.clear_screen()
                    self.hud_obj.show_display()
                    continue
                elif pay_back_amt > self.stash_obj.debt:
                    print(
                        'Loan Shark: "You\'re trying to give me more money than you owe me!!\n'
                        'I appreciate the gesture, but I don\'t like owing people money."\n'
                        )
                    time.sleep(3)
                    hf.clear_screen()
                    self.hud_obj.show_display()
                    continue
                break
            except ValueError:
                print(f'\nLoan Sharek: "{self.random_insult_generator()}! I only take whole dollars, pal!!"')
                time.sleep(2)
                hf.clear_screen()
                self.hud_obj.show_display()
                continue

        if pay_back_amt == 0:
            print(
                '\nLoan Sharek: You\'re trying to pay me $0? Really? You know what I do for a living, right?\n'
                'Get the hell outta here!!"'
                )
            time.sleep(2)
        else:
            # decrement Stash.debt attribute
            self.stash_obj.pay_loan_shark(pay_back_amt)
            # decrement TrenchCoat.debt attribute
            self.trench_coat_obj.cash_to_loan_shark(pay_back_amt)
            print('\nLoan Shark: "It\'s about damn time."')

            self.check_if_75k()
            time.sleep(2)


    def which_hood(self):
        '''Asks the user where they want to go next, does error checking, and hurls
        a random insult for entering a wrong input.

        Returns the name of the next hood that the user wants to go to for use
        in creating a new NewHood object in the main for loop of the start_game function
        '''
        while True:
            try:
                go_to_city = int(input(
                    '\nWhere do you want to go?\n'
                    '[1] The Bronx\n'
                    '[2] Central Park\n'
                    '[3] Manhattan\n'
                    '[4] Brooklyn\n'
                    '[5] The West Side\n'
                    '[6] Queens\n'
                    '>> '
                    ))
                if go_to_city < 1 or go_to_city > 6:
                    print(f'\n{self.random_insult_generator()}! That\'s not a choice between 1 and 6!!')
                    time.sleep(2)
                    hf.clear_screen()
                    self.hud_obj.show_display()
                    self.market_price()
                    continue

                if go_to_city == 1:
                    if self.check_if_same_hood('The Bronx'):
                        continue
                    return 'The Bronx'
                elif go_to_city == 2:
                    if self.check_if_same_hood('Central Park'):
                        continue
                    return 'Central Park'
                elif go_to_city == 3:
                    if self.check_if_same_hood('Manhattan'):
                        continue
                    return 'Manhattan'
                elif go_to_city == 4:
                    if self.check_if_same_hood('Brooklyn'):
                        continue
                    return 'Brooklyn'
                elif go_to_city == 5:
                    if self.check_if_same_hood('The West Side'):
                        continue
                    return 'The West Side'
                else:
                    if self.check_if_same_hood('Queens'):
                        continue
                    return 'Queens'
                break
            except ValueError:
                print(f'\n{self.random_insult_generator()}! That\'s not a choice between 1 and 6!!')
                time.sleep(2)
                hf.clear_screen()
                self.hud_obj.show_display()
                self.market_price()
                continue


    def sell_drugs(self):
        # talk to drug dealer
        # buy_or_sell flag will make the drug dealer's question make sense
        drug_choice, current_drug_price, name_of_drug = self.talk_to_drug_dealer('do you have to sell')

        qty_possible = self.trench_coat_obj.drugs_list[drug_choice].quantity

        print(
            f'\n{self.hood_name} Drug Dealer: "So you wanna sell {name_of_drug}, huh?\n'
            'How many do you want to sell to me?"\n'
            )
        while True:
            drug_qty = input(
                f'You have {qty_possible} units of {name_of_drug} to sell:\n'
                '>> '
                )
            try:
                int(drug_qty)
                break
            except ValueError:
                hf.clear_screen()
                self.hud_obj.show_display()
                self.market_price()
                print('\nYou\'re kind of pissing me off...I need a whole number')
                continue

        drug_qty = int(drug_qty)


        if drug_qty > qty_possible:
            print(f'Sorry, bud. You don\'t have that much {name_of_drug} to sell to me!')
            time.sleep(2)
        elif drug_qty == 0:
            print(f'\n{self.hood_name} Drug Dealer: "You\'re wasting my time!"')
            time.sleep(2.5)
        else:
            # complete the transaction of buying the drugs
            self.trench_coat_obj.sold_drug(drug_choice, drug_qty, current_drug_price)


    def buy_drugs(self):
        # talk to drug dealer
        # buy_or_sell flag will make the drug dealer's question make sense
        drug_choice, current_drug_price, name_of_drug = self.talk_to_drug_dealer('are you looking for')

        max_limit = self.trench_coat_obj.capacity if self.trench_coat_obj.cash//current_drug_price > self.trench_coat_obj.capacity else self.trench_coat_obj.cash//current_drug_price
        max_flag = 'trench coat capacity' if self.trench_coat_obj.cash//current_drug_price > self.trench_coat_obj.capacity else 'cash'
        min_flag = 'trench coat capacity' if max_flag == 'cash' else 'cash'

        print(f'\n{self.hood_name} Drug Dealer: "So you wanna buy {name_of_drug}, huh? How much do you want?"')
        while True:
            drug_qty = input(
                f'\nYou\'re limited by your {max_flag}!\n'
                f'You have enough {max_flag} to buy up to {max_limit} units of {name_of_drug},\n'
                f'even though you have more {min_flag} than that.\n'
                'How much do you want to buy?\n'
                '>> '
                )
            try:
                drug_qty = int(drug_qty)
                if drug_qty > max_limit:
                    hf.clear_screen()
                    self.hud_obj.show_display()
                    print(f'Market prices of drugs in {self.hood_name}:\n')
                    self.market_price()
                    print(
                        f'\nI literally just said you can\'t buy more than {max_limit} units, what\'s wrong with you?\n'
                          'Let\'s try this again ok?....'
                          )
                    time.sleep(2)
                    continue
                break
            except ValueError:
                hf.clear_screen()
                self.hud_obj.show_display()
                self.market_price()
                print('\n{self.hood_name} Drug Dealer: "You\'re kind of pissing me off...I need a whole number."')
                continue

        if drug_qty * current_drug_price > self.trench_coat_obj.cash:
            print('Sorry, bud. You don\'t have enough cash to buy that many!')
        elif drug_qty == 0:
            print(f'\n{self.hood_name} Drug Dealer: "You\'re wasting my time!"')
            time.sleep(2.5)
        else:
            # complete the transaction of buying the drugs
            self.trench_coat_obj.bought_drug(drug_choice, drug_qty, current_drug_price)


    def talk_to_drug_dealer(self, buy_or_sell):
        '''Every time Player talks to the drug dealer, it's the same basic interaction
        but is either buying or selling. the buy_or_sell flag is a string that is passed
        in to make the drug dealer's "ask" make sense grammatically. Then the function
        returns a tuple with the index for the drug of choice, the drug's current market
        value and the drug's name'
        '''
        drug_choice = -1
        while True:
            try:
                print(f'\n{self.hood_name} Drug Dealer: "What kind of drugs {buy_or_sell}?"')
                drug_choice = int(input(
                    f'\nPick one [1-{len(self.drugs_list)}]:\n'
                    '>> '
                    )) - 1

                if drug_choice < 0 or drug_choice > 5:
                    print(f'That\'s not a choice between 1 and {len(self.drugs_list)}!!')
                    time.sleep(2)
                    hf.clear_screen()
                    self.hud_obj.show_display()
                    self.market_price()
                    continue
                break
            except ValueError:
                print(f'That\'s not a choice between 1 and {len(self.drugs_list)}!!')
                time.sleep(2)
                hf.clear_screen()
                self.hud_obj.show_display()
                self.market_price()
                continue

        return (drug_choice, self.drugs_list[drug_choice].market_price, self.drugs_list[drug_choice].drug_name)


    def check_if_75k(self):
        '''Every time Player sells drugs or visits the loan shark, this function
        is called to check if they have satisfied the requirements of the game
        (i.e., paid off the loan shark and made enough money to pay tuition,
         all before the 1st of August 2021)
        '''
        if self.trench_coat_obj.cash > 75000 and self.stash_obj.debt == 0:
            print(
                '\nCogratulations! You were able to make enough money to pay for\n'
                'tuition and you paid off the loan shark before August 1st, 2021!\n\n'
                )

            input('You won!!! Press [Enter] to end game ')
            hf.end_game()


    def repaint_hud(self):
        self.hud_obj.show_display()
        print(f'Market prices of drugs in {self.hood_name}:\n')
        self.market_price()
        # print('\n')


    def market_price(self):
        print('\n'.join(self.print_contents))


    def random_insult_generator(self):
        random_insult = [
            'Hey, dumbass',
            'You\'re stupid',
            'How are you so bad at typing?',
            'You stupid or something?',
            'What an idiot',
            'You suck at this',
            'Way to go. Everyone\'s dumber because of you'
            ]
        return random_insult.pop(random.randint(0, len(random_insult)-1))


    def check_if_same_hood(self, hood_name):
        if self.hood_name == hood_name:
            print(f'\nYou\'re already in {self.hood_name}!!')
            time.sleep(2)
            hf.clear_screen()
            self.hud_obj.show_display()
            return True
