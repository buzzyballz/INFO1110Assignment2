
class Tile:
		
	def __init__(self, highest_elevation, *lowest_elevation):
		"""
		Initialises the terrain tile and attributes
		"""
		self.highest_elevation = highest_elevation
		self.lowest_elevation = lowest_elevation
	
	
	def elevation(self):
		"""
		Returns an integer value of the elevation number 
		of the terrain object
		"""
		pass
	
	def is_shaded(self):
		"""
		Returns True if the terrain tile is shaded, otherwise False
		"""
		pass
	
	def set_occupant(self, obj):
		"""
		Sets the occupant on the terrain tile
		"""
		pass
	
	def get_occupant(self):
		"""
		Gets the entity on the terrain tile
		If nothing is on this tile, it should return None
		"""
		pass
	
	
