#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 21:02:42 2016

@author: jyon
"""
def interchange(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
def colorsort(nums):
    red_pos = -1
    blue_pos = len(nums)
    for idx, e in enumerate(nums):
        while (nums[red_pos + 1] == 0):
            red_pos  = red_pos + 1
        while (nums[blue_pos-1] == 2):
            blue_pos = blue_pos -1
        if (idx>red_pos and idx < blue_pos):
            #print(e)
            if e == 0:
                #exchange with red_pos + 1
                #print(red_pos, blue_pos)
                if (nums[red_pos + 1] == 2):
                    interchange(nums, red_pos+1, blue_pos-1)
                    interchange(nums, idx, red_pos+1)
                    blue_pos = blue_pos + 1
                else:
                    interchange(nums, idx, red_pos+1)
                red_pos = red_pos + 1
            elif e==2:
                if (nums[blue_pos - 1] == 0):
                    interchange(nums, red_pos+1, blue_pos-1)
                    interchange(nums, idx, blue_pos-1)
                    red_pos = red_pos + 1
                else:
                    interchange(nums, idx, blue_pos-1)
                blue_pos = blue_pos - 1
        #print(nums)
    return nums

print(colorsort([0,1,2,1,2,0,1,2,0,0,1,1,2,0,1,2]))
    