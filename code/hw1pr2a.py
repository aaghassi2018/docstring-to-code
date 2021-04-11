# coding: utf-8
#
# hw1pr2a.py
#

import random          # imports the library named random

#Name: Ashkon Aghassi

def rps():
    userChoice = input("Choose from \'rock\', \'paper\', or \'scissors\': ")
    computerChoice = random.choice(['rock','paper','scissors'])

    print()
    print('You chose', userChoice)
    print('I (computer) chose', computerChoice)
    print()


    if userChoice == computerChoice:
        print('We Tied!')

    if userChoice == 'rock' and computerChoice== 'paper':
        print('I (computer) won!')

    if userChoice == 'paper' and computerChoice== 'rock':
        print('You won!')

    if userChoice == 'scissors' and computerChoice== 'rock':
        print('I (computer) won!')

    if userChoice == 'rock' and computerChoice== 'scissors':
         print('You won!')

    if userChoice == 'paper' and computerChoice== 'scissors':
        print('I (computer) won!')

    if userChoice == 'scissors' and computerChoice== 'paper':
        print('You won!')