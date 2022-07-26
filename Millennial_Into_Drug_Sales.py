#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 23:00:00 2021

@author: Christian Montecillo
"""

from helper import helper_functions as hf
from drugs import drugs as dg
from HUD import hud as hd
from containers import containers as ctr

# Features to add later:
# acquire_gun function -- maybe will do for v2.0 :D
    # error checking everywhere!
    # random chance events
# more comments and docstrings!


def main():
    '''This function kicks off the game, and initializes the objects that will be
    used in the game. The main objects created are:
    1. the drugs that each container holds
    2. the containers themselves (TrenchCoat, NewHood, and Stash)
    3. the HUD (heads up display)
    '''
    # initialize all the drugs for use in containers
    neighborhood_drugs = dg.make_drugs()
    stash_drugs = dg.make_drugs()
    trench_coat_drugs = dg.make_drugs()

    # intializes the containers with initial appropiate values
    starting_hood = 'The Bronx'
    stsh = ctr.Stash('Stash', stash_drugs)
    tc = ctr.TrenchCoat('Trench Coat', trench_coat_drugs)
    new_display = hd.HUD(stsh, tc, starting_hood)
    nh = ctr.NewHood(starting_hood, new_display, stsh, tc, neighborhood_drugs)

    # print out credits screen
    hf.clear_screen()
    hf.mids_credits()

    # print instructions if player chooses to
    print_instructions = input(
        'Do you want Instructions? [y/n] or any key for no\n'
        '>> '
        ).lower()

    if print_instructions == 'y':
        hf.instructions()

        print('Range of drug prices per unit:\n')

        # print all the drugs objects recently created
        for drugs in neighborhood_drugs:
            print(drugs)

    input('\nPress [Enter] to start the game ')

    # this is the main for loop that simulates 30 days of time due to time constraint
    for _ in range(30):
        # paint the display
        new_display.show_display()
        go_to_hood = nh.negotiate()
        new_display.change_hood(go_to_hood)
        stsh.add_debt()
        new_display.increment_date()
        my_drugs = dg.make_drugs()

        # create a NewHood object because Player wanted to move to a different hood
        nh = ctr.NewHood(go_to_hood, new_display, stsh, tc, my_drugs)

    # if the game exits the for loop, then Player did not succeed and game
    # prints out a disparaging remark and quits
    print(
        '\n\nToo bad for you, you didn\'t make enough money\n'
        'for tuition and you ran out of time. You blew it!n\n'
        )

    hf.end_game()


if __name__ == '__main__':
    # starts the game
    main()
