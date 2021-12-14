#!/usr/bin/python

# AoC 2019 p6 solution
# Author: Brad Banks 2019-12-19

class Node:
    def __init__(self, label, parent_label, level):
        self.label = label
        self.parent_label = parent_label
        self.level = level
        self.children = []

    def __str__(self):
        res = ""
        try:
            if (self.level != None and self.level > 0):
                res = "Node {0} {1} {2}".format(self.label, self.parent_label, self.level)
            else:
                res = "{0} None {1}".format(self.label, self.level)
            res += "   Children: ["
            for child in self.children:
                res += " {0},".format(child.label)
            res = res[:-1]
            res += " ]"
        except AttributeError:
            res = "Node {0} with parent_label {1} couldn't convert to a string".format(self.label, self.parent_label)
        return res

class OrbitalMap:
    def __init__(self):
        self.nodes = {}
        self.root_node = None

    def parseMap(self, fname):
        self.nodes = {}
        for l in open(fname).readlines():
            w = l.strip().split(')')
            if (len(w) != 2): raise RuntimeError("Line in orbit map has unexpected format")
            parent_label = w[0]
            child_label = w[1]
            try:
                parent = self.nodes[parent_label]
            except KeyError:
                parent = Node( parent_label, None, None )
                self.nodes[parent_label] = parent

            try:
                child = self.nodes[child_label]
                child.parent_label = parent_label
            except KeyError: 
                child = Node( child_label, parent_label, None )
                self.nodes[child_label] = child
            parent.children.append( child )

        for node in self.nodes.values():
            if (node.parent_label is None):
                if (self.root_node != None):
                    raise RuntimeError("Found another node: {0} but I already have a root node".format(node))
                self.root_node = node
                print("Found root node: {0}".format(node))

        if (self.root_node == None):
            raise RuntimeError("No node in map is a possible root node, all have a parent")

        processed_nodes = self.advanceLevel(self.root_node, 0)
        if (processed_nodes != len(self.nodes)):
            raise RuntimeError("Number of processed_nodes != ttl_nodes")
        
    def advanceLevel(self, node, level):
        node.level = level
        processed_nodes = 1
        for child in node.children:
            processed_nodes += self.advanceLevel(child, level + 1)
        return processed_nodes

    def calcTotalOrbits(self):
        orbits = 0
        for v in self.nodes.values():
            orbits += v.level
        return orbits

    def findDistanceBetweenOrbits(self, ostart, ofinish):
        start = self.nodes[ostart]
        finish = self.nodes[ofinish]

        start_path = []
        finish_path = []
        paths = [(start, start_path), (finish, finish_path)]
#        next_node_label = start.parent
        for (node, path) in paths:
            while node.parent_label != None:
                path.append(node.parent_label)
                node = self.nodes[node.parent_label]
            path.reverse()
        min_level = min(start.level, finish.level)
        print(start_path)
        print(finish_path)
        for i in range(0,min_level+1):
            if (start_path[i] != finish_path[i]):
                print("Diverged at level {0} with labels startpath {1} and finishpath {2}".format(i, start_path[i], finish_path[i]))
                diverge_level = i
                break
        steps = start.level - i
        steps += finish.level - i
        return steps
    # find path from root to start, and from root to finish
    # compare the two until they diverge
    # from point of divergence, add level diff from diverge to start and level diff from diverge to finish


    def printOrbits(self):
        curlevel = 0
        matched = True
        while matched:
            matched = False
            for node in self.nodes.values():
                if (node.level == curlevel):
                    matched = True
                    print(node)
            curlevel += 1

def main():
    fname = "input6.txt"

    dbg = False
    if (dbg): fname = "testinp6.txt"
    
    orbital_map = OrbitalMap()
    orbital_map.parseMap( fname )
    res = orbital_map.calcTotalOrbits()
    print("Total number of orbits is: {0}".format(res))

#    orbital_map.printOrbits()
    steps = orbital_map.findDistanceBetweenOrbits("YOU", "SAN")
    print("Total orbital steps from YOU to SAN is {0}".format(steps))

main()
