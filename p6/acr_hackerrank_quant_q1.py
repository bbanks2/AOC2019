#!/usr/bin/python

# Athena Hackerrank Quant test Q1
# Author: Brad Banks 2020-07-30

# Compute Rolling Min

class RollingMin(object):
    def __init__(self, interval_length):
        self.interval_length = interval_length
        self.obs = []
        self.currMin = tuple([-9999999999999, 9999999999999])
 
    def update(self, time, value):
        new_obs = tuple([time, value])
        recompute = False or len(self.obs) == 0
        cutoff_time = time - self.interval_length
        while len(self.obs) > 0 and self.obs[0][0] <= cutoff_time:
            if self.obs[0][1] <= self.currMin[1]:
                recompute = True
            self.obs.pop(0)
        self.obs.append(new_obs)
        if recompute:
            self.currMin = min(self.obs, key=lambda x: x[1])
        else:
            self.currMin = min(self.currMin, new_obs, key=lambda x: x[1])
        return self.currMin[1]

def main():
    minfinder = RollingMin( 2 )

    obs = [[1, 100], [2, 103], [3, 104]]
    
    for o in obs:
        minfinder.update(o[0], o[1])
        print("Current minimum time and value are: {0} , {1}".format(minfinder.currMin[0], minfinder.currMin[1]))

main()
