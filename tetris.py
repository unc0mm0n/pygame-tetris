from piece import *
from random import choice
from utils import Vector

import time

DEFAULT_WIDTH = 10
DEFAULT_HEIGHT = 21
DEFAULT_SIZE = 4

STARTING_SPEED = 5
SPEED_INCREMENT = 0.1



COLORS = [
	(255, 0, 0),
	(0, 255, 0),
	(0, 0, 255),
	(0, 255, 255)
]

class Tetris(object):
	'''Manage the tetris game, call update to move the game a step forward.'''

	def __init__(self, width = DEFAULT_WIDTH, height = DEFAULT_HEIGHT, piece_size = DEFAULT_SIZE):
		self.width = width - 1
		self.height = height - 1
		self.piece_size = piece_size
		self.reset()

	def new_piece(self, size):
		piece = Piece.Random( size, choice(COLORS) )
		piece.move( Vector((self.width // 2, 0)) )
		return piece

	def reset(self):
		self.playing = True
		self.board = []
		self.current_piece = None
		self.lines_cleared = 0
		self.speed = STARTING_SPEED

	def current_can_down(self):
		next_location = self.current_piece.copy()
		next_location.move(DOWN)

		for block in next_location:
			if block.pos[1] > self.height:
				return False

			for location in self.board:
				if block.corguent(location):
					return False

		return True

	def update(self):
		if self.current_piece is None:
			self.current_piece = self.new_piece(self.piece_size)
			if not self.current_can_down():
				self.playing = False

		if self.current_can_down():
			self.current_piece.move(DOWN)
		else:
			for block in self.current_piece:
				self.board.append(block)
			self.current_piece = None

		#TODO: Check Scoring

	def pprint(self):
		occupied = {}
		print('--'*self.width)
		if self.current_piece:
			for block in self.current_piece:
				occupied[block.pos] = 'c'

		for block in self.board:
			occupied[block.pos] = 'O'

		for y in range(self.height + 1):
			for x in range(self.width + 1):
				print(occupied.get((x, y), '.'),end = ' ')
			print()
		print('--'*self.width, '\n')

if __name__ == '__main__':
	t = Tetris(piece_size = 4)

	while t.playing:
		t.update()
		t.pprint()
		time.sleep(0.1)
