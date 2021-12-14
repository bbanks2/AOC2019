#!/usr/bin/python3

# AoC 2019 Problem 3 Solution

class WireGrid:
    def __init__(self):
        self.hashgrid = {}
        self.mindist = 10**9
        self.intersections = []

    def getMinDist(self):
        return self.mindist

    def getIntersections(self):
        return self.intersections

    def addPoint(self, x, y, val):
        try:
            if (self.hashgrid[(x,y)] != val):
                self.mindist = min(self.mindist, abs(x) + abs(y))
                print("Mindist is: {0} {1}".format(self.mindist, abs(x)+abs(y)))
                self.intersections.append( (x,y) )

#            print("Added 1 to count of {0}: {1}".format((x,y), self.hashgrid[(x,y)]))
        except KeyError:
#            print("Inserting {0} to hashgrid".format((x,y)))
            self.hashgrid[(x,y)] = val

    def addWire(self, w, label):
        x = y = 0
        w = w.split(',')
        for segment in w:
#            print("Adding segment: " + segment)
            dir = segment[0]
            dist = int(segment[1:])
            for i in range(0, dist):
                if ( dir == 'R' ):
                    x += 1
                elif ( dir == 'L' ):
                    x -= 1
                elif ( dir == 'U' ):
                    y += 1
                elif ( dir == 'D' ):
                    y -= 1
                else:
                    raise ValueError("Invalid direction: {0} with dist: {1}".format(dir, dist))
                self.addPoint( x, y, label )

def main():
    dbg = False
    fname = "input3.txt"
    if ( dbg ):
        fname = "testinp3.txt"

    grid = WireGrid()
    cnt = 1
    for l in open(fname).readlines():
        if ( cnt % 2 == 1 ):
            grid = WireGrid()
            grid.addWire( l, 0 )
        else:
            grid.addWire( l, 1 )
            print("Mindist after line: {0} is: {1}".format(cnt, grid.getMinDist()))
            for intersection in grid.getIntersections():
                print(intersection)
#                grid.printGrid()
        cnt += 1

main()
