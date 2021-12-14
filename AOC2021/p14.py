#!/usr/bin/python3

# AoC 2021 Problem 14 Solutions

from io import IncrementalNewlineDecoder

fname = "input14.txt"

dbg = False
#dbg = True
if dbg: fname = "testinp14.txt"


class PolymerPairInserter():
    def __init__(self):
        self.rules = {}
        self.start = {}
        self.freqcnts = [0] * 26

    def readRules(w):

def ansa():
    return 0

def recurse_help(rules, start, numsteps):


def ansb(rules, start, numsteps):
    nstrs = []
    for j in range(1, len(start)):
        pstr = start[j-1:j+1]
        nstrs.append('')
        for i in range(numsteps):
            nstr = ''
            for k in range(1, len(pstr)):
                inschar = rules.get(pstr[k-1:k+1])
                nstr = nstr + pstr[k-1] + inschar
#            print(nstr)
            pstr = nstr + pstr[-1]
            if(len(pstr) > 32 and i < numsteps - 1):
                fcnt1 = recurse_help(rules, pstr(:22), numsteps-i)
                fcnt2 = recurse_help(rules, pstr[22:], numsteps-i)
        if(j < len(start) - 1):
            nstrs[j-1] = pstr[:-1]
        else:
            nstrs[j-1] = pstr
#        print("After step #: ", i, " nstrs[", j-1, "] is: ", nstrs[j-1])


    freqcnt = [0] * 26
    for s in nstrs:
        for i in range(len(s)):
            freqcnt[ord(s[i]) - ord('A')] += 1
    print("Freqcnt: ", freqcnt)
    while ( 0 in freqcnt):
        freqcnt.remove(0)
    return max(freqcnt) - min(freqcnt)


def main():
    f = open(fname)
    lines = f.readlines()
    i = 0
    rules = {}
    for l in lines:
        l = l.strip()
        if(i == 0):
            start = l
            i += 1
            continue
        if(i == 1):
            i += 1
            continue
        w = l.split()
        rules[w[0]] = w[2]
        i += 1
    print(rules)

    pstr = start
    numsteps = 10
    nstr = ""
    for i in range(numsteps):
        nstr = ""
        for j in range(1,len(pstr)):

#            print(pstr[j-1:j+1])
            inschar = rules.get(pstr[j-1:j+1])
            nstr = nstr + pstr[j-1] + inschar
#            print(nstr)
        pstr = nstr + pstr[-1]
        print("After step #: ", i, " len(pstr) is: ", len(pstr))

    freqcnt = [0] * 26
    for i in range(len(pstr)):
        freqcnt[ord(pstr[i]) - ord('A')] += 1
    print("Freqcnt: ", freqcnt)
    while ( 0 in freqcnt):
        freqcnt.remove(0)

    resa = max(freqcnt) - min(freqcnt)
    print("Resa: {0}".format(resa))
    resb = ansb(rules, start, 20)
    print("Resb: {0}".format(resb))

main()
