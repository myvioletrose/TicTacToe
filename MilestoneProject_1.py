# import
from IPython.display import clear_output
import random

# set up global variables
board = [' '] * 10
available = [str(num) for num in range(0, 10)]
players = [0, 'X', 'O']

# create display board
def display_board(a, b):
	print('   available moves	     TIC-TAC-TOE\n' + 
		'\n 	' +
		a[1] + '|' + a[2] + '|' + a[3] + '		 	' + b[1] + '|' + b[2] + '|' + b[3] + '\n 	' +
		'-----			-----\n 	' +
		a[4] + '|' + a[5] + '|' + a[6] + '		 	' + b[4] + '|' + b[5] + '|' + b[6] + '\n 	' +
		'-----			-----\n 	' +
		a[7] + '|' + a[8] + '|' + a[9] + '		 	' + b[7] + '|' + b[8] + '|' + b[9] + '\n 	')

# alternate player
def alter_player():
	return random.choice((-1, 1))

##########################################################################################
# create "checking" - empty space check, return True if position is empty
def space_check(b, position):
	return b[position] == ' '
# create "checking" - full board check, return True if all positions are filled
def full_board_check(b):
	return ' ' not in b[1:]
# create "checking" - win check
def win_check(b, mark):
	return( ( b[1] == b[2] == b[3] == mark ) or
			( b[4] == b[5] == b[6] == mark ) or
			( b[7] == b[8] == b[9] == mark ) or
			( b[1] == b[4] == b[7] == mark ) or
			( b[2] == b[5] == b[8] == mark ) or
			( b[3] == b[6] == b[9] == mark ) or
			( b[1] == b[5] == b[9] == mark ) or
			( b[3] == b[5] == b[7] == mark ) )

# player choice - to update marker "position"
def player_choice(b, player):
	position = 0

	while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
		try:
			position = int( input( 'Player %s, choose your next position: (1-9)' %(player) ) )
		except:
			print("Incorrect, please try again.")

	return position

# place marker
def place_marker(a, b, marker, position):
	a[position] = ' '
	b[position] = marker

# replay
def replay():
	return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')