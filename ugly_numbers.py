#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 11:17:46 2016

@author: jyon
"""
import numpy as np
n = 16
UN = np.arange(n)
pos_2=-1
pos_3=-1
pos_5=-1
UN[0] = 1
for i in range(1, n):
    UN[i] = min(UN[pos_2+1]*2, UN[pos_3+1]*3, UN[pos_5+1]*5)
    #print(UN[i])
    if(UN[i] % (UN[pos_2+1]*2) == 0):
        pos_2 = pos_2 + 1
    if(UN[i] % (UN[pos_3+1]*3) == 0):
        pos_3 = pos_3 + 1
    if(UN[i] % (UN[pos_5+1]*5) == 0):
        pos_5 = pos_5 + 1
    #print(pos_2, pos_3, pos_5)
print(UN[n-1])