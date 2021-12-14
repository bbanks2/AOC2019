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
        self.callstack = 0
        self.totalrecursecalls = 0
        self.maxcallstack = 0

    def setRules(self, rules):
        self.rules = rules.copy()

    def setStart(self, start):
        self.start = start

    def recursePair(self, pair, numsteps):
        if(numsteps == 0):
            self.freqcnt[ord(pair[0]) - ord('A')] += 1
            # print("Recpair reached base for end pair: {0} , now self.freqcnt is: {1}".format(pair, self.freqcnt))
            return
        inschar = self.rules.get(pair)
        npair1 = pair[0] + inschar
        npair2 = inschar + pair[1]
        self.totalrecursecalls += 1
        if (self.totalrecursecalls % 1000000 == 0):
            print("At totalcalls: {0} numsteps: {1} for pair: {2} Callstack: {3} Freqcnt: {4}".format(
                self.totalrecursecalls, numsteps, pair, self.callstack, self.freqcnt))
        self.callstack += 1
        if (self.callstack > self.maxcallstack):
            self.maxcallstack = self.callstack
        self.recursePair(npair1, numsteps - 1)
        self.recursePair(npair2, numsteps - 1)
        self.callstack -= 1
#        print("With numsteps: ", numsteps, " left, nstr is: ", nstr)
        return

    def getFreqcnt(self, numsteps):
        self.freqcnt = [0] * 26
        for j in range(1, len(self.start)):
            pstr = self.start[j - 1:j + 1]
            print("Starting recursion for start pair #: {0} pair: {1} for numsteps: {2}".format(j, pstr, numsteps))
            self.recursePair(pstr, numsteps)
#            print("pstr: {0} numsteps: {1} Nstr: {2}".format(pstr, numsteps, nstr))
#            dupl_adjust = 1
#            if(j == len(self.start) - 1):
#                dupl_adjust = 0
#            for i in range(len(nstr) - dupl_adjust):
#                freqcnt[ord(nstr[i]) - ord('A')] += 1
        self.freqcnt[ord(self.start[j]) - ord('A')] += 1
        print("Sum freqcnt: {0} Maxcallstack: {1} Freqcnt: {2}".format(sum(self.freqcnt), self.maxcallstack, self.freqcnt))
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
    numstepsb = 10
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
    nstr = ""
    for i in range(numstepsa):
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
    while (0 in freqcnt):
        freqcnt.remove(0)

    resa = max(freqcnt) - min(freqcnt)
    print("Resa: {0}".format(resa))
    resb = ansb(rules, start, numstepsb)
    print("Resb: {0}".format(resb))

main()
