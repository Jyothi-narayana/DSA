#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 20:29:34 2016

@author: jyon
"""

def DP(lower, upper):
    if (lower == upper):
        return 0
    #elif (lower + 1 == upper):
    #    return lower
    elif not (lower < upper):
        return 0
    else:
        mini = 10000
        #print(lower, upper)
        for i in range(lower, upper):
            #if i == lower:
            #    res = DP(i+1, upper) + i
            #else:
            res = max(DP(lower, i-1), DP(i+1, upper)) + i
            if (res < mini):
                mini = res
        return res

print(DP(1, 10))