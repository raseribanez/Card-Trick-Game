# Ben Woodfield
# This game was a card toy from a christmas cracker, I decided to write it into Python to practice 
# Written & Coded by Ben Woodfield 02/01/2016
#(First Program Written with no help or guide)

# INSTRUCTIONS OF THE ORIGINAL GAME
#1: The player is given 6 cards (the original trick had actual cards), each has a grid with 32 numbers.
#2: The player is asked to pick a number from any of the cards.
#3: Only the cards with the chosen number on are to be kept - the others aren't needed
#4: The remaining cards' top left numbers (top left corners) will equal the number chosen
#%: It works for ANY number that is chosen!

#!/usr/bin/env python
import time

GRID_1 = ['32....33....34....35....36....37....38....39....',
          '40....41....42....43....44....45....46....47....',
          '48....49....50....51....52....53....54....55....',
          '56....57....58....59....60....61....62....63....']


GRID_2 = ['8.....9.....10....11....12....13....14....15....',
          '24....25....26....27....28....29....30....31....',
          '40....41....42....43....44....45....46....47....',
          '56....57....58....59....60....61....62....63....']


GRID_3 = ['4.....5.....6.....7.....12....13....14....15....',
          '20....21....22....23....28....29....30....31....',
          '36....37....38....39....44....45....46....47....',
          '52....53....54....55....60....61....62....63....']


GRID_4 = ['2.....3.....6.....7.....10....11....14....15....',
          '18....19....22....23....26....27....30....31....',
          '34....35....38....39....42....43....46....47....',
          '50....51....54....55....58....59....62....63....']


GRID_5 = ['16....17....18....19....20....21....22....23....',
          '24....25....26....27....28....29....30....31....',
          '48....49....50....51....52....53....54....55....',
          '56....57....58....59....60....61....62....63....']


GRID_6 = ['1.....2.....5.....7.....9.....11....13....15....',
          '17....19....21....23....25....27....29....31....',
          '33....35....37....39....41....43....45....47....',
          '49....51....53....55....57....59....61....63....']


userName = raw_input("Welcome to the Magic Grid - Number Trick! Please enter your name >>>  ")
time.sleep(2)
print "Welcome to the program,", userName
goAgain = 1
print ("Take a quick look at the 6 number-grids below...")# I don't know how to insert a table, grid or chart to display the numbers - for now they appear in a bit of a messy fashion
time.sleep(2)
goAgain = 1
print "\n\nHere is Grid Number - 1\n\n"
print (GRID_1)
time.sleep(1)
print "\n\nHere is Grid Number - 2\n\n"
print (GRID_2)
time.sleep(1)
print "\n\nHere is Grid Number - 3\n\n"
print (GRID_3)
time.sleep(1)
print "\n\nHere is Grid Number - 4\n\n"
print (GRID_4)
time.sleep(1)
print "\n\nHere is Grid Number - 5\n\n"
print (GRID_5)
time.sleep(1)
print "\n\nHere is Grid Number - 6\n\n"
print (GRID_6)
time.sleep(2)

print "\n\nPick any Number from One of the Grids...and remember the grid it was from...\n\n"
time.sleep(2)

print "Please enter your chosen Number:"
user_reply = raw_input('>>>')
time.sleep(2)
print "Thank You...now for this trick to work you need to concentrate ONLY on the grids which have YOUR chosen NUMBER in..."
time.sleep(3)
print "Please enter the Grid Numbers containing your number - (including the one you chose) - (for example enter 1, 2, 3)"
user_reply = raw_input('>>>')

print "OK, Well Done...Now, I want you to look at the grids you have chosen, and take note of their first numbers - you will need to enter these below"
time.sleep(6)

firstNumber = int(raw_input("Pease enter your First Number >"))
secondNumber = int(raw_input("Please enter your Second Number >"))
thirdNumber = int(raw_input("Please enter your Third Number - type 0 if you don't have one >"))
fourthNumber = int(raw_input("Please enter your Fourth Number - type 0 if you don't have one >"))
print ("\nThe sum of these numbers should result in the Number You Chose at the start\n")
time.sleep(4)
print "\nYour Number Is.......\n"
time.sleep(2)
print (firstNumber + secondNumber + thirdNumber + fourthNumber)
time.sleep(2)


#input("\n\nPress the enter key to exit.")#THIS BASIC EXIT FUNCTION WORKS (however the program should have a loop style function to ask another question or quit - when I know how to do this properly I will update it)
# The lines of code below were taken from a magic8ball program
# the code is supposed to ask the user if they want to play again 
# if [yes] is typed, it loops to the start again, and anything else typed quits the program
# I changed the printed writing to fit with this program, but it didnt even work on the 8ball program

def final():
        print("Thanks For Playing Magic Number!...Would you like to play again?...Type [yes] to continue, or anything else to quit")
        user_reply = input("> ")
        while(input):
               if user_reply == "yes":
                      userinput()
               else:
                        print("Thanks for playing Magic Number!")
                        sys.exit(0)

final() 





            



