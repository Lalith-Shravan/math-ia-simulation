from math import *

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def distanceTo(self, point):
        return sqrt(pow((self.x - point.x),2) + pow((self.y - point.y),2) + pow((self.z - point.z),2))