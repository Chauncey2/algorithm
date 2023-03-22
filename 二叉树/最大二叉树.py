#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   最大二叉树.py
@Time    :   2023/03/21 17:55:53
@Author  :   gaochangju 
@Version :   1.0
'''

""" 
给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：

二叉树的根是数组中的最大元素。
左子树是通过数组中最大值左边部分构造出的最大二叉树。
右子树是通过数组中最大值右边部分构造出的最大二叉树。
通过给定的数组构建最大二叉树，并且输 出这个树的根节点。
"""
# here put the import lib
from typing import List
from . import TreeNode

class Solution:
    def constructMaximumBinaryTree(self,nums:List[int])-> TreeNode:
        """ 使用递归构造最大二叉树

        Args:
            nums (List[int]): 数组

        Returns:
            TreeNode: 根节点
        """
        # 如果数组为空则返回空节点
        if len(nums):
            return None

        # 找到当前数组中的最大值并切割
        max_value = max(nums)
        root = TreeNode(max_value)
        max_index = nums.index(max_value)
        # 切割
        left_nums = nums[:max_index]
        right_nums = nums[max_index+1:]
        
        # 递归
        root.left = self.constructMaximumBinaryTree(left_nums)
        root.right = self.constructMaximumBinaryTree(right_nums)
        # 返回值
        return root
        
        