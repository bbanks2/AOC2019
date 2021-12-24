#!/usr/bin/python3

# AoC 2021 Problem 18 Solutions

from io import IncrementalNewlineDecoder

fname = "input18.txt"

dbg = False
dbg = True
if dbg: fname = "testinp18.1.txt"

class Snailfish():
    def __init__(self):
        self.lst = []

    def addToLst(self, sf):
        return self.addSFs(self.lst, sf)

    def addSFs(self, lhs, rhs):
        self.lst = lhs + rhs
        return self.lst.copy()

def ansa():
    return 0

def ansb():
    return 0



def main():
    sf = Snailfish()
    f = open(fname)
    lines = f.readlines()
    sflines = []
    for i ,l in enumerate(lines):
        l = l.strip()
        wcnt = 0
        while(len(l) != 0):
            if(l[0] == '['): # falling asleep here
                print("L42 p18 resume here")
            cnt += 1
            l = l[1:]

        sf.addToLst( l )
    print("Sf.lst: ", sf.lst)
    resa = ansa()
    print("Resa: {0}".format(resa))
    resb = ansb()
    print("Resb: {0}".format(resb))

main()
