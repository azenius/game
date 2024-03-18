#migrate to C# cross-platform library
from pygame.math import Vector2 

# resolution
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
TITLE_SIZE = 64

# pos  
OVERLAY_POSITIONS = {
	'tool' : (40, SCREEN_HEIGHT - 15), 
	'seed': (70, SCREEN_HEIGHT - 5)}

PLAYER_TOOL_OFFSET = {
	'left': Vector2(-50,40),
	'right': Vector2(50,40),
	'up': Vector2(0,-10),
	'down': Vector2(0,50)
}

LAYERS = {
	'water': 0,
	'ground': 1,
	'grass': 2,
	'building floor': 3,
	'plants decor': 4,
	'house top': 5,
	'rain drops': 6
}

GROW_SPEED = {
# define
}

SALE_PRICES = {
# define
}
PURCHASE_PRICES = {
# define
}