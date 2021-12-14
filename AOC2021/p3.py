#!/usr/bin/python3

# AoC 2021 Problem 3a and 3b Solution

from io import IncrementalNewlineDecoder
from os import lseek

fname = "input3a.txt"

dbg = False
#dbg = True
if dbg: fname = "testinp3b.txt"


def ans3a():
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    d = 0
    p = 0
    lncnt = 0

    for l in open(fname).readlines():
        lncnt += 1
        w = l.split()
        w = w[0]
        for i in [0,1,2,3,4,5,6,7,8,9,10,11]:
            a[i] += int(w[i])
#        print(a)
#        elif (w[0] == ""):
#            d = int(w[1])

    denom = lncnt / 2
    res = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    resdec = 0
    for i in [0,1,2,3,4,5,6,7,8,9,10,11]:
        if (a[i] > denom):
            res[i] = 1
            resdec += 2**(11-i)
    eps = 2**12 - resdec - 1
#    print("res: ", res)
#    print("Resdec: {0} eps: {1} 2**12: {2}".format(resdec, eps, 2**12))
    return resdec * eps


def ans3b():
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    lncnt = 0
    lines = []

    for l in open(fname).readlines():
        lncnt += 1
        w = l.split()
        w = w[0]
        lines.append(w)
        for i in [0,1,2,3,4,5,6,7,8,9,10,11]:
            a[i] += int(w[i])

    oxy = lines.copy()
    cos = lines.copy()
    oxybit = 0
    cosbit = 0
    if (a[0] > len(oxy) / 2):
        oxybit = 1
    elif (a[0] == len(oxy) / 2):
        oxybit = 1
        cosbit = 1
    else:
        cosbit = 1

    i = 0
    print("Oxy: {0} Cos: {1}  i: {2}".format(oxy, cos, i))

    while(True):
        if (len(oxy) > 1):
            noxy = []
            loxy = len(oxy)
            for e in oxy:
                print(int(e[i]))
                if (int(e[i]) == oxybit):
                    print("Appending: ", e)
                    noxy.append(e)
            if (len(noxy) > 1):
                noxybitcnt = 0
                for e in noxy:
                    noxybitcnt += int(e[i+1])
                if (noxybitcnt >= len(noxy) / 2):
                    oxybit = 1
                else:
                    oxybit = 0
            oxy = noxy.copy()
            print(oxy)

        if (len(cos) > 1):
            ncos = []
            lcos = len(cos)
            for e in cos:
                if (int(e[i]) == cosbit):
                    ncos.append(e)
            if (len(ncos) > 1):
                ncosbitcnt = 0
                for e in ncos:
                    ncosbitcnt += int(e[i+1])
                if (ncosbitcnt < len(ncos) / 2):
                    cosbit = 1
                else:
                    cosbit = 0
            cos = ncos.copy()
            print(cos)

        if (len(oxy) == 1 and len(cos) == 1):
            break
        if (len(oxy) == 0 or len(cos) == 0):
            print("Error: Oxy: {0} Cos: {1}  i: {2}".format(oxy, cos, i))
            return -1
        i += 1
        print("Starting next loop, i: ", i)

    print("Done. Oxy: {0} Cos: {1}".format(oxy, cos))

    oxy = oxy[0]
    cos = cos[0]
    oxydec = 0
    cosdec = 0
    for i in [0,1,2,3,4,5,6,7,8,9,10,11]:
#    for i in [0,1,2,3,4]:

        if (int(oxy[i]) == 1):
            oxydec += 2**(11-i)
        if (int(cos[i]) == 1):
            cosdec += 2**(11-i)
    print("Oxydec: {0} Cosdec: {1}".format(oxydec, cosdec))
    return oxydec * cosdec

def main():
#    resa = ans3a()
#    print("Resa: {0}".format(resa))
    resb = ans3b()
    print("Resb: {0}".format(resb))

main()
