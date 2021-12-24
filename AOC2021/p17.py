#!/usr/bin/python3

# AoC 2021 Problem 17 Solutions

from io import IncrementalNewlineDecoder

fname = "input17.txt"

dbg = False
dbg = True
if dbg: fname = "testinp17.txt"

def ansa():
    return 0

def ansb():
    return 0

class Target():
    def __init__(self, xmin, ymin, xmax, ymax):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
        self.maxypath = []
        self.maxyval = -10**10

    def inTarget(self, x, y):
        return (x >= self.xmin and x <= self.xmax and y >= self.ymin and y <= self.ymax)

    def simPath(self, xvel, yvel):
        path = []
        x = y = 0
        while (y >= self.ymin):
            path.append((x,y))
            if (self.inTarget(x,y)):
                has_maxy = False
                for (xi, yi) in path:
                    if (yi > self.maxyval):
                        self.maxyval = yi
                        self.maxypath = path
                return self.maxyval
            x += xvel
            y += yvel
            if (xvel > 0):
                xvel -= 1
            if (xvel < 0):
                xvel += 1
            yvel -= 1
        return None


def main():
    f = open(fname)
    lines = f.readlines()
    for l in lines:
        l = l.strip()
        w = l.split(',')
        print(w)

    cnt = 0
    targ = Target(81,-150,129,-108)
    for i in range(12,130):
        for j in range(-151,150):
            resa = targ.simPath(i,j)
            if (resa):
                cnt += 1
                print("Resa: {0} cnt: {1} (x, y): ({2}, {3})".format(resa, cnt, i, j))

    cnt = 0
    for i in range(12,130):
        for j in range(-151,150):
            resb = targ.simPath(i,j)
            if (resb):
                cnt += 1
        print("Resb: {0} cnt: {1} (x, y): ({2}, {3})".format(resb, cnt, i, j))

main()
