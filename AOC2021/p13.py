#!/usr/bin/python3

# AoC 2021 Problem 13 Solutions

from io import IncrementalNewlineDecoder

fname = "input13.txt"

dbg = False
#dbg = True
if dbg: fname = "testinp13.txt"

class MarkedPaper():
    def __init__(self):
        self.paper = []
        self.xmax = 0
        self.ymax = 0
        self.visdotcnt = 0

    def markPoints(self, points):
        for e in points:
            if(e[0] > self.xmax): self.xmax = e[0]
            if(e[1] > self.ymax): self.ymax = e[1]


        for i in range(self.ymax + 1):
            row = []
            for j in range(self.xmax + 1):
                row.append('.')
            self.paper.append(row)

        for e in points:
            self.paper[e[1]][e[0]] = '#'
            self.visdotcnt += 1

    def fold(self, fold):
        if(fold[0] == 'y'):
            oppidx = 0
            for i in range(fold[1] + 1, len(self.paper)):
                oppidx += 2
                row = self.paper[i]
                for j in range(len(row)):
                    if(row[j] == '#'):
                        self.paper[i-oppidx][j] = '#'
            self.paper = self.paper[:fold[1]]
            self.ymax = fold[1] - 1
        if(fold[0] == 'x'):
            oppidx = 0
            for i in range(len(self.paper)):
                row = self.paper[i]
                oppidx = 0
                for j in range(fold[1] + 1, self.xmax + 1):
                    oppidx += 2
                    if(row[j] == '#'):
                        self.paper[i][j-oppidx] = '#'
                self.paper[i] = row[:fold[1]]
            self.xmax = fold[1] - 1
        self.visdotcnt = 0
        for i in range(len(self.paper)):
            for j in range(len(self.paper[i])):
                if (self.paper[i][j] == '#'):
                    self.visdotcnt += 1
        return self.visdotcnt

    def pMP(self):
        print("xmax: ", self.xmax, " ymax: ", self.ymax, " visdotcnt: ", self.visdotcnt)
        for i in range(len(self.paper)):
            str1 = ""
            print(str1.join(self.paper[i]))


def ansa():
    return 0

def ansb():
    return 0



def main():
    f = open(fname)
    lines = f.readlines()
    points = []
    folds = []
    for l in lines:
        l = l.strip()
        w = l.split(',')
        if(len(w) == 2):
            w[0] = int(w[0])
            w[1] = int(w[1])
            points.append(w)
        if(len(w) == 1 and 'fold' in w[0]):
            w = w[0].split()
            w = w[2].split('=')
            w[1] = int(w[1])
            folds.append(w)
    print("points:\n", points)
    print("folds:\n", folds)

    mp = MarkedPaper()
    mp.markPoints(points)
    mp.pMP()

    for i, fold in enumerate(folds):
        print("Applying fold #: ", i, " with fold info: ", fold)
        mp.fold(fold)
        mp.pMP()

    resa = ansa()
    print("Resa: {0}".format(resa))
    resb = ansb()
    print("Resb: {0}".format(resb))

main()
