#!/usr/bin/python3

# AoC 2021 Problem 12 Solutions

from codecs import replace_errors
from io import IncrementalNewlineDecoder
from networkx import Graph

fname = "input12.txt"

dbg = False
#dbg = True
if dbg: fname = "testinp12.txt"

def ansb():
    return 0

def printGraph(dg):
    print("Nodes: ", dg.nodes())
    print("Edges:", dg.edges())

def findPaths(dg, nodelbl, phist, revisit_small_ok, res):
    trynxt = dg.adj[nodelbl]
    next = []
    for e in trynxt:
        phe = phist.copy()
        resmlok = revisit_small_ok
        if(e == 'start'):
            continue
        if(e == 'end'):
            phe.append(e)
            res.append(phe)
            continue
        if(e[0] >= 'A' and e[0] <= 'Z'):
            phe.append(e)
            findPaths(dg, e, phe, resmlok, res)
        else:
            if(e not in phist):
                phe.append(e)
                findPaths(dg, e, phe, resmlok, res)
            else: # duplicate small caveq
                if(resmlok):
                    phe.append(e)
                    resmlok = False
                    findPaths(dg, e, phe, resmlok, res)
                # else: do nothing, just here to show explicitly the case of a repeat when revisit_small_ok is False
        # one of the 4 outcomes happened and now continue to the next e in trynxt
    return len(res)

def main():
    f = open(fname)
    lines = f.readlines()
    graph = Graph()
    for l in lines:
        l = l.strip()
        w = l.split('-')
        graph.add_edge(w[0], w[1])
    printGraph(graph)
    revisit_small_ok = False
    paths = []
    resa = findPaths(graph, 'start', ['start'], revisit_small_ok, paths)
#    print("A: paths: ")
#    paths.sort()
#    for path in paths:
#        print(path)

    revisit_small_ok = True
    paths = []
    resb = findPaths(graph, 'start', ['start'], revisit_small_ok, paths)
#    print("B: paths: ")
#    paths.sort()
#    for path in paths:
#        print(path)

    print("Resa: {0}".format(resa))
    print("Resb: {0}".format(resb))

main()
