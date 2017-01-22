#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 12:50:06 2016

@author: jyon
"""

class Solution(object):
    def move(self, nums, idx):
        e = nums[idx]
        r_idx = idx + e
        n_nums = len(nums)
        if (r_idx >= 0 and r_idx <= (n_nums - 1)):
            return r_idx
        if (r_idx > (n_nums - 1)):
            while (r_idx > (n_nums - 1)):
                r_idx = r_idx - n_nums
        else:
            while (r_idx < 0):
                r_idx = r_idx + n_nums
        return r_idx
        
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        has_loop = False
        elements_to_visit = list(range(0,len(nums)))
        
        for idx in elements_to_visit:
            #e is the start index
            curr_idx = idx
            visited_idx = []
            same_direction = True
            while(same_direction):
                if (curr_idx in visited_idx):
                    #last element of visited index shouldn't be same as curr
                    l = visited_idx[len(visited_idx) -1]
                    if (len(visited_idx) > 1 and l != curr_idx):
                        #Found cycle
                        return True
                    else:
                        #no cycle possible from this index
                        same_direction = False
                visited_idx.append(curr_idx)
                res_idx = self.move(nums, curr_idx)
                if (nums[res_idx] * nums[curr_idx] < 0):
                    #indicates change in direction 
                    same_direction = False
                curr_idx = res_idx
            #remove visited index from elements_to_visit
            elements_to_visit = [x for x in elements_to_visit if x not in visited_idx]
        return has_loop
        