#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   有序数组转换为BST.py
@Time    :   2023/03/24 13:23:39
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
from typing import List
from . import TreeNode


class Solution:
    """使用递归创建BST"""

    def build_bst(self, nums: List[int]) -> TreeNode:
        if not len(nums):
            return None
        root = self.traversal(nums, left=0, right=len(nums)-1)
        return root

    def traversal(self, nums: List[int], left, right) -> TreeNode:
        if left > right:
            return
        mid = left + (right - left)//2  # 防止 left 和 right 数据类型过大导致的int数据类型越界
        # 创建节点
        node = TreeNode(nums[mid])
        node.left = self.traversal(nums, left, min-1)
        node.right = self.traversal(nums, mid+1, right)
        return node

    def build_bst_iteration(self, nums: List[int]) -> TreeNode:
        """ 使用左闭右闭的方法进行处理 """
        if not len(nums):
            return None
        # 初始化根节点
        root = TreeNode()
        node_stack = [root]
        left_stack = [0]
        right_stack = [len(nums)-1] # 原方法中，放入的是 len(nums) 

        while node_stack:
            node = node_stack.pop()
            left = left_stack.pop()
            right = right_stack.pop()
            mid = left + (right - left)//2
            node.value = nums[mid]

            if left < mid:
                node.left = TreeNode()
                node_stack.append(node.left)
                left_stack.append(left)
                right_stack.append(mid-1) # 原方法中放入的是 mid
            if right > mid:
                node.right = TreeNode()
                node_stack.append(node.right)
                left_stack.append(mid+1)
                right_stack.append(right)
        return node
