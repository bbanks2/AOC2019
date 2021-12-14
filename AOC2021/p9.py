#!/usr/bin/python3

# AoC 2021 Problem 9 Solutions

from io import IncrementalNewlineDecoder
#from os import lseek

fname = "input9.txt"

dbg = False
#dbg = True
if dbg: fname = "testinp9.txt"


def ansa():
    return 0

def ansb():
    return 0

def tryPoint(i, j, val, seenijs, tryijs, seennines, lpoints, n, hmap):
    if(hmap[i][j] >= val):
        if(hmap[i][j] == 9):
            if(tuple([i,j]) not in seennines):
                seennines.add(tuple([i,j]))
                lpoints[i][j] = 9
        else:
            if(tuple([i, j]) not in seenijs):
                seenijs.add(tuple([i,j]))
                tryijs.append([i,j])
                lpoints[i][j] = n

def main():
    f = open(fname)
    lines = f.readlines()
    hmap = []
    lpoints = []
    for l in lines:
        w = l.split()
        row = []
        lprow = []
        for i in range(len(w[0])):
            row.append(int(w[0][i]))
            lprow.append(1)
        hmap.append(row)
        lpoints.append(lprow)
    print(lpoints)

    xlen = len(hmap[0])
    ylen = len(hmap)
    for i in range(ylen):       
        for j in range(xlen):
            if(j > 0):
                if(hmap[i][j] >= hmap[i][j-1]):
                    lpoints[i][j] = 0
            if(j < xlen - 1):
                if(hmap[i][j] >= hmap[i][j+1]):
                    lpoints[i][j] = 0
            if(i > 0):
                if(hmap[i][j] >= hmap[i-1][j]):
                    lpoints[i][j] = 0
            if(i < ylen - 1):
                if(hmap[i][j] >= hmap[i+1][j]):
                    lpoints[i][j] = 0
    print(hmap)
    print(lpoints)
    resa = 0
    basins = []
    for i, lprow in enumerate(lpoints):
        for j, v in enumerate(lprow):
            if (v > 0):
                resa += hmap[i][j] + 1
                basins.append([i,j])
    print("Resa: {0}".format(resa))

    basinsizes = []
    idxtryijs = 0
    seenijs = set()
    seennines = set()
    tryijs = []

    for n, basin in enumerate(basins):
        j = basin[1]
        i = basin[0]
        basinsize = 0

        if(tuple([i, j]) in seenijs):
            raise(RuntimeError("A new basin is already in seenijs"))
        seenijs.add(tuple([i,j]))
        tryijs.append([i,j])
        lpoints[i][j] = 'B'
 
        while(len(tryijs) != idxtryijs):
            i = tryijs[idxtryijs][0]
            j = tryijs[idxtryijs][1]
            val = hmap[i][j]
            if(basinsize > 0):
                lpoints[i][j] = n+1
            if(j > 0):
                tryPoint(i, j-1, val, seenijs, tryijs, seennines, lpoints, n, hmap)
            if(j < xlen - 1):
                tryPoint(i, j+1, val, seenijs, tryijs, seennines, lpoints, n, hmap)
            if(i > 0):
                tryPoint(i-1, j, val, seenijs, tryijs, seennines, lpoints, n, hmap)
            if(i < ylen - 1):
                tryPoint(i+1, j, val, seenijs, tryijs, seennines, lpoints, n, hmap)
            basinsize += 1
            idxtryijs += 1
        basinsizes.append(basinsize)

    print("Basins: ", basins)
    print("Lpoint basins:")
    for lprow in lpoints:
        print(lprow)
    print("Basinsizes: ", basinsizes)
    print("Idxtryijs: ", idxtryijs)
    print("Gridsize: ", xlen*ylen, " Sumbs: ", sum(basinsizes), "Nines: ", len(seennines))
    print("Tryijs: ", tryijs)
    resb = sorted(basinsizes, reverse=True)

    print("Sorted basinsizes: {0}".format(resb))
    print("Resb: ", resb[0] * resb[1] * resb[2])

main()
