from tile import Tile
from planet import Planet

def load_level(filename):
	"""
	Loads the level and returns an object of your choosing
	"""
	file = open(filename, "r")
	lines = file.readlines()
	for i in range(len(lines)):
		lines[i] = lines[i].rstrip()
	name = lines[1][5:]
	width = int(lines[2][6:])
	height = int(lines[3][7:])
	planet = Planet(name, width, height)
	tiles = []
	temp = []
	counter = 1
	for i in range(7, len(lines)):
		t = lines[i].split(",")
		if len(t) == 2:
			t = Tile(t[0], t[1])
		elif len(t) == 3:
			t = Tile(t[0], t[1], t[2])
		temp.append(t)
		if counter == planet.width:
			tiles.append(temp)
			temp = []
			counter = 1
		else:
			counter += 1
	return tiles

load_level("first.level")
