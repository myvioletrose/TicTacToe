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
def space_check(b, p):
	return b[p] == ' '
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
# I am not sure why this below piece would work, shouldn't position be defined first as a global variable and then subsequently overwritten when the game begins?
# really don't understand why this below would work...??
def player_choice(b, pl):
	position = 0

	while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
		try:
			position = int( input( 'Player %s, choose your next position: (1-9)' %(pl) ) )
		except:
			print("Incorrect, please try again.")

	return position

# place marker
def place_marker(a, b, pl, p):
	a[p] = ' '
	b[p] = pl

# replay
def replay():
	return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

#########################################################
###################### game begins ######################
#########################################################
while True:
	clear_output()
	print('Welcome to Tic Tac Toe!')

	toggle = alter_player()
	player = players[toggle]
	print('For this round, Player %s will go first!' %(player))

	game_on = True
	input('Hit Enter to continue')
	while game_on:
		display_board(available, board)  # display the board
		position = player_choice(board, player)  # define position
		place_marker(available, board, player, position)  # record position for a marker

		# check win
		if win_check(board, player):
			display_board(available, board)
			print('Congratulations! Player ' + player + ' wins!')
			game_on = False
		# check draw	
		else: 
			if full_board_check(board):
				display_board(available, board)
				print('The game is a draw')
				break
		# if no win or draw, alter player	
			else:
				toggle *= -1
				player = players[toggle]
				clear_output()

	# reset the board and available moves list
	board = [' '] * 10
	available = [str(num) for num in range(0, 10)]

	# so we can just run the replay function in the if-statment?
	if not replay():
		break










