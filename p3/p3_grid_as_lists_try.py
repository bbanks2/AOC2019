#!/usr/bin/python3

# AoC 2019 Problem 3 Solution

class WireGrid:
    def __init__(self):
        self.hashgrid = {}
        self.mindist = 10^9
        self.grid = [[]]
        self.intersections = []
        self.ymax = 0

    def addPoint(self, x, y):
        try:
            self.hashgrid[(x,y)] += 1
#            print("Added 1 to count of {0}: {1}".format((x,y), self.hashgrid[(x,y)]))
        except KeyError:
#            print("Inserting {0} to hashgrid".format((x,y)))
            self.hashgrid[(x,y)] = 1

        if ( self.hashgrid[(x,y)] == 2 and not(x==0 and y==0) ):
            self.mindist = min(self.mindist, x+y)
            self.intersections.append( (x,y) )


    def addPointToGrid(self, x, y):
        if (x < 0):
            raise RuntimeError("X cant be negative")
        if (y < 0):
            raise RuntimeError("Y cant be negative")

        self.ymax = max(y, self.ymax)

        if ( x == len(self.grid) ):
            self.grid.append([])
        for i in range( len(self.grid[x]), y+1 ):
            self.grid[x].append(0)

        self.grid[x][y] += 1
        print("Printing after adding point [{0}, {1}]".format(x,y))
        self.printGrid()

        if ( self.grid[x][y] == 2 and not(x==0 and y==0) ):
            self.intersections.append( [x,y] )

    def addWire(self, w):
        x = y = 0
        w = w.split(',')
        self.addPoint(0,0)
        for segment in w:
            print("Adding segment: " + segment)
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
                self.addPoint( x, y )

    def printGrid(self):
        for j in range(0,self.ymax+1):
            j = self.ymax - j
            s = ""
            for i in range( len(self.grid) ):
                if ( j < len(self.grid[i]) ):
                    s += str(self.grid[i][j]) + ' '
                else:
                    s += '. '
            print(s)

    def getIntersections(self):
        return( self.intersections )

def main():
    fname = "input3.txt"

    grid = WireGrid()

    dbg = True
    if ( dbg ):
        fname = "testinp3.txt"
        cnt = 1
        for l in open(fname).readlines():
            if ( cnt % 2 == 1 ):
                grid.reset()
                grid.addWire( l )
            else:
                grid.addWire( l )
#                grid.findClosestIntersection()
                print("Printing intersections after line: {0}".format(cnt))
                for intersection in grid.getIntersections():
                    print(intersection)
#                grid.printGrid()
            cnt += 1
        exit()

main()
