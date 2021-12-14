#!/usr/bin/python3

# AoC 2019 Problem 3 Solution
# Author: Brad Banks on 2019/12/20

class WireGrid:
    def __init__(self):
        self.hashgrid = {}
        self.pathdists = {}
        self.mindist = 10**9
        self.minpathdist = 10**9

    def addPoint(self, x, y, val):
        self.pathdists[val] += 1
        try:
            (val1, pathdist1) = self.hashgrid[(x,y)]
            if (val != val1):
                self.mindist = min(self.mindist, abs(x) + abs(y))
                self.minpathdist = min(self.minpathdist, self.pathdists[val] + pathdist1)
            # else this wire is tripping over itself, so we leave the existing shorter pathdist untouched
        except KeyError:
            self.hashgrid[(x,y)] = (val, self.pathdists[val])

    def addWire(self, w, label):
        x = y = 0
        self.pathdists[label] = 0
        w = w.split(',')
        for segment in w:
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
            print("Min Manhattan dist for pair of wires #{0} is: {1}".format(int(cnt/2), grid.mindist))
            print("Min path dist for pair of wires #{0} is: {1}".format(int(cnt/2), grid.minpathdist))
        cnt += 1

main()
