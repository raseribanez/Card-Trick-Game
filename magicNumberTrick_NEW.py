# Ben Woodfield  PYTHON 2.7
# This game was a card toy from a christmas cracker, I decided to write it into Python to practice 
# Written & Coded by Ben Woodfield 02/01/2016
#(First Program Written with no help or guide)

'''            INSTRUCTIONS OF THE ORIGINAL GAME
1: The player is given 6 cards (the original trick had actual cards), each has a grid with 32 numbers.
2: The player is asked to pick a number from any of the cards.
3: Only the cards with the chosen number on are to be kept - the others aren't needed
4: The remaining cards' top left numbers (First number in the top left corners) 
5: will equal the number chosen.  It works for ANY number that is chosen!'''

# 01 / 12 / 2016
# NOTE:
# I reopened this after I asked a question on Stack Overflow.
# I askied if there was a solution to put the numbers into tidy grids
# One reply was a handy little function to put the data into 4 x 6 grids 
# Heres the question and reply (Reply from Patrik Haugh):
# http://stackoverflow.com/questions/40915353/how-to-display-a-grid-of-numbers-neatly/40915777#40915777

# CHANGES MADE:
# Applied the new grid function to all 6 grids to look neater
# Added the replay function at the end of game
# Added a few "Enter to continue" scenarios to slow things down
# Put everything into functions for efficiency

#!/usr/bin/env python
import time
import sys

GRID_1 = ['32....33....34....35 \n36....37....38....39',
          '\n40....41....42....43 \n44....45....46....47',
          '\n48....49....50....51 \n52....53....54....55',
          '\n56....57....58....59 \n60....61....62....63\n\n']

GRID_2 = ['8.....9.....10....11 \n12....13....14....15',
          '\n24....25....26....27 \n28....29....30....31',
          '\n40....41....42....43 \n44....45....46....47',
          '\n56....57....58....59 \n60....61....62....63\n\n']


GRID_3 = ['4.....5.....6.....7  \n12....13....14....15',
          '\n20....21....22....23 \n28....29....30....31',
          '\n36....37....38....39 \n44....45....46....47',
          '\n52....53....54....55 \n60....61....62....63\n\n']


GRID_4 = ['2.....3.....6.....7  \n10....11....14....15',
          '\n18....19....22....23 \n26....27....30....31',
          '\n34....35....38....39 \n42....43....46....47',
          '\n50....51....54....55 \n58....59....62....63\n\n']


GRID_5 = ['16....17....18....19 \n20....21....22....23',
          '\n24....25....26....27 \n28....29....30....31',
          '\n48....49....50....51 \n52....53....54....55',
          '\n56....57....58....59 \n60....61....62....63\n\n']


GRID_6 = ['1.....2.....5.....7\n9.....11....13...15',
          '\n17....19....21...23  \n25....27....29...31',
          '\n33....35....37...39  \n41....43....45...47',
          '\n49....51....53...55  \n57....59....61...63\n\n']


def grid_print(GRID_1):
    for x in zip(*[iter(GRID_1)]*4):
        print('{:<4}{:^6}{:^6}{:^6}'.format(*x))

def grid_print(GRID_2):
    for x in zip(*[iter(GRID_2)]*4):
        print('{:<4}{:^6}{:^6}{:^6}'.format(*x))

def grid_print(GRID_3):
    for x in zip(*[iter(GRID_3)]*4):
        print('{:<4}{:^6}{:^6}{:^6}'.format(*x))


def grid_print(GRID_4):
    for x in zip(*[iter(GRID_4)]*4):
        print('{:<4}{:^6}{:^6}{:^6}'.format(*x))

def grid_print(GRID_5):
    for x in zip(*[iter(GRID_5)]*4):
        print('{:<4}{:^6}{:^6}{:^6}'.format(*x))


def grid_print(GRID_6):
    for x in zip(*[iter(GRID_6)]*4):
        print('{:<4}{:^6}{:^6}{:^6}'.format(*x))

def questions():
        print('|---Welcome to the Magic Number Trick---| \nFollow the simple instructions to play.')
        time.sleep(0.80)
        name = input('What is your name? \n>>> ')
        time.sleep(0.5)
        print("Hi %s let's get started..." % name)
        time.sleep(1.5)
        print('I am going to show you 6 grids of numbers...\n\nThen ask you to pick a number between 1 and 63 from one of the grids.')
        cont1 = input("Press Enter to continue:")
        print("Here is Grid 1: \n")
        grid_print(GRID_1)
        time.sleep(0.75)
        print("Here is Grid 2: \n")
        grid_print(GRID_2)
        time.sleep(0.75)
        print("Here is Grid 3: \n")
        grid_print(GRID_3)
        time.sleep(0.75)
        print("Here is Grid 4: \n")
        grid_print(GRID_4)
        time.sleep(0.75)
        print("Here is Grid 5: \n")
        grid_print(GRID_5)
        time.sleep(0.75)
        print("Here is Grid 6: \n")
        grid_print(GRID_6)
        time.sleep(0.75)
        cont =  input("\n\nPick a number...Keep it to yourself... \n\nThen press Enter to continue when ready...\n\n|-----------------------------------------|\n\n")
        time.sleep(2)
        print("Thank You...now for this trick to work you need \n\nto concentrate ONLY on the grids which have \n\nYOUR chosen NUMBER in...")
        time.sleep(1.5)
        print("Have a look through the grids...\n\nSee which ones have your number, \n\nIncluding the grid you got your number from")
        time.sleep(1.5)
        cont2 = input("Then press Enter to continue")
        print("\n\n\nYou are going to enter the FIRST number from each grid \n\ncontaining your number")
        time.sleep(1)
        print ("Follow the next set of instructions carefully... \nEnter the numbers one at a time:")
        time.sleep(2)
        firstNumber = int(input("Pease enter your First Number \n>>> "))
        secondNumber = int(input("Please enter your Second Number \n>>> "))
        thirdNumber = int(input("Please enter your Third Number - type 0 if you don't have one \n>>> "))
        fourthNumber = int(input("Please enter your Fourth Number - type 0 if you don't have one \n>>>"))
        time.sleep(4)
        print ("\nYour Number Is.......\n")
        time.sleep(2)
        print (firstNumber + secondNumber + thirdNumber + fourthNumber)
        time.sleep(2)

def final():
        print("Thanks For Playing Magic Number!...Would you like to play again?")
        user_reply = input("..Type [yes] to continue, or anything else to quit\n>>> ")
        while(input):
               if user_reply == "yes":
                      questions()
               else:
                        print("Thanks for playing Magic Number!")
                        sys.exit(0)


questions()
final()





            



