#!/usr/bin/python3

# AoC 2021 Problem 11 Solutions

from io import IncrementalNewlineDecoder
#from os import lseek

fname = "input11.txt"

dbg = False
#dbg = True
if dbg: fname = "testinp11.txt"

class OctoGrid():
    def __init__(self):
        self.flashcnt = 0
        self.grid = []
        self.flashed = []
        self.stepcnt = 0

    def initGrid(self, lines):
        self.grid = []
        self.flashed = []
        for i in range(len(lines)):
            l = lines[i]
            row = []
            frow = []
            for j in range(len(l)):
                row.append(int(l[j]))
                frow.append(0)
            self.grid.append(row)
            self.flashed.append(frow)
        self.pGrid()

    def step(self):
        # first increment all vals, make flashed grid while at it
        prev_flashcnt = self.flashcnt
        self.stepcnt += 1
        g = self.grid
        flashed = self.flashed
        for i in range(len(g)):
            r = g[i]
            for j in range(len(r)):
                g[i][j] += 1
        print("Stepping, after increment:")
        self.pGrid()

        # flash
        for i in range(len(g)):
            r = g[i]
            for j in range(len(r)):
                if(g[i][j] > 9 and not flashed[i][j]):
                    self.flash(i, j)

        print("After flashing:")
        self.pGrid()
        if(self.flashcnt - prev_flashcnt == 100):
            return True
        # reset all flashed vals to 0
        for i in range(len(g)):
            r = g[i]
            for j in range(len(r)): 
                if(g[i][j] > 9 and flashed[i][j]):
                    g[i][j] = 0
                    flashed[i][j] = 0
        print("After reset:")
        self.pGrid()
        return False

    def flash(self, i, j):
        self.flashed[i][j] = 1
        self.flashcnt += 1

        g = self.grid
        if(i>0):
            if (j>0):
                self.flashPoint(i-1,j-1)
            self.flashPoint(i-1,j)
            if (j<len(g[i])-1):
                self.flashPoint(i-1,j+1)
        if (j>0):
            self.flashPoint(i,j-1)
        if (j<len(g[i])-1):
            self.flashPoint(i,j+1)
        if (i<len(g)-1):
            if (j>0):
                self.flashPoint(i+1,j-1)
            self.flashPoint(i+1,j)
            if (j<len(g[i])-1):
                self.flashPoint(i+1,j+1)

    def flashPoint(self, i, j):
        g = self.grid
        g[i][j] += 1
        if(g[i][j] > 9 and not self.flashed[i][j]):
            self.flash(i, j)

    def pGrid(self):
        g = self.grid
        for i in range(len(g)):
            print(g[i])
        print("Flashed for above on step #: ", self.stepcnt)
        for i in range(len(self.flashed)):
            print(self.flashed[i])
        print()


def ansa():
    return 0

def ansb():
    return 0



def main():
    f = open(fname)
    lines = f.readlines()
    for i, l in enumerate(lines):
        lines[i] = lines[i].strip()

    octocave = OctoGrid()
    octocave.initGrid(lines)
    for i in range(100):
        octocave.step()

    print("Resa: {0}".format(octocave.flashcnt))
    synced = False
    while (not synced):
        i += 1
        synced = octocave.step()

    resb = i
    print("Resb: {0}".format(resb))

main()
