#!/usr/bin/python3

# AoC 2021 Problem 4a and 4b Solution

from io import IncrementalNewlineDecoder
from os import lseek

fname = "input4a.txt"

dbg = False
#dbg = True
if dbg: fname = "testinp4a.txt"

class Board:
    def __init__(self):
        self.rows = []
        self.marks = []

    def addLine(self, w):
        row = []
        blankmark = []
        for e in w:
            row.append(int(e))
            blankmark.append(0)
        self.rows.append(row)
        self.marks.append(blankmark)

    def checkWin(self, i, j):
        # check row
        if (self.marks[i].count(1) == 5):
            return True
        # check col
        cnt = 0
        for rmark in self.marks:
            if (rmark[j] == 1):
                cnt += 1
        if (cnt == 5):
            return True
        return False

    def calcScoreAtWin(self, draw):
        sumunmark = 0
        for i in range(0,5):
            for j in range(0,5):
                if (self.marks[i][j] == 0):
                    sumunmark += self.rows[i][j]
        return sumunmark * draw

    def markNum(self, n):
        i = j = 0
        for r in self.rows:
            try:
                j = r.index(n)
            except ValueError:
                i += 1
                continue
            self.marks[i][j] = 1
            if (self.checkWin(i, j)):
                return self.calcScoreAtWin(n)
            i += 1
        return False



    def nrows(self):
        return len(self.rows)

    def __str__(self):
        res = ""
        try:
            for row in self.rows:
                res += str(row) + "\n"
            for rmark in self.marks:
                res += str(rmark) + "\n"

        except AttributeError:
            res = "Couldn't convert to a string".format(self.rows)
        return res


def ans4a():
    lncnt = 0
    boards = []
    draws = []
    nextBoard = False
    for l in open(fname).readlines():
        lncnt += 1
        if (lncnt == 1):
            drawstrs = l.split(',')
            for e in drawstrs:
                draws.append(int(e))
        else:
            w = l.split()
            if (len(w) == 0):
                print("Zero line, nextBoard is: ", nextBoard)
                if (nextBoard and nextBoard.nrows() == 5):
                    boards.append(nextBoard)
                nextBoard = Board()
                continue
            print("Calling addLine: ", w)
            nextBoard.addLine(w)

    print("File finished, nextBoard is: ", nextBoard)
    if (nextBoard and nextBoard.nrows() == 5):
        boards.append(nextBoard)

    print("draws: ", draws)
    print("boards:\n")
    for b in boards:
        print(b)

    for d in draws:
        for i, b in enumerate(boards):
            res = b.markNum(d)
            if (res):
                print ("Winning board is #: ", i+1, " with score: ", res, " and here it is:\n", b)
                return res

    print("boards:\n")
    for b in boards:
        print(b)

    return 0

def ans4b():
    lncnt = 0
    boards = []
    draws = []
    nextBoard = False
    for l in open(fname).readlines():
        lncnt += 1
        if (lncnt == 1):
            drawstrs = l.split(',')
            for e in drawstrs:
                draws.append(int(e))
        else:
            w = l.split()
            if (len(w) == 0):
                print("Zero line, nextBoard is: ", nextBoard)
                if (nextBoard and nextBoard.nrows() == 5):
                    boards.append(nextBoard)
                nextBoard = Board()
                continue
            print("Calling addLine: ", w)
            nextBoard.addLine(w)

    print("File finished, nextBoard is: ", nextBoard)
    if (nextBoard and nextBoard.nrows() == 5):
        boards.append(nextBoard)

    print("draws: ", draws)
    print("boards:\n")
    for b in boards:
        print(b)

    tbrem = []
    lastres = 0
    for d in draws:
        for i, b in enumerate(boards):
            res = b.markNum(d)
            if (res):
                print ("Winning board is #: ", i+1, " with score: ", res, " and here it is:\n", b)
                lastres = res
                tbrem.append(i)
        if (tbrem):
            for i, e in enumerate(tbrem):
                print("Removing board#: ", e)
                del boards[e - i]
            tbrem = []

    print("boards:\n")
    for b in boards:
        print(b)

    return lastres


def main():
    resa = ans4a()
    print("Resa: {0}".format(resa))
    resb = ans4b()
    print("Resb: {0}".format(resb))

main()


