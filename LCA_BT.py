#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 13:12:52 2016

@author: jyon
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # returns a path from the root to a node if the node exists
    def path(self, root, node):
        if (root == None):
            return []
        #print root.val
        if (root.val == node.val and root.left == node.left and root.right == node.right):
            #print 'I am here'
            return [root.val]
        left_path = self.path(root.left, node)
        right_path = self.path(root.right, node)
        #print left_path
        #print right_path
        path = []
        if (left_path and len(left_path) > 0):
            left_path.insert(0, root.val)
            path = left_path
        elif (right_path and len(right_path) > 0):
            right_path.insert(0, root.val)
            path = right_path
        #print path
        return path
                
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #print p.val
        #print root.val
        p_path = self.path(root, p)
        q_path = self.path(root, q)
        print p.val
        print q.val
        print p_path
        print q_path
        idx = -1
        shorter = len(p_path) if (len(p_path) < len(q_path)) else len(q_path)
        #print shorter
        while ((idx+1) < shorter and p_path[idx + 1] == q_path[idx + 1]):
            idx = idx + 1
        #print idx
        #print root.val
        return p_path[idx]
        #return 1