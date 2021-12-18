#!/usr/bin/python3

# AoC 2021 Problem 16 Solutions

from io import IncrementalNewlineDecoder

fname = "day16/input16.txt"

dbg = False
#dbg = True
if dbg: fname = "day16/testinp16.1.txt"

maxv = 2**62

def ansa():
    return 0

def ansb():
    return 0

def processPacket(b, maxbcnt, maxpcktstack, versions, structure):
    cnt = pcktcnt = 0
    maxpcktcnt = maxpcktstack[-1]
    while(len(b) > 5 and cnt < maxbcnt and pcktcnt < maxpcktcnt):
        version = int(b[0:3], 2)
        versions.append(version)
        type = int(b[3:6], 2)
        print("vers: {0} type: {1}".format(version, type))
        if (version == 0 and type == 0):
            print("Warning: suspected end of bitstream 0s, but continuing anyway")
        b = b[6:]
        cnt += 6
        if(type == 4):
            structure.append('L')
            literal = ''
            while(b[0] == '1'):
                literal = literal + b[1:5]
                b = b[5:]
                cnt += 5
            literal = literal + b[1:5]
            b = b[5:]
            cnt += 5
            print("int(literal): {0}  literal(bits): {1} remaining b: {2}".format(int(literal, 2), literal, b))
        else: # operator packet
            if(b[0] == '0'):
                structure.append('B')
                bitlen = int(b[1:16], 2)
                maxpcktstack.append(maxv)
                b = b[16:]
                cnt += 16
            else:
                structure.append('P')
                bitlen = maxv
                subpcktlen = int(b[1:12], 2)
                maxpcktstack.append(subpcktlen)
                b = b[12:]
                cnt += 12
                # print("Processed {0} packets with bitcnt: {1} of up to pcktcnt: {2} packets".format(pcktcnt, bcnt, subpcktlen))

            structure.append([])
            if(type == 0):
                optype = 'sum' # PICKUP HERE

            (bcnt, pcktcnt) = processPacket(b, bitlen, maxpcktstack, versions, structure[-1])
            maxpcktcnt += pcktcnt # these packets don't count against maxpcktcnt total becuase they are subpackets
            # print("Processed {0} packets with bitcnt: {1} of up to bitlen: {2} bits".format(pcktcnt, bcnt, bitlen))

            cnt += bcnt
            b = b[bcnt:]
        pcktcnt += 1 # pcktcnt increases by 1 at this parent call level. subpckts cancelled out by being added to both pcktcnt and maxpcktcnt
        print("Starting next packet loop, cnt: {0} pcktcnt: {1} versions: {2} structure: {3} b: {4} ".format(cnt, pcktcnt, versions, structure, b))

    if (cnt >= maxbcnt):
        print("Stopped processing b after reaching cnt: ", cnt, " >= ", maxbcnt)
    if (pcktcnt >= maxpcktcnt):
        print("Stopped processing because processed pcktcnt: {0} of maxpcktcnt: {1} packets".format(pcktcnt, maxpcktcnt))
    if (len(b) <= 5):
        print("Stopped processing because len(b): {0} isn't long enough to be a valid header. b: {1}".format(len(b), b))
    return(cnt, pcktcnt)

def main():
    f = open(fname)
    lines = f.readlines()
    if (dbg):
        lines = []
        lines.append("D2FE28")
        lines.append("38006F45291200")
        lines.append("EE00D40C823060")
        lines.append("8A004A801A8002F478")
        lines.append("620080001611562C8802118E34")
        lines.append("C0015000016115A2E0802F182340")
        lines.append("A0016C880162017C3686B18A3D4780")

    newline_buff = ""
    for l in lines:
        l = l.strip()
        if(newline_buff):
            print(newline_buff)
        print("***** STARTNG NEW PACKET: {0} *****".format(l))
        leading0s = ''
        dgt1 = int(l[0], 16)
        if(dgt1 == 0):
            #raise(RuntimeError("Line starts with char '0', doesn't parse"))
            leading0s = '0000'
            dgt2 = int(l[1], 16)
            if(dgt2 == 0):
                raise(RuntimeError("Line starts with two char '0's, not handled yet, see code"))
            elif(dgt2 < 2):
                leading0s += '000'
            elif(dgt2 < 4):
                leading0s += '00'
            elif(dgt2 < 8):
                leading0s += '0'
        elif(dgt1 < 2):
            leading0s = '000'
        elif(dgt1 < 4):
            leading0s = '00'
        elif(dgt1 < 8):
            leading0s = '0'

        w = '0x' + l
        a = int(w, 0)
        b = bin(a)
        print(w)
        print(a)

        if (b[0] == '0' and b[1] == 'b'):
            b = leading0s + b[2:]
        print(b, "  len(b): ", len(b))
        versions = []
        structure = []
        maxpcktstack = [1]
        (bcnt, pcktcnt) = processPacket(b, maxv, maxpcktstack, versions, structure)
        b = b[bcnt:]
        print("Done processing valid packets. Processed bcnt: {0} bits in pcktcnt: {1} packets, versions: {2} Structure: {3}".format(bcnt, pcktcnt, versions, structure))
        print("Remaining b: ", b)
        resa = sum(versions)
        print("RESA version sum: {0}  for hex string: {1}".format(resa, l))
        resb = ansb()
        print("Resb: {0}".format(resb))
        newline_buff = "\n"
main()
