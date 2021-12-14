#!/usr/bin/python3

# AoC 2021 Problem 4a and 4b Solution

from io import IncrementalNewlineDecoder
from os import lseek
#from posix import XATTR_SIZEMAX

fname = "input7.txt"

dbg = False
# dbg = True
if dbg: fname = "testinp7.txt"


def ans7():
    l = open(fname).readline()
    w = l.split(',')
    xs = []
    sum = max = 0
    min = 10**20
    for e in w:
        x = int(e)
        xs.append(x)
        sum += x
        if (min > x):
            min = x
        if (max < x):
            max = x

    avg = sum / len(w)
    ravg = round(avg)
    print("Sum: {0} avg: {1} ravg: {2} min: {3} max: {4}".format(sum, avg, ravg, min, max))
    minstepsa = minposa = minstepsb = minposb = 10**20
    for pos in range(min,max+1):
        fuelstepsa = fuelstepsb = 0
        for x in xs:
            fuelstepsa += abs(x - pos)
            fuelstepsb += abs(x-pos) * (abs(x-pos) + 1) / 2
        if (fuelstepsa < minstepsa):
            minstepsa = fuelstepsa
            minposa = pos
            print ("New minstepsa: {0} at minposa: {1}".format(minstepsa, minposa))
        if (fuelstepsb < minstepsb):
            minstepsb = fuelstepsb
            minposb = pos
            print ("New minstepsb: {0} at minposb: {1}".format(minstepsb, minposb))
    return [minstepsa, minstepsb]


def main():
    res = ans7()
    print("Resa: {0}".format(res[0]))
    print("Resb: {0}".format(res[1]))

main()
