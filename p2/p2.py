#!/usr/bin/python3

# AoC 2019 Problem 2a Solution

def intcode_parse( l ):
#    inputs = map(int(), l.split(','))
    inputs = l.split(',')
    vals = []
    for inp in inputs:
        vals.append(int(inp))
    return vals

def intcode_calc( vals ):
    # read current opcode
    # get vals and perform op and write result
    # move to next opcode
    # repeat until opcode is 99
    curpos = 0
    while( vals[curpos] != 99 ):
        op = vals[curpos]
        a1 = vals[curpos+1]
        a2 = vals[curpos+2]
        out = vals[curpos+3]
        if ( op == 1 ):
            vals[out] = vals[a1] + vals[a2]
        elif ( op == 2 ):
            vals[out] = vals[a1] * vals[a2]
        else:
            raise ValueError("Invalid Opcode at position: {0} opcode: {1}".format(curpos, vals[curpos]))
        curpos += 4
    return vals[out]

def q1a( vals ):
    # next two lines are to change the two values per the directions in question
    vals[1] = 12
    vals[2] = 2
    res = intcode_calc( vals )
    print("Q1a result is: {0}".format(res))

# def q2b( vals ):
    # need to try replacements for position 1 and 2 such that final output is 19690720


def main():
    fname = "input2.txt"

    dbg = False
    if ( dbg ):
        fname = "testinp2a.txt"
        for l in open(fname).readlines():
            vals = intcode_parse( l )
            res = intcode_calc( vals )
            print("Result is: {0}".format(res))
        exit()

    firstline = True
    for l in open(fname).readlines():
        assert firstline == True
        if ( firstline ):
            vals = intcode_parse( l )
            firstline = False

    q1a( vals.copy() )

main()
