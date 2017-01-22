#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 23:27:16 2016

@author: jyon
"""
import numpy as np

def process_permutation(a):
    print(a)

def construct_candidates(a, k, n):
    #print(a)
    in_perm = np.empty([n])
    in_perm.fill(False)
    c = []
    if (k>0):
        for k in range(0, k):
            in_perm[int(a[k])] = True
    for i in range(0, n):
        if (not in_perm[i]):
          c.append(i)
    #print(c)
    return c

def backtrack(a, k, n):
    if (k==n-1):
        process_permutation(a)
    else:
        k = k+1
        c = construct_candidates(a, k, n)
        for cai in c:
            a[k] = cai
            backtrack(a, k, n)

n = 4
a = np.empty([n])
a.fill(False)
backtrack(a, -1, n)