# Object Oriented programming - Introduction, Blob class object creation &
# multiple
# blob objects creation
# Modularity - removing all hardcoded values in the class and making them
# configurable from outside
# Inheriting parent/base/super class and overriding the values of it from child
# Operator overloading : + - * / 
# Detecting collision 
# class
import pygame
import random
from blob import Blob
import numpy as np

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 15
STARTING_GREEN_BLOBS = 5
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
	def __init__(self, x_boundary, y_boundary):
		#super().__init__(color, x_boundary, y_boundary)
		Blob.__init__(self, (0, 0, 255), x_boundary, y_boundary) # this will cause
		#problems when it comes to multiple inheritence

	def __add__(self, other_blob):
		if other_blob.color ==  (255, 0, 0):
			self.size -=  other_blob.size
			other_blob.size -=  self.size
			
		elif other_blob.color == (0, 255, 0):
			self.size +=  other_blob.size
			other_blob.size = 0
		elif other_blob.color == (00,0,255):
			pass
		else:
			raise Exception('Unsuported color is passed')
			
			
	'''def move(self): # overrides super class method definition 
		self.x += random.randrange(-7, 7)
		self.y += random.randrange(-7, 7)'''
class RedBlob(Blob):
	def __init__(self, x_boundary, y_boundary):
		Blob.__init__(self, (255, 0, 0), x_boundary, y_boundary) # this will cause


class GreenBlob(Blob):
	def __init__(self, x_boundary, y_boundary):
		Blob.__init__(self, (0, 255, 0), x_boundary, y_boundary) # this will cause


def is_touching(b1, b2):
	return np.linalg.norm(np.array([b1.x, b1.y]) - np.array([b2.x, b2.y])) < (b1.size + b2.size)

def handle_collisions(blob_list):
	blues, reds, greens = blob_list
	for blue_id, blue_blob in blues.copy().items():
		for other_blobs in blues,reds, greens:
			for other_id , other_blob in other_blobs.copy().items():
				if blue_blob == other_blob:
					pass
				else:
					if is_touching(blue_blob, other_blob):
						blue_blob + other_blob
						if other_blob.size <= 0:
							del other_blobs[other_id]
						if blue_blob.size <= 0:
							del blue_blobs[blue_id]
	return blues, reds, greens
				


	

		
def draw_environment(blob_list):
	game_display.fill(WHITE)
	blues, reds, greens =handle_collisions(blob_list)
	for blob_dict in blob_list:
		for blob_id in blob_dict:
			blob = blob_dict[blob_id]
			pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
			blob.move()
	pygame.display.update()
	return blues, reds, greens
def main():
	#red_blob = Blob(BLUE)
	blue_blobs = dict(enumerate([BlueBlob(WIDTH, HEIGHT) for _ in range(STARTING_BLUE_BLOBS)]))
	red_blobs = dict(enumerate([RedBlob(WIDTH, HEIGHT) for _ in range(STARTING_RED_BLOBS)]))
	green_blobs = dict(enumerate([GreenBlob(WIDTH, HEIGHT) for _ in range(STARTING_GREEN_BLOBS)]))
	display_screen = True
	'''
	print('blue size : {} , red size: {}'.format(blue_blobs[0].size, red_blobs[0].size))
	blue_blobs[0] + red_blobs[0]
	print('blue size : {} , red size: {}'.format(blue_blobs[0].size, red_blobs[0].size))
	'''
	while display_screen:
		
		blues, reds, greens = draw_environment([blue_blobs, red_blobs, green_blobs])
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				display_screen = False


if __name__ == '__main__':
	main()