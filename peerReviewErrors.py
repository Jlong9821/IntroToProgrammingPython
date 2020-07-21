# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <Jacob Longfield>
# Creation Date: <7/21/2020>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
	cave = ''
	while (cave != '1') and (cave != '2'): 
		print('Which cave will you go into? (1 or 2)')
		cave = input()
	return cave #Was caves needs to be cave to match variable name

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(2) #Says to sleep for 2 seconds but parameter is 3
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!') # I do get both messages when the game is played
	else:
		print ('Gobbles you down in one bite!') #Missing ()

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y': # Use == to check if something is equal x2
	displayIntro()
	caveNumber = chooseCave() #Need to match method name. Was choosecave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input().lower()
	if playAgain == "no" or playAgain == 'n': #Message only appears if user types in no, for yes it also checks for y
		print("Thanks for playing") #Playing is spelled wrong

# Program quits if 'Yes' is used or if 'Y' is used. Use .lower() to take care of that