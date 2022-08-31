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

def pc_guess(x):
    print(f'Please choose a number between 1 and {x}')
    key=''
    while key != 'yes':
        key=input('Are you ready? \n').lower()
    num = ''
    low = 1
    high = x
    while num != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        print(f'The number is {guess}')
        num = input('Is the number correct (C), too high (H) or too low(L)? \n').lower()
        if num == 'h':
            high = guess-1
        elif num == 'l':
            low = guess+1         
    print(f'Your number is {guess}')

print('How do you want to play?')
mode = input('Should the computer(pc) guess or should you (me) guess?\n').lower()
if mode == 'me':
    guess(10)
else:
    pc_guess(10)