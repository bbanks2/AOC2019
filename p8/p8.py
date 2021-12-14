#!/usr/bin/python

# AoC 2019 Problem 8 solution
# Author: Brad Banks    2019-12-25

class LayeredImage:
    def __init__(self, nrows, ncols):
        self.nrows = nrows
        self.ncols = ncols
        self.layers = []

    def readImage(self, input):
        self.layers = []
        input.strip()

        nitems_per_layer = self.nrows * self.ncols
        if (len(input) % nitems_per_layer != 0):
            raise RuntimeError("Length of input {0} isn't a multiple of image dimensions {1} by {2}".format(len(input), self.nrows, self.ncols))

        nlayers = int(len(input) / nitems_per_layer)
        for k in range(0, nlayers):
            self.layers.append( ImageLayer(self.nrows, self.ncols) )
            start_layer_idx = k*nitems_per_layer
            end_layer_idx = (k+1)*nitems_per_layer
            self.layers[k].readLayer(input[start_layer_idx:end_layer_idx])

    def printImage(self):
        for k in range(0, len(self.layers)):
            print("****  Layer {0}  ****".format(k))
            self.layers[k].printLayer()

    def errorCheck(self):
        min_zeros_cnt = 10**9
        min_zeros_layer = -1
        for k in range(0, len(self.layers)):
            if (self.layers[k].freq_cnts[0] < min_zeros_cnt):
                min_zeros_layer = k
                min_zeros_cnt = self.layers[k].freq_cnts[0]
            ones = self.layers[min_zeros_layer].freq_cnts[1]
            twos = self.layers[min_zeros_layer].freq_cnts[2] 
        return ones * twos

    def renderImage(self):
        rendered_layer = ImageLayer(self.nrows, self.ncols)

        for i in range(self.nrows):
            transparent_col = ['x'] * self.ncols
            rgrid = rendered_layer.grid
            rgrid.append( transparent_col.copy() )

        for l in self.layers:
            for i in range(self.nrows):
                for j in range(self.ncols):
                    if rgrid[i][j] == 'x' and l.grid[i][j] != 2:
                        if l.grid[i][j] == 0:
                            rgrid[i][j] = ' '
                        elif l.grid[i][j] == 1:
                            rgrid[i][j] = '*'
                        else:
                            raise RuntimeError("invalid value {0} found in a layer")
        rendered_layer.printLayer()

class ImageLayer:
    def __init__(self, nrows, ncols):
        self.nrows = nrows
        self.ncols = ncols
        self.grid = []

    def readLayer(self, input):
        self.grid = []
        self.freq_cnts = [0] * 10

        input.strip()
        if (self.nrows * self.ncols != len(input)):
            raise RuntimeError("Length of input {0} doesn't match image dimensions {1} by {2}".format(len(input), self.nrows, self.ncols))

        idx = 0
        for i in range(0, self.nrows):
            self.grid.append([])
            for j in range(0, self.ncols):
                val = int(input[idx])
                self.grid[i].append(val)
                self.freq_cnts[val] += 1
                idx += 1

    def printLayer(self):
        for i in range(0, self.nrows):
            s = ''
            for j in range(0, self.ncols):
                s += str(self.grid[i][j])
            print(s)

def main():
    fname = "input8.txt"
    nrows = 6
    ncols = 25

    dbg = False
    if dbg:
        fname = "testinp8.txt"
        nrows = 2
        ncols = 3

    image = LayeredImage(nrows, ncols)
    for l in open(fname).readlines():
        image.readImage( l )
        # image.printImage()
        res = image.errorCheck()
        print("Error check result: {0}".format(res))
        image.renderImage()

main()