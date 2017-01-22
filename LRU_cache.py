#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 14:29:06 2016

@author: jyon
"""

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {} # current capacity of the cache: len(self.cache.keys())
        self.queue = [] # most recently used is at the tail of the queue

    def get(self, key):
        """
        :rtype: int
        """
        if (key in self.cache.keys()):
            # update the value in Q
            idx = self.queue.index(key)
            self.queue = self.queue[0:idx] + self.queue[idx+1:len(self.queue)]
            self.queue.insert(len(self.queue), key)
            #print self.queue
            #print self.cache
            return self.cache[key]
        else:
            return -1
            
    def add(self, key, value):
        self.cache[key] = value
        self.queue.insert(len(self.queue), key)
    
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        curr_capacity = len(self.cache.keys())
        # if already in the cache, just update the value and the rank in Queue
        if (key in self.cache.keys()):
            self.cache[key] = value
            idx = self.queue.index(key)
            self.queue = self.queue[0:idx] + self.queue[idx+1:len(self.queue)]
            self.queue.insert(len(self.queue), key)
        elif (curr_capacity < self.capacity):
            #There is still space, just add to the cache and the Q
            self.add(key, value)
        else:
            #remove from Q and cache and then add to Q and cache
            #remove head of Q 
            remove_key = self.queue[0]
            self.queue = self.queue[1:len(self.queue)]
            self.cache.pop(remove_key)
            #add key and value to Q and hashtable
            self.add(key, value)