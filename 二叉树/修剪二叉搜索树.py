#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   修剪二叉搜索树.py
@Time    :   2023/03/24 11:30:28
@Author  :   gaochangju 
@Version :   1.0
'''
""" 
给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。
通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。
你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。

迭代法比递归法要好理解很多

"""

# here put the import lib
from . import TreeNode

class Solution:
    
    def trim_bst_recursion(self,root:TreeNode,low:int,high:int)-> TreeNode:
        if not root:
            return root
        
        if root.value < low:
            return self.trim_bst_recursion(root.right,low,high)
        if root.value > high:
            return self.trim_bst_recursion(root.left,low,high)
        
        if root.value >=low and root.value<=high:
            root.left = self.trim_bst_recursion(root.left,low,high)
            root.right = self.trim_bst_recursion(root.right,low,high)
            return root
         
    
    def trim_bst_iteration(self,root:TreeNode,low:int,high:int)->TreeNode:
        # 迭代法更像是一种一边向区间内收缩，一边抛弃节点的过程
        if not root:
            return root
        # 移动根节点，将根节点移动到区间内
        while root and (root.value<low or root.value>high):
            if root.value <low:
                root = root.right
            if root.value >high:
                root = root.left
    
        # 移动左子树 将左子树移动到区间内
        cur = root
        while cur.left and (cur.left.value<low):
            if cur.left.value < low:
                cur.left = cur.right
            cur = cur.left
    
        # 一定右子树，将右子树移动到区间内
        cur = root
        while cur.righ and (cur.right.value >high):
            if cur.right.value > high:
                cur.high = cur.left
            cur = cur.right
            
        return root
        
    