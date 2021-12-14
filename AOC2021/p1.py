#!/usr/bin/python3

# AoC 2021 Problem 1a and 1b Solution

from io import IncrementalNewlineDecoder


fname = "input1a.txt"

dbg = False
if dbg: fname = "testinp1a.txt"


def ans1a():
    increasecnt = 0
    prev = -1
    for l in open(fname).readlines():
        msmt = int(l)
        if (prev == -1):
            prev = msmt
            continue
        if (msmt > prev):
            increasecnt += 1
        prev = msmt

    return increasecnt

def ans1b():
    increasecnt = 0
    buf = []
    prev = -1
    i = 0
    for l in open(fname).readlines():
        msmt = int(l)
        if (len(buf) < 3):
            buf.append(msmt)
            continue
        if (prev == -1):
            prev = buf[0] + buf[1] + buf[2]
            i = 3 # i is lncnt - 1 so the 4th line will push out the 1st line
        else:
            i += 1
        
        buf[i%3] = msmt
        nwsum = buf[0] + buf[1] + buf[2]
        if (nwsum > prev):
            increasecnt += 1
        prev = nwsum

    return increasecnt


def main():
    increasecnt = ans1a()
    print("Total Increases: {0}".format(increasecnt))
    increasecnt = ans1b()
    print("Total Increases of 3sum: {0}".format(increasecnt))

main()
