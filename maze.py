#import libraries
import pygame
from random import *

#window Size and tile size
SIZE = WIDTH, HEIGHT = 800, 600
TILE = 50
cols, rows = WIDTH // TILE, HEIGHT // TILE


pygame.init()
#set screen to display size for color settings later
screen=pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

class Cell:
    def __init__(self, x, y):
        #cordinates of cell
        self.x, self.y = x, y
        #dictionary for cell sides
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        #Whether the cell is visited
        self.visited = False

    #Cell that creates the maze
    def draw_current_cell(self):
    	x, y = self.x * TILE, self.y * TILE
    	pygame.draw.rect(screen, pygame.Color('green'), (x + 2, y + 2, TILE - 2, TILE - 2))

    #Draw sides of cell
    def draw(self):
        x, y = self.x * TILE, self.y * TILE
        #If cell is visited paint black
        if self.visited:
            pygame.draw.rect(screen, pygame.Color('black'), (x, y, TILE, TILE))
        #Which sides the walls have left depending on dictionary
        if self.walls['top']:
            pygame.draw.line(screen, pygame.Color('red'), (x, y), (x + TILE, y), 2)
        if self.walls['right']:
            pygame.draw.line(screen, pygame.Color('red'), (x + TILE, y), (x + TILE, y + TILE), 2)
        if self.walls['bottom']:
            pygame.draw.line(screen, pygame.Color('red'), (x + TILE, y + TILE), (x , y + TILE), 2)
        if self.walls['left']:
            pygame.draw.line(screen, pygame.Color('red'), (x, y + TILE), (x, y), 2)

    def check_cell(self, x, y):
        #Allows you to find elements in a 1D array knowing its index in a 2D array
        find_index = lambda x, y: x + y * cols
        #check if cell doesnt go beyond the edges of the field
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return grid_cells[find_index(x, y)]

    #check cells and return random neighboring cell
    def check_neighbors(self):
        neighbors = []
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False


def remove_walls(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False

#Put cell class in a 1D array
grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
current_cell = grid_cells[0]
#Define stack as an empty list
stack = []

while True:
	screen.fill(pygame.Color('indigo'))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	#go throough all cells and call their methods
	[cell.draw() for cell in grid_cells]
	current_cell.visited = True
	current_cell.draw_current_cell()

    #Define next cell as the result from check neighbor
	next_cell = current_cell.check_neighbors()
    #if not false value
	if next_cell:
		next_cell.visited = True
		remove_walls(current_cell, next_cell)
		stack.append(current_cell)
		current_cell = next_cell
	elif stack:
		current_cell = stack.pop()


	pygame.display.flip()
	clock.tick(20)



