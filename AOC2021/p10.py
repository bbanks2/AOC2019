#!/usr/bin/python3

# AoC 2021 Problem 10 Solutions

from io import IncrementalNewlineDecoder
#from os import lseek

fname = "input10.txt"

dbg = False
#dbg = True
if dbg: fname = "testinp10.txt"

openc = '([{<'
closec = ')]}>'

def chunkya(l):
    stack = []
    for i in range(len(l)):
        if(l[i] in openc):
            stack.append(l[i])
        else:
            z = closec.find(l[i])
            if(stack[-1] != openc[z]):
                return l[i]
            else:
                stack.pop()
    return 0

def ansa(a):
    res = 0
    for e in a:
        if (e == ')'): res += 3
        if (e == ']'): res += 57
        if (e == '}'): res += 1197
        if (e == '>'): res += 25137
    return res

def chunkyb(l):
    stack = []
    for i in range(len(l)):
        if(l[i] in openc):
            stack.append(l[i])
        else:
            z = closec.find(l[i])
            if(stack[-1] != openc[z]):
                return l[i]
            else:
                stack.pop()
    score = 0
    for a in reversed(stack):
        z = openc.find(a)
        score = score * 5 + z + 1
    print("Stack: ", stack, " has score: ", score)
    return score


def main():
    f = open(fname)
    lines = f.readlines()
    inc_lines = []
    bad_chars = []
    for i, l in enumerate(lines):
        res = chunkya(l.strip())
        if (res):
            print("Line #: ", i, " had res: ", res)
            bad_chars.append(res)
        else:
            inc_lines.append(l.strip())
    resa = ansa(bad_chars)
    print("Resa: {0}".format(resa))

    scores = []
    for l in inc_lines:
        scores.append(chunkyb(l))
        scores.sort()
        mididx = int((len(scores) - 1) / 2)
        resb = scores[mididx]
    print("Resb: {0}".format(resb))

main()
