#!/usr/bin/python3

# AoC 2021 Problem 13 Solutions

from io import IncrementalNewlineDecoder

fname = "input13.txt"

dbg = False
dbg = True
if dbg: fname = "foo.txt"


def ansa():
    return 0

def ansb():
    return 0



def main():
    f = open(fname)
    lines = f.readlines()
    paths = []
    for l in lines:
        l = l.strip()
        w = l.split(',')
        paths.append(w)
    paths.sort()
    for p in paths:
        print(p)
    resa = ansa()
    print("Resa: {0}".format(resa))
    resb = ansb()
    print("Resb: {0}".format(resb))

main()
