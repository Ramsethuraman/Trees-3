# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:07:03 2020

@author: WELCOME
"""
"""
Symmetric Tree
DFS
Working on Leetcode
Time complexity= O(N)
Space Complexity = O(H) 
"""

class binaryTree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        
        def helper(left,right):
            #Base
            if not left and not right:
                return True
            if not left or not right or left.val!=right.val:
                return False
            case1=helper(left.left,right.right)
            case2=helper(left.right,right.left)
            return case1 and case2
        return helper(root.left,root.right)

treeNode=binaryTree(6)
treeNode.left=binaryTree(4)
treeNode.right=binaryTree(8)
treeNode.left.left=binaryTree(1)
print(Solution().isSymmetric(treeNode))