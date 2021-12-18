#!/usr/bin/python3

# AoC 2021 Problem 15 Solutions

from io import IncrementalNewlineDecoder
from networkx import DiGraph
from math import floor

from networkx.algorithms.coloring.greedy_coloring import _maximal_independent_set
fname = "input15.txt"

dbg = False
#dbg = True
if dbg: fname = "testinp15.txt"

def printGraph(wg):
    print("Num nodes: ", len(wg.nodes()))#, " Nodes: ", wg.nodes())
    print("Num edges: ", len(wg.edges()))#, " Edges: ", wg.edges())
    print("Weight 1000,1001: ", wg[1000][1001])

def dijstrka(wg, start, end):
    dists = {}
    steps = {}
    paths = {}
    Q = []
    maxd = 10**10
    for node in wg.nodes():
        if(node != start):
            dists[node] = maxd
            steps[node] = maxd
        else:
            dists[start] = 0
            steps[start] = 0
            paths[start] = [start]
        Q.append(node)

    while (Q):
        nxtmindist = maxd
        nxtnode = len(dists)
        for n in Q:
            if(dists[n] < nxtmindist):
                nxtmindist = dists[n]
                nxtnode = n
        Q.remove(nxtnode)
        for node in wg.successors(nxtnode):
            w = wg.edges[nxtnode, node]['weight']
            ndist = dists[nxtnode] + w
            if(ndist < dists[node]):
                dists[node] = ndist
                steps[node] = steps[nxtnode] + 1
#                print("Adding node: ", node, " to path for nxtnode: ", nxtnode)
#               print("Nextnode path: ", paths[nxtnode])
                paths[node] = paths[nxtnode] + [node] # can't append because append doesn't return a copy which we need here
    print(dists)
    print(steps)
    sum = 0
    pn = -1
    for i, n in enumerate(paths[end]):
        if (pn != -1):
            w = wg.edges[pn, n]['weight']
            sum += w
            print("i: {0}   n: {1}  w: {2}".format(i, n, w))
        pn = n
    print("Sum of w for above path: ", sum)
    return(dists[end])

def nodeid(i ,j):
    return(1000*i + j)

def getij_for_nodeid(nodeid):
    i = floor(nodeid / 1000)
    j = nodeid % 1000
    return([i, j])

def main():
    f = open(fname)
    lines = f.readlines()
    cavern = []
    for i, l in enumerate(lines):
        l = l.strip()
        row = []
        for j in range(len(l)):
            row.append(int(l[j]))
        cavern.append(row)
    print("maxi: {0} maxj: {1}".format(i, j))

    graph = DiGraph()
    for i in range(len(cavern)):
#        print(cavern[i])
        for j in range(len(cavern[i])):
            nodeida = nodeid(i, j)
            # add edges in both dirs to nodes that are to right and below current i,j. Assume edges to/from left and above are already added
            if(j < len(cavern[i]) - 1):
                nodeidb = nodeid(i, j+1)
                graph.add_edge(nodeida, nodeidb, weight=cavern[i][j+1])
                graph.add_edge(nodeidb, nodeida, weight=cavern[i][j])
            if(i < len(cavern) - 1):
                nodeidb = nodeid(i+1, j)
                graph.add_edge(nodeida, nodeidb, weight=cavern[i+1][j])
                graph.add_edge(nodeidb, nodeida, weight=cavern[i][j])

#    printGraph(graph)
    start = nodeid(0, 0)
    end = nodeid(len(cavern) - 1, len(cavern[0]) - 1)
    print("Start: ", start, " End: ", end)

    resa = dijstrka(graph, start, end)
    print("Resa: ", resa)

    # part b, cavern is now 5x5 of the original with each point + 1 with a wraparound from 9 to 1 per tile
    cavern = []
    for y in range(5):
        for i, l in enumerate(lines):
            l = l.strip()
            row = []
            for x in range(5):
                for j in range(len(l)):
                    val = (int(l[j]) + x + y )
                    if(val > 9):
                        val -= 9
                    row.append(val)
            cavern.append(row)
            print(row)
    print("maxi: {0} maxj: {1}".format(len(cavern)-1, len(cavern[0])-1))
    graph = DiGraph()
    for i in range(len(cavern)):
#        print(cavern[i])
        for j in range(len(cavern[i])):
            nodeida = nodeid(i, j)
            # add edges in both dirs to nodes that are to right and below current i,j. Assume edges to/from left and above are already added
            if(j < len(cavern[i]) - 1):
                nodeidb = nodeid(i, j+1)
                graph.add_edge(nodeida, nodeidb, weight=cavern[i][j+1])
                graph.add_edge(nodeidb, nodeida, weight=cavern[i][j])
            if(i < len(cavern) - 1):
                nodeidb = nodeid(i+1, j)
                graph.add_edge(nodeida, nodeidb, weight=cavern[i+1][j])
                graph.add_edge(nodeidb, nodeida, weight=cavern[i][j])

    printGraph(graph)
    start = nodeid(0, 0)
    end = nodeid(len(cavern) - 1, len(cavern[0]) - 1)
    print("Start: ", start, " End: ", end)

    resb = dijstrka(graph, start, end)
    print("Resb: ", resb)

main()