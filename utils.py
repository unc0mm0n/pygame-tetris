from collections import deque

class Queue(object):
    '''
        A basic implementation of a queue using a Deque
        O(1) addition and removal

        enqueue(self, item) => Add an item to back of the queue
        dequeue(self, item) => Remove an item from the front of the queue, raise IndexError if empty
        is_empty(self) => return True if empty
    '''

    def __init__(self):
        self.items = deque()

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def enqueue(self, item):
        self.items.appendleft(item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

class Vector(tuple):
    '''
        A basic implementation of a Vector as a tuple.
        supports addition and subtraction of vectors, and multiplication and division by a scalar
    '''

    def __repr__(self):
        return 'Vector({0})'.format(tuple(self))

    def __str__(self):
        return str(tuple(self))

    # Basic operations

    def __add__(self, other):
        return Vector(v + w for v, w in zip(self, other))

    def __radd__(self, other):
        return Vector(w + v for v, w in zip(self, other))

    def __sub__(self, other):
        return Vector(v - w for v, w in zip(self, other))

    def __rsub__(self, other):
        return Vector(w - v for v, w in zip(self, other))

    def __mul__(self, s):
        return Vector(v*s for v in self)

    def __rmul__(self, s):
        return Vector(v*s for v in self)
    
    def __floordiv__(self, s):
        return Vector(v//s for v in self)

    def __rfloordiv__(self, s):
        return Vector(s//v for v in self)

    def __truediv__(self, s):
        return Vector(v/s for v in self)

    def __rtruediv__(self, s):
        return Vector(s/v for v in self)

    def __neg__(self):
        return -1 * self


if __name__ == '__main__':
    a = Vector((2, 3))
    v = Vector((3, 5))
    d = Vector((3, 5, 8))
    print(repr(a))
    print(a+v)
    print(a+v+d)
    print(a*v)
    print(a-v)
    print(v/a)
    b = Vector((2,3))
    print(a==b)