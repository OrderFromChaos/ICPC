# Heh, actually n-body
import sys
import re

steps = 1000
DEBUG = False

class Body:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.velx, self.vely, self.velz = 0, 0, 0
    def gravityUpdate(self, other):
        if self.x != other.x:
            self.velx += [-1,1][self.x < other.x]
        if self.y != other.y:
            self.vely += [-1,1][self.y < other.y]
        if self.z != other.z:
            self.velz += [-1,1][self.z < other.z]
    def __repr__(self):
        return ((f"pos=<x={self.x}, y={self.y}, z={self.z}>, "  
                 f"vel=<x={self.velx}, y={self.vely}, z={self.velz}>"))

def totalEnergy(b):
    # potential energy
    pot = sum([abs(q) for q in [b.x, b.y, b.z]])
    # kinetic neergy
    kin = sum([abs(q) for q in [b.velx, b.vely, b.velz]])
    return pot * kin

bodies = []
for line in sys.stdin:
    getnums = re.compile('[-\d]+')
    x, y, z = [int(q) for q in re.findall(getnums, line)]
    bodies.append(Body(x,y,z))

for i in range(steps):
    if DEBUG:
        for b in bodies:
            print(b)
        print(sum([totalEnergy(q) for q in bodies]))

    
    # Update velocities using relative position
    for b1 in bodies:
        for b2 in bodies:
            b1.gravityUpdate(b2)

    # Update position by velocity
    for b in bodies:
        b.x += b.velx
        b.y += b.vely
        b.z += b.velz

if DEBUG:
    for b in bodies:
        print(b)

print(sum([totalEnergy(q) for q in bodies]))