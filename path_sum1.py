# 112. Path Sum
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def lol(arr,sum1,current):
            nonlocal piyu
            arr.append(current.val)
            if sum(arr)==sum1 and current.left==None and current.right==None:
                piyu=True
                return
            if current.left!=None:
                lol(list(arr),sum1,current.left)
            if current.right!=None:
                lol(list(arr),sum1,current.right)      
        piyu=False
        p=root
        if p!=None:
            n=lol([],targetSum,p)
        return piyu