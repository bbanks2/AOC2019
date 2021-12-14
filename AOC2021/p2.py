#!/usr/bin/python3

# AoC 2021 Problem 2a and 2b Solution

from io import IncrementalNewlineDecoder


fname = "input2a.txt"

dbg = False
if dbg: fname = "testinp2a.txt"


def ans2a():
    horpos = 0
    depth = 0

    for l in open(fname).readlines():
        w = l.split()
        if (w[0] == "forward"):
            horpos += int(w[1])
        elif (w[0] == "up"):
            depth -= int(w[1])
        elif (w[0] == "down"):
            depth += int(w[1])

    return depth * horpos

def ans2b():
    horpos = 0
    depth = 0
    aim = 0

    for l in open(fname).readlines():
        w = l.split()
        if (w[0] == "forward"):
            horpos += int(w[1])
            depth += aim * int(w[1])
        elif (w[0] == "up"):
            aim -= int(w[1])
        elif (w[0] == "down"):
            aim += int(w[1])

    return depth * horpos


def main():
    resa = ans2a()
    print("Resa: {0}".format(resa))
    resb = ans2b()
    print("Resb: {0}".format(resb))

main()
