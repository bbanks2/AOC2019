#!/usr/bin/python3

# AoC 2021 Problem 5a and 5b Solution

from io import IncrementalNewlineDecoder
from os import lseek

fname = "input5a.txt"

dbg = False
#dbg = True
if dbg: fname = "testinp5a.txt"

class GridLines:
    def __init__(self):
        self.lines = []
        self.grid = []
        self.minx = self.miny = 10**20
        self.maxx = self.maxy = 0

    def addLines(self, f, allow_diag):
        for l in f.readlines():
            w = l.split()
            x1y1 = w[0].split(',')
            x2y2 = w[2].split(',')
            x1 = int(x1y1[0])
            y1 = int(x1y1[1])
            x2 = int(x2y2[0])
            y2 = int(x2y2[1])
            if (not allow_diag and x1 != x2 and y1 != y2):
                continue
            if (x1 > x2 or (y1 > y2 and not x1 < x2)):
                tmp = x1
                x1 = x2
                x2 = tmp
                tmp = y1
                y1 = y2
                y2 = tmp

            self.lines.append([[x1, y1], [x2, y2]])
            if (x1 < self.minx):
                self.minx = x1
            if (y1 < self.miny):
                self.miny = y1
            if (x2 > self.maxx):
                self.maxx = x2
            if (y2 > self.maxy):
                self.maxy = y2

        print(self.minx, self.miny, self.maxx, self.maxy)
#        print(self.lines)
#        print(self)

    def buildGrid(self):
        for y in range(self.miny, self.maxy+1):
            row = []
            for x in range(self.minx, self.maxx+1):
                row.append(0)
            self.grid.append(row)
#        print("Grid y-dim len: ", len(self.grid), " x-dim: ", len(self.grid[0]))

        for l in self.lines:
            # vert line
            if (l[0][0] == l[1][0]):
                x = l[0][0] - self.minx
                for y in range(l[0][1], l[1][1]  + 1):
#                    print("Vert line adding 1 to point ", x+self.minx, y)
                    self.grid[y-self.miny][x] += 1
            elif (l[0][1] == l[1][1]):
                y = l[0][1] - self.miny
                for x in range(l[0][0], l[1][0] + 1):
#                    print("Horiz line adding 1 to point ", x, y+self.miny)
                    self.grid[y][x-self.minx] += 1
            elif (abs(l[1][0] - l[0][0]) == abs(l[1][1] - l[0][1])):
                # need to check that it's a 45 degree angle point
                i = 0
                y = l[0][1]
                yreverse = (y > l[1][1])
                for x in range(l[0][0], l[1][0] + 1):
#                    print("Diag line adding 1 to point ", x, y+i)
                    self.grid[y+i-self.miny][x-self.minx] += 1
                    if(yreverse):
                        i -= 1
                    else:
                        i += 1
            else:
                raise RuntimeError("Neither x nor y are equal or have the same difference, so not a horizontal, vertical or diagonal line")

#        print(self)
        return 0

    def countMultis(self):
        count = 0
        for r in self.grid:
            for e in r:
                if (e > 1):
                    count += 1
        return count

    def __str__(self):
        res = ""
        try:
            for row in self.grid:
                res += str(row) + "\n"

        except AttributeError:
            res = "Couldn't convert to a string".format(self.rows)
        return res



def ans5a():
    f = open(fname)

    gridlines = GridLines()
    gridlines.addLines(f, False)
    gridlines.buildGrid()
    f.close()
    return gridlines.countMultis()

def ans5b():
    f = open(fname)
    gridlines = GridLines()
    gridlines.addLines(f, True)
    gridlines.buildGrid()
    f.close()
    return gridlines.countMultis()

def main():

    resa = ans5a()
    print("Resa: {0}".format(resa))
    resb = ans5b()
    print("Resb: {0}".format(resb))

main()
