#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 16:35:04 2016

@author: jyon
"""

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ele_indicies = {}
        self.my_list = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        #print 'Hi'
        self.my_list.append(val)
        idx = len(my_list) - 1
        if (val not in self.ele_indicies.keys()):
            #add a new key to the dict
            self.ele_indicies[val] = [idx]
            return True
        else:
            self.ele_indicies[val].append(idx)
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if (val in self.ele_indicies.keys()):
            #remove 
            # if count > 1, them decrement count 
            idx = self.ele_indicies[val].pop()
            self.my_list.pop(idx)
            if (len(self.ele_indicies[val]) == 0):
                
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        for v in self.my_dict.keys():
            if (self.my_dict[v][1] > 0):
                self.my_dict[v][1] = self.my_dict[v][1] - 1
                return v
        for v in self.my_dict.keys():
            self.my_dict[v][1] = self.my_dict[v][0]
        v = self.my_dict.keys()[0]
        self.my_dict[v][1] = self.my_dict[v][1] - 1
        return v

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()