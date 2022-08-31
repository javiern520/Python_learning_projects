# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 10:45:14 2022

@author: jnaranjo
"""

import random

def play():
    user = input('What is your choice?\n"r" for rock, "p" for paper or "s" for scissors\n').lower()
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'It\'s a tie !!!'
    
    if is_win(user, computer):
        return 'You have won!!!!'
    
    return 'You have lost :('

def is_win(user, computer):
    # r>s or s>p or p>r
    if (user=='r' and computer=='s') or (user=='s' and computer=='p') or \
        (user=='p' and computer=='r'):
        return True
    
print(play())            