#!/usr/bin/python

# AoC 2019 P4 solution
# Author: Brad Banks 2019-12-20

def check_password( v, check_not_three ):
    has_exactly_two_repeated = False
    has_repeated = False
    monotonic_increasing = True
#    if (v % 100000 == 0):

#    print("v: {0}  len(v): {1}".format(v, len(v)))
    runcnt = 1
    for i in range(1,len(v)):
        if (v[i] == v[i-1]):
            has_repeated = True
            runcnt += 1
            if (runcnt == 2 and i == len(v)-1):
                has_exactly_two_repeated = True
        else:
            if (runcnt == 2):
                has_exactly_two_repeated = True
            runcnt = 1

        if (v[i] < v[i-1]):
            monotonic_increasing = False

    if (check_not_three):
        res = ( len(v) == 6 and has_exactly_two_repeated and monotonic_increasing )
    else:
        res = ( len(v) == 6 and has_repeated and monotonic_increasing )
    return res

def main():
    rangemin = 382345
    rangemax = 843167

    satisfy_cnt = 0
    for i in range(rangemin, rangemax+1):
        if (check_password(str(i), False)):
            satisfy_cnt += 1

    print("Satisfy count two or more: {0}".format(satisfy_cnt))

    satisfy_cnt = 0
    for i in range(rangemin, rangemax+1):
        if (check_password(str(i), True)):
            satisfy_cnt += 1

    print("Satisfy count exactly two: {0}".format(satisfy_cnt))

main()
