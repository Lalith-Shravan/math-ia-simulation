from math import *
from point import Point


class OrbitalObject:
    def __init__(self, mass, radius, inclination, longitude):
        self.point = Point(0,0,0)
        self.time = 0
        self.inclination = inclination
        self.longitude = longitude
        self.radius = radius

        G = 6.674e-11
        
        self.angularVelocity = sqrt((G * mass) / pow(self.radius, 3))

        self.move(0)
    
    def move(self, time):
        trueAnamoly = (self.angularVelocity * time) % (2 * pi)
        
        newX = cos(trueAnamoly) * cos(self.longitude) - sin(trueAnamoly) * cos(self.inclination) * sin(self.longitude)
        newX *= self.radius

        newY = cos(trueAnamoly) * sin(self.longitude) + sin(trueAnamoly) * cos(self.inclination) * cos(self.longitude)
        newY *= self.radius

        newZ = sin(trueAnamoly) * sin(self.inclination)
        newZ *= self.radius

        self.point.x = newX
        self.point.y = newY
        self.point.z = newZ
    
    def __repr__(self):
        return f"Current position ({self.point.x}, {self.point.y}, {self.point.z})"
