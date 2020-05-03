# Object Oriented programming - Introduction, Blob class object creation &
# multiple
# blob objects creation
# Modularity - removing all hardcoded values in the class and making them
# configurable from outside
# Inheriting parent/base/super class and overriding the values of it from child
# class
import pygame
import random
from blob import Blob


STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 15
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Testing game window')
clock = pygame.time.Clock()

class BlueBlob(Blob):
	#pass
	def __init__(self, color, x_boundary, y_boundary):
		super().__init__(color, x_boundary, y_boundary)
		#Blob.__init__(self, color, x_boundary, y_boundary) # this will cause
		#problems when it comes to multiple inheritence
		self.color = BLUE
	def move(self): # overrides super class method definition 
		self.x += random.randrange(-7, 7)
		self.y += random.randrange(-7, 7)

		
def draw_environment(blob_list):
	game_display.fill(WHITE)
	for blob_dict in blob_list:
		for blob_id in blob_dict:
			blob = blob_dict[blob_id]
			pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
			blob.move()
	pygame.display.update()

def main():
	#red_blob = Blob(BLUE)
	blue_blobs = dict(enumerate([BlueBlob(BLUE, WIDTH, HEIGHT) for _ in range(STARTING_BLUE_BLOBS)]))
	red_blobs = dict(enumerate([BlueBlob(RED,  WIDTH, HEIGHT) for _ in range(STARTING_RED_BLOBS)]))
	display_screen = True
	while display_screen:
		
		draw_environment([blue_blobs,red_blobs])
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				display_screen = False


if __name__ == '__main__':
	main()