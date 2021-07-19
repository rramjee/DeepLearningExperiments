import random
from collections import namedtuple 
#from PyClassicRound import classic_round
from decimal import *
import cmath
import math
from session11 import Polygon

class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._polygons = [Polygon(i, R) for i in range(3, m+1)]
        
    def __len__(self):
        return self._m - 2
    
    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'

    def __iter__(self):
        return self.PolyIterator(self)
    
    def __getitem__(self, s):
        return self._polygons[s]
    
    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons, 
                                 key=lambda p: p.area/p.perimeter,
                                reverse=True)
        return sorted_polygons[0]

    class PolyIterator:
        def __init__(self, poly_obj):
            self._poly_obj = poly_obj
            self._index = 0
            
        def __iter__(self):
            return self

        def __next__(self):
            if self._index >= len(self._poly_obj):
                raise StopIteration
            else:
                item = self._poly_obj._polygons[self._index]
                self._index += 1
                return item