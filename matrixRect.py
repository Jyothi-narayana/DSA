#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 18:56:34 2016

@author: jyon
"""

class Solution(object):
    def one_trails(self, A):
        rows = len(A)
        columns = len(A[0])
        trails = {}
        for i in range(0,rows):
            a_row = A[i]
            trail = []
            curr_idx = -1
            for idx, j in enumerate(a_row):
                #print idx, j
                #print j
                if (j == '1' and idx > curr_idx):
                    curr_idx = idx
                    #print 'Yes'
                    while (curr_idx < len(a_row) and a_row[curr_idx] == '1'):
                        #print 'Yes'
                        curr_idx = curr_idx + 1
                    trail.append((idx, curr_idx))
            trails[i] = trail
        print trails
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        self.one_trails(matrix)
        return 0
        