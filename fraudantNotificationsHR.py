#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 21:27:15 2016

@author: jyon
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput

def kMedian(k_list, k, mid):
    if (mid):
        return k_list[k/2]
    else:
        return (k_list[k/2] + k_list[(k/2) - 1])/float(2)

def insertionPoint(arr, n, e):
    low = 0
    high = n-1
    while (low < high):
        mid = (low+high)/2
        if (e == arr[mid]):
            return mid
        if (arr[mid] > e):
            high = mid - 1
        else:
            low = mid + 1
    return low 

def search(arr, n, e):
    low = 0
    high = n-1
    while (low < high):
        mid = (low+high)/2
        if (e == arr[mid]):
            return mid
        if (arr[mid] > e):
            high = mid - 1
        else: 
            low = mid + 1
    return low

first = True
n = 0
k = 0
nums = []
for line in fileinput.input():
    if (first):
        first = False
        s = line.split(" ")
        n = int(s[0])
        k = int(s[1])
    else:
        nums = [ int(x) for x in line.split(" ") ]
if (n <= k):
    print 0
else:
    k_sorted = sorted(nums[0:k])
    n_notification = 0
    #set this to True if k is odd
    middle = True
    if (k%2 == 0):
        middle = False
    i = k
    while (i < n):
        #find median in k_sorted
        median = kMedian(k_sorted, k, middle)
        if (nums[i] >= 2*median):
            n_notification = n_notification + 1
        #now remove the i-k element 
        # k_sorted.remove(nums[i-k])
        idx = search(k_sorted, k, nums[i-k])
        k_sorted.pop(idx)
        
        #insert ith element to k_sorted
        idx = insertionPoint(k_sorted, k-1, nums[i])
        k_sorted.insert(idx, nums[i])
        i = i + 1
    
    print n_notification