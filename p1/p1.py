#!/usr/bin/python3

fname = "input1a.txt"

dbg = False
if dbg: fname = "testinp1a.txt"

def calc_fuelreq( mass ):
    fr = int((mass / 3 )) - 2
    if (fr < 0):
        fr = 0
    return fr

def ans1a():
    fuelreq = 0
    for l in open(fname).readlines():
        mass = int(l)
        fuelreq += calc_fuelreq( mass )
#        print("Mass: {0}  Fuel: {1}".format(mass, fuelreq))
    return fuelreq

def ans1b():
    fuelreq = 0
    for l in open(fname).readlines():
        mass = int(l)
        module_fr = 0
        fr = mass
        while ( fr >= 9 ): # fr less than 9 will have 0 fuel requirement
            fr = calc_fuelreq( fr )
            module_fr += fr

#        print("Mass: {0}  Fuel: {1}".format(mass, module_fr))
        fuelreq += module_fr
    return fuelreq

def main():
    fuelreq = ans1a()
    print("Total Fuelreq: {0}".format(fuelreq))
    fuelreq = ans1b()
    print("Total Fuelreq: {0}".format(fuelreq))

main()
