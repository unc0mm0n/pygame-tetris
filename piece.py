from utils import *
from random import *


UP = Vector((0, -1))
DOWN = Vector((0, 1))
LEFT = Vector((-1, 0))
RIGHT = Vector((1, 0))

class Block(object):
	''' A representation of a block. Holds xy coordinates and color
		Supports move operation with Vector
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

	def __len__(self):
		return len(self.pos)

	def move(self, direction):
		return Block(self.pos + direction, self.color)

	def corguent(self, other):
		'''Return true if both blocks are in the same position.'''
		return self.pos == other.pos

class Piece(object):
	''' A representation of a piece built from blocks.'''

	def __generate_piece(size, color):
		'''static method returning a set of Block objects representing a piece of given size.'''
		piece = set()

		loc = tuple((0, 0))
		piece.add(Block(loc, color))
		dirs = [UP, DOWN, RIGHT, LEFT]
		while len(piece) < size:
			if random() > 2:
				#Generate from a random position
				block = choice(tuple(piece))
				direction = choice(dirs)
				loc = block.pos + direction
				piece.add(Block(loc, color))

			else:
				#Generate from the last position
				block = Block(loc, color)
				direction = choice(dirs)
				loc = block.pos + direction
				piece.add(block)
		return piece

	def __init__(self, piece):
		'''Create a piece using a given set of blocks.'''
		self.blocks = set(piece)
		self.dimensions = len(next(iter(piece)))

		self.center = self.__normalize()

	@classmethod
	def Random(cls, size, color):
		'''Create a piece using a random set of blocks, forming a legal, 2 dimensional piece'''
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

	def __eq__(self, other):
		if self.blocks == other.blocks:
			return True
		for _ in range(4):
			self.rotate_cw()
			#print(self, "=======", other)
			#print(self.blocks - other.blocks, '\nROTATING\n\n')
			if self.blocks == other.blocks:
				return True
		return False

	def __hash__(self):
		total = 0
		for block in self.blocks:
			total += hash(block)
		return total

	def move(self, direction):
		'''Move all blocks buidling the piece in the given direction.'''
		new_blocks = set()
		for block in self.blocks:
			new_blocks.add(block.move(direction))
		self.blocks = new_blocks

	def edges(self, dimension):
		'''Returns the two farthest points in given dimension. '''
		blocks = iter(self.blocks)
		lowest = next(blocks).pos[dimension]
		highest = lowest

		for block in blocks:
			height = block.pos[dimension]
			if height < lowest:
				lowest = height
			if height > highest:
				highest = height

		return (lowest, highest)

	def __normalize(self):
		'''Center piece around (0, 0,...,0).'''
		center = Vector(0 for n in range(self.dimensions))

		edges = [self.edges(n) for n in range(self.dimensions)]
		vec = Vector(-sum(edge)//2 for edge in edges)

		while vec != center:
			vec = Vector(-sum(edge)//2 for edge in edges)
			self.move(vec)
			edges = [self.edges(n) for n in range(self.dimensions)]
		#print(vec)

	def copy(self):
		return eval(repr(self))

	def rotate_cw(self):
		new_blocks = set()
		for block in self.blocks:
			x, y = block.pos
			new_blocks.add(Block(Vector((-y, x)), block.color))
		self.blocks = new_blocks

	def pprint(self):
		self.move(Vector((4, 4)))

		occupied = {}
		for block in self.blocks:
			occupied[block.pos] = '*'

		for y in range(8):
			for x in range(8):
				if (x, y) in occupied:
					print('*', end = "")
				else:
					print(' ', end = "")
			print()

		self.move(Vector((-4, -4)))

def main():

	a=Piece({Block(Vector((0, 1)), 'b'), Block(Vector((1, 0)), 'b'), Block(Vector((-1, 0)), 'b'), Block(Vector((0, 0)), 'b')})

	b=Piece({Block(Vector((1, 1)), 'b'), Block(Vector((1, -1)), 'b'), Block(Vector((1, 0)), 'b'), Block(Vector((0, 0)), 'b')})

	#a.pprint()
	#a._Piece__normalize()
	#b._Piece__normalize()
	print(b)
	#print(b)
	#b.pprint()
	#a.rotate_cw()
	#a.pprint()
	print(a==b)

	test_pieces(10000)


def test_pieces(sample_size = 1000):
	pieces = {}
	for _ in range(sample_size):
		piece = Piece.Random(4, 'b')
		found = False
		for _ in range(4):
			if piece in pieces:
				pieces[piece] += 1
				found = True
				break
			piece.rotate_cw()
		if not found:
			pieces[piece] = 1

	for key in pieces:
		key.pprint()
	#	print(key)
		print("{} times".format(pieces[key]))
		print('\n', repr(key))
		print("=====")
	print(len(pieces), "total pieces")


if __name__ == '__main__':
	main()
	