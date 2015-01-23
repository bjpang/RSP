#Rock Paper Scissors

import math
import random

def playgame():
	print "Time to play a game of Rock, Paper, Scissors!"
	#Rock = 0
	#Paper = 1
	#Scissors = 2
	playerChoice = input("Choose one of them (1:Rock, 2:Paper, 3:Scissors): ")
	#playerChoice = 0
	winner = 0
	computerChoice = random.randint(1, 3)
	choices = {1:"Rock", 2:"Paper", 3:"Scissors"}
	print "You chose " + choices[playerChoice]
	print "The computer chose " + choices[computerChoice]
	if playerChoice == computerChoice:
		print "You tied this round!"
		return 0
	elif playerChoice == 1:
		if computerChoice == 2:
			print "You lost this round!"
			return 2
		print "You won this round!"
		return 1
	elif playerChoice == 2:
		if computerChoice == 1:
			print "You won this round!"
			return 1
		print "You lost this round!"
		return 2
	else:
		if computerChoice == 1:
			print "You lost this round!"
			return 2
		print "You won this round!"
		return 1

if __name__ == '__main__':
	games = input("Do you want to play Rock, Paper, Scissors? (1: Yes, 2: No): ")
	#games = 3
	playerScore, compScore = 0, 0
	while games == 1:
		point = playgame()
		#Tie = 0
		#Player Win = 1
		#Computer Win = 2
		if point == 1:
			playerScore = playerScore + 1
		elif point == 2:
			compScore = compScore + 1
		else:
			playerScore = playerScore + 1
			compScore = compScore + 1
		games = input("Do you want to play again? (1:Yes, 2:No): ")


	print "Your score: " + str(playerScore)
	print "Computer score: " + str(compScore)
	if(playerScore < compScore):
		print "Sorry, you lost more times!"
	elif playerScore == compScore:
		print "You tied with the computer! You should play again!"
	else:
		print "You won more times! Congratulations!"
