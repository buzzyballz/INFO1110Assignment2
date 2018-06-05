import sys
from loader import load_level

def quit():
	"""
	Will quit the program
	"""
	sys.exit()
	
def menu_help():
	"""
	Displays the help menu of the game
	"""
	print("START <level file> - Starts the game with a provided file.")
	print("QUIT - Quits the game")
	print("HELP - Shows this message")

def menu_start_game(filepath):
	"""
	Will start the game with the given file path
	"""
	load_level(filepath)

def menu():
	"""
	Start the menu component of the game
	"""
	while True:
		user_input = raw_input()
		if 'START' in user_input:
			print(user_input[6:])
			menu_start_game(user_input[6:])
		elif user_input == 'QUIT':
			quit()
		elif user_input == 'HELP':
			menu_help()
			continue
		else:
			print("No menu item")
			continue

menu()
