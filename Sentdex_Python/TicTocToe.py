import itertools
from colorama import Fore,Back,Style,init
init()

def win(current_game):

	def all_same(row_copy):
		if row_copy.count(row_copy[0]) == len(row_copy) and row_copy[0] != 0:
			return True
		else: 
			return False

	#horizontal
	for row in game:
		if all_same(row):
			print(f'Player {row[0]} is the winner horizontally')
			return True
	#Diagonal
	diags = []
	for col,row in enumerate(reversed(range(len(game)))):
		diags.append(game[row][col])
	if all_same(diags):
			print(f'Player {diags[0]} is the winner Diagonally (/)')
			return True

	diags = []
	for idx in range(len(game)):
		diags.append(game[idx][idx])
	if all_same(diags):
			print(f'Player {diags[0]} is the winner Diagonally (\\)')
			return True

	#vertical
	for col in range(len(game)):
		check = []
		for row in game:
			check.append(row[col])
		if all_same(check):
			print(f'Player {check[0]} is the winner vertically')
			return True
	return False

#A function should not modify the global values. 
#It should take copy of the object or values and return modified objects or values 
def game_board(game_map,player=0, row=0,col=0, just_display=False):
	try:
		if(game_map[row][col] != 0):
			print('This position already occupied, choose another')
			return game_map, False

		if not just_display:
			game_map[row][col] = player
		print("   "+"  ".join([str(i)  for i in range(len(game_map))]))
		for count,row in enumerate(game_map):
			
			colored_row = ''
			for i in row:
				if i == 0:
					colored_row += Fore.RED+" - "+Style.RESET_ALL
				elif i == 1:
					colored_row += Fore.GREEN +" X "+Style.RESET_ALL
				elif i == 2:
					colored_row += Fore.MAGENTA +" O "+Style.RESET_ALL
			print(count,colored_row)

		return game_map,True
	except IndexError as e :
		print('input row/column as 0 or 1 or 2')
		return game_map,False
	except Exception as e:
		print('Something went wrong')
		return game_map,False

play = True
players = [1,2]
while  play:
	game_size = int(input('Enter game size for tic toc toe: '))
	game = [[0 for i in range(game_size)] for i in range(game_size)]
	game,_ = game_board(game,just_display=True) 
	game_won = False
	player = itertools.cycle(players)
	while not game_won:
		current_player = next(player)
		print(f"Current Player: {current_player}")
		played = False
		while not played:
			row = int(input("Select row (0,1,2):"))
			column = int(input("Select column (0,1,2):"))
			game,played =game_board(game,current_player,row,column)
		if win(game):
			game_won = True
			again = input("The game is over, would you like to play again ? (y/n) :")
			if again.lower() == "y":
				print('Restarting')
			elif again.lower() == 'n':
				print('Thanks for playing... Bye')
				play  = False
			else:
				print('Wrong input.. exiting the game')



#game = game_board(game,just_display=True)  
#game =game_board(game,1,1,1) # game_board(player=1, row=1,col=1)


#win(game)
