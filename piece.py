from utils import *
from random import *


UP = Vector((0, -1))
DOWN = Vector((0, 1))
LEFT = Vector((-1, 0))
RIGHT = Vector((1, 0))

class Block(object):
	''' A representation of a block. Holds xy coordinates and color
		Supports move operation with Vector2
	'''

	def __init__(self, pos, color):
		self.pos = pos
		self.color = color

	def __eq__(self, other):
		return self.pos == other.pos and self.color == other.color

	def __hash__(self):
		return hash(hash(self.pos) + hash(self.color))

	def __repr__(self):
		return "Block({}, {})".format(repr(self.pos), repr(self.color))

	def __str__(self):
		return "Block: {}, {}".format(str(self.pos), str(self.color))

	def move(self, direction):
		self.pos += direction

	def corguent(self, other):
		'''Return true if both blocks are in the same position.'''
		return self.pos == other.pos

class Piece(object):
	''' A representation of a piece Built from blocks.'''

	def __generate_piece(size, color):
		'''static method returning a set of Block objects representing a piece of given size.'''
		piece = set()
		
		loc = (0, 0)
		piece.add(Block(loc, color))
		dirs = [DOWN, RIGHT]
		while len(piece) < size:
			block = sample(piece, 1)[0]
			direction = choice(dirs)
			loc = block.pos + direction

			piece.add(Block(loc, color))
		return piece

	def __init__(self, piece):
		'''Create a piece using a given set of blocks.'''
		self.blocks = piece

	@classmethod
	def Random(cls, size, color):
		'''Create a piece using a random set of blocks, forming a legal piece'''
		return cls(Piece.__generate_piece(size, color))

	def __repr__(self):
		return 'Piece({})'.format(self.blocks)

	def __len__(self):
		return len(self.blocks)

	def __str__(self):
		str = 'Piece:\n'
		for block in self.blocks:
			str += '{0}\n'.format(block)
		return str

	def __iter__(self):
		return iter(self.blocks)

	def move(self, direction):
		'''Move all blocks buidling the piece in the given direction.'''
		for block in self.blocks:
			block.move(direction)

if __name__ == '__main__':
	a = Piece.Random(4, 'b')
	b = eval(repr(a))
	print(b)
	b.move(DOWN)
	for _ in range(5):
		b.move(DOWN)
		b.move(RIGHT)
		print(b)
