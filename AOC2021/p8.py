#!/usr/bin/python3

# AoC 2021 Problem 8 Solutions

from abc import abstractproperty
from io import IncrementalNewlineDecoder
from itertools import permutations
#from os import lseek

fname = "input8.txt"

dbg = False
#dbg = True
if dbg: fname = "testinp8.txt"


def ansa():
    return 0

def ansb():
    return 0

def ansa(a):
    cnts = [0] * 10
    for e in a:
        for o in e:
            if(len(o) == 2):
                cnts[1] += 1
            elif(len(o) == 3):
                cnts[7] += 1
            elif(len(o) == 4):
                cnts[4] += 1
            elif(len(o) == 7):
                cnts[8] += 1

#    print(cnts)
    return sum(cnts)

def freqDecode(note):
    freqcnts = [0] * 7
    possible_decodes = [[], 0, [], [], 0, 0, []]
    for w in note:
        for i in range(len(w)):
            freqcnts[ord(w[i]) - ord('a')] += 1
    for i, freqcnt in enumerate(freqcnts):
        # first 3 unique cnts
        if(freqcnt == 4): # this is 'e'
            possible_decodes[4] = chr(i + ord('a'))
        if(freqcnt == 6): # this is 'b'
            possible_decodes[1] = chr(i + ord('a'))
        if(freqcnt == 9): # this is 'f'
            possible_decodes[5] = chr(i + ord('a'))
        # now multi possibilities        
        if(freqcnt == 7): # this is 'd' or 'g'
            possible_decodes[3].append(chr(i + ord('a')))
            possible_decodes[6].append(chr(i + ord('a')))

        if(freqcnt == 8): # this is 'a' or 'c'
            possible_decodes[0].append(chr(i + ord('a')))
            possible_decodes[2].append(chr(i + ord('a')))

#    print(note)
#    print(freqcnts)
#    print(possible_decodes)
    return possible_decodes

def ansb(notes, outputs):        
    blank_decode = [None] * 7
    res = 0
    for i in range(len(notes)):
        note = notes[i]
        decode_complete = False
        possible_decodes = freqDecode(note)
        foundc = False
        while(not decode_complete):
            for w in note:
                    if(len(w) == 2):
                        # remove the 'f' and the one left is 'c' and the other possibility for 'c' is 'a'
                        f = possible_decodes[5]
                        c = w.replace(f, '')
                        possible_decodes[2] = c
                        possible_decodes[0].remove(c)
                        possible_decodes[0] = possible_decodes[0][0]
                        foundc = True
                    if(len(w) == 4 and foundc):
                        # remove the 'bcf' and the one left is 'd' and the other possibility for 'd' is 'g'
                        b = possible_decodes[1]
                        c = possible_decodes[2]
                        f = possible_decodes[5]
                        d = w.replace(b, '').replace(c, '').replace(f, '')
                        possible_decodes[3] = d
                        possible_decodes[6].remove(d)
                        possible_decodes[6] = possible_decodes[6][0]
                        decode_complete = True
                        break

#        print("Possible_decodes: ", possible_decodes)

        output = outputs[i]
        val = 0
        for k, d in enumerate(output):
            d = decodeDigit(d, possible_decodes)
            val += 10**(3-k) * d
#        print("Output: ", output, "decodes to: ", val)
        res += val
    return res

def decodeDigit(d, decoder):
    if(len(d) == 2):
        return 1
    if(len(d) == 3):
        return 7
    if(len(d) == 4):
        return 4
    if(len(d) == 7):
        return 8

    if(len(d) == 5):
        # if it has a 'e' segment lit then it's 2, otherwise check for the 'c' and it's 3, else 5
        if(decoder[4] in d):
            return 2
        else:
            if(decoder[2] in d):
                return 3
            else:
                return 5

    if(len(d) == 6):
        # if 'd' segment not lit then it's 0, otherwise check if 'e' lit and it's 6, else 9
        if(decoder[3] not in d):
            return 0
        else:
            if(decoder[4] in d):
                return 6
            else:
                return 9


def main():
    f = open(fname)
    lines = f.readlines()
    notes = []
    outputs = []
    for l in lines:
        w = l.split('|')
#        print(w)
        notes.append(w[0].split())
        outputs.append(w[1].split())

#    print(notes)
#    print(outputs)

    resa = ansa(outputs)
    print("Resa: {0}".format(resa))
    resb = ansb(notes, outputs)
    print("Resb: {0}".format(resb))

main()
