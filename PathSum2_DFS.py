# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:07:03 2020

@author: WELCOME
"""
"""
Path Sum 2
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
    def pathSum(self, root, sum):
        result=[]
        
        
        def helper(root,total,tempList):
            tempList=list(tempList)
            #Base
            if not root:
                return 
            if not root.left and not root.right and total+root.val==sum:
                tempList.append(root.val)
                result.append(tempList)
                return
            helper(root.left,total+root.val,tempList+[root.val])
            helper(root.right,total+root.val,tempList+[root.val])
        helper(root,0,[])
        return result

treeNode=binaryTree(6)
treeNode.left=binaryTree(4)
treeNode.right=binaryTree(8)
treeNode.left.left=binaryTree(1)
print(Solution().pathSum(treeNode,11))