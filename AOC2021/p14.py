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
        self.freqcnt = [0] * 26

    def setRules(self, rules):
        self.rules = rules.copy()
        self.paircnts = {}
        for k in rules.keys():
            self.paircnts[k] = 0

    def setStart(self, start):
        self.start = start
        for j in range(1, len(self.start)):
            pstr = self.start[j - 1:j + 1]
            self.paircnts[pstr] += 1
#        print("Paircnts: ", self.paircnts)

    def stepPaircnts(self):
        freqcnt = [0] * 26
        ncnts = self.paircnts.copy()
        for k, v in self.rules.items():
            pcnt = self.paircnts[k]
            lpair = k[0] + v
            rpair = v + k[1]
            ncnts[k] -= pcnt
            ncnts[lpair] += pcnt
            ncnts[rpair] += pcnt
            freqcnt[ord(k[0]) - ord('A')] += pcnt
            freqcnt[ord(v) - ord('A')] += pcnt
            # Don't add the right side cause it double counts for any letter not on extreme left or right end.
            # Add the +1 for right end letter in caller
        self.paircnts = ncnts
        return freqcnt

    def getFreqcnt(self, numsteps):
        for i in range(numsteps):
            self.prevfc = self.freqcnt
            self.freqcnt = self.stepPaircnts()
            self.freqcnt[ord(self.start[-1]) - ord('A')] += 1 # adding the +1 for rightmost letter
#            print("Numsteps: {0} Sum freqcnt: {1} Freqcnt: {2}".format(i+1, sum(self.freqcnt), self.freqcnt))
#        for i in range(len(self.freqcnt)):
#            print(i, self.prevfc[i], self.freqcnt[i] - self.prevfc[i])
        return self.freqcnt

def ansa():
    return 0

def ansb(rules, start, numsteps):
    ppi = PolymerPairInserter()
    ppi.setRules(rules)
    ppi.setStart(start)
    freqcnt = ppi.getFreqcnt(numsteps)

    while (0 in freqcnt):
        freqcnt.remove(0)

    return(max(freqcnt) - min(freqcnt))


def main():
    numstepsa = 10
    numstepsb = 40
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
#    print(rules)

    pstr = start
    nstr = ""
    for i in range(numstepsa):
        nstr = ""
        for j in range(1,len(pstr)):

            #            print(pstr[j-1:j+1])
            inschar = rules.get(pstr[j-1:j+1])
            nstr = nstr + pstr[j-1] + inschar
#            print(nstr)
        pstr = nstr + pstr[-1]
#        print("After step #: ", i, " len(pstr) is: ", len(pstr))

    freqcnt = [0] * 26
    for i in range(len(pstr)):
        freqcnt[ord(pstr[i]) - ord('A')] += 1
#    print("Freqcnt: ", freqcnt)
    while (0 in freqcnt):
        freqcnt.remove(0)

    resa = max(freqcnt) - min(freqcnt)
    print("Resa: {0}".format(resa))
    resb = ansb(rules, start, numstepsb)
    print("Resb: {0}".format(resb))

main()
