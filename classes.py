from collections import namedtuple


class Goat:
    legs_number = 4

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def __str__(self):
        return f'wight = {self.weight}, height = {self.height}'



'''namedtuple'''

Point = namedtuple('Point', ['x', 'y', 'z'])
A = Point(1, 2, 3)
A.x  # 1



'''Связный список'''

a = [1]  # [1]
a.append([2])  # [1, [2]]
a[1].append([3, a])  # [1, [2, [3, [...]]]]


a = [1]
a.append([2])
a[1].append([3, None])
p = a
while p is not None:
    # print(p[0])
    p = p[1]
    # print('вот', p[1])


class LinkedList:
    def __init__(self):
        self._begin = None
    
    def insert(self, x):
        self._begin = [x, self._begin]

    def pop(self):
        assert self._begin is not None, 'list is empty'
        x = self._begin[0]
        self._begin = self._begin[1]
        return x
