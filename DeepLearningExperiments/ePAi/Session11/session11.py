import random
#from PyClassicRound import classic_round
from decimal import *
import cmath
import math

class Polygon:
    def __init__(self, numedges,circumrad):
      #try:
      if isinstance(numedges, int) and circumrad >0 and numedges > 2:
          self.numedges = numedges
          self.circumrad = circumrad
      else:
          raise ValueError('num edges needs to be a positive integer greater than 2 and circum radius needs to be positive number')
      #except ValueError as ve:
      #  print('Work with number between -1 and 1 only')

    # defining object representation
    def __repr__(self):
      return 'Representation of Polygon Class with ' + str(self.numedges) + ' edges and ' + str(self.circumrad) + ' circum radius'

    def __numedges__(self):
        return self.numedges

    def __interiorangle__(self):
        return (2*self.circumrad)*math.sin(math.pi/self.numedges)

    def __apothem__(self):
        edges= self.numedges
        rad = self.circumrad
        return (rad)*math.cos(math.pi/edges)

    def __edgelength__(self):
        return ((self.numedges-2)*180)/math.pi

    def __area__(self):
        apothemval = self.__apothem__()
        print(apothemval)
        edgelengthval = self.__edgelength__()
        return (self.numedges*apothemval*edgelengthval)/2
    
    def __perimeter__(self):
        edgelengthval = self.__edgelength__()
        return (self.numedges*edgelengthval)

    def __gt__(self,other):
        if isinstance(other, Polygon):
            return (self.numedges > other.numedges) 
        else:
            raise ValueError("Not an instance of Polygon Class")

    def __eq__(self,eqval):
        if isinstance(eqval, Polygon):
            return (self.numedges == eqval.numedges) and (self.circumrad==eqval.circumrad)
        else:
            raise TypeError('Work with number between -1 and 1 only')

if __name__ == '__main__':
    p = Polygon(25,6)
    print(p.__repr__())
    #print(p.__len__())
    print(p[3])
    print(p.maxefficiencypolygon())






























































    def __gt__(self,other):
        if isinstance(other, Polygon):
            return (self.numedges > other.numedges) 
        else:
            raise ValueError("Not an instance of Polygon Class")

    def __eq__(self,eqval):
        if isinstance(eqval, Polygon):
            return (self.numedges == eqval.numedges) and (self.circumrad==eqval.circumrad)
        else:
            raise TypeError('Work with number between -1 and 1 only')

if __name__ == '__main__':
    p = Polygon(4,6)
    print(p.__area__())
    print(f'number of vertices = {p.__numedges__()}\nnumber of edges = {p.__numedges__()}\nEdge Length = {p.__edgelength__()}\ninterior angle = {p.__interiorangle__()}\napothem = {p.__apothem__()}\narea = {p.__area__()}\nperimeter = {p.__perimeter__()}\n')