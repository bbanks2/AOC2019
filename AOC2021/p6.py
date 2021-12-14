#!/usr/bin/python3

# AoC 2021 Problem 6 Solutions

from io import IncrementalNewlineDecoder
#from os import lseek

fname = "input6.txt"

dbg = False
#dbg = True
if dbg: fname = "testinp6.txt"

existfishdays = 6
createfishdays = 8

def ansa(days_init, ndays):
    fish = [0] * (createfishdays + 1)
    for d in days_init:
        fish[d] += 1

    for n in range(ndays):
        nxtfish = [0] * 9
        # slide all the fish down a day
        nxtfish[0:createfishdays] = fish[1:createfishdays+1]

        # repro the day 0 dudes
        nxtfish[existfishdays] += fish[0]
        nxtfish[createfishdays] += fish[0]

        fish = nxtfish

    print(fish)
    return sum(fish)

def ansb(days_init, ndays):
    fish = [0] * (createfishdays + 1)
    for d in days_init:
        fish[d] += 1

    for n in range(ndays):
        nxtfish = [0] * 9
        # slide all the fish down a day
        nxtfish[0:createfishdays] = fish[1:createfishdays+1]

        # repro the day 0 dudes
        nxtfish[existfishdays] += fish[0]
        nxtfish[createfishdays] += fish[0]

        fish = nxtfish

    print(fish)
    return sum(fish)

def main():
    f = open(fname)
    line = f.readline()
    days = list(map(int, line.split(',')))
    print(days)    

    resa = ansa(days, 80)
    print("Resa: {0}".format(resa))
    resb = ansb(days, 256)
    print("Resb: {0}".format(resb))

main()
