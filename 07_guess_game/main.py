# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 09:11:00 2022

@author: jnaranjo
"""

import random

def guess(x):
    num = random.randint(1, x)
    guess=0
    while guess != num:
        guess = int(input(f'Guess a number between 1 and {x} \n'))
        if guess>num:
            print('Guess is too high!!')
        elif guess<num:
            print('Guess is too low!!')
    print(f'You guessed the number {num} correctly!!!')

guess(10)