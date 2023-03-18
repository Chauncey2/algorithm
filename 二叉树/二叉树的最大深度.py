#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   二叉树的最大深度.py
@Time    :   2023/03/17 23:12:44
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
from collections import deque
from . import TreeNode
from . import BinaryTree

""" 
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例： 给定二叉树 [3,9,20,null,null,15,7]
"""


class Solution:
    def get_depth_recursion(self, root: TreeNode) -> int:
        """ 获取二叉树的最大深度（拓展：如果能够适配n叉树应该如何调整？）
        """
        # 定义边界条件
        if not root:
            return 0
        # 定义递归体
        left_depth = self.get_depth_recursion(root.left)
        right_depth = self.get_depth_recursion(root.right)
        depth = 1 + max(left_depth, right_depth)
        # 返回值
        return depth

    def get_depth_recursion_mini(self, root: TreeNode) -> int:
        # 递归函数的精简写法
        if not root:
            return 0
        return 1+max(self.get_depth_recursion_mini(root.left), self.get_depth_recursion_mini(root.right))

    def get_depth_preorder(self, root: TreeNode) -> TreeNode:
        """ 使用前序遍历的递归写法获取二叉树的最大深度
        使用到了回溯的思想，所谓回溯就是记录上一次的结果，如果本次结果不对就进行回退
        """
        result = 0

        def get_depth(node, depth):
            result = max(result, depth)
            if not node.left and not node.right:
                return
            if node.left:
                depth += 1
                get_depth(node.left, depth)
                depth -= 1
            if node.right:
                depth += 1
                get_depth(node.right, depth)
                depth -= 1
            return

        # 如果root非空，则使用递归寻找二叉树的最大深度
        if root:
            get_depth(root, 0)

        return result

    def get_depth_iterasion(self, root: TreeNode) -> int:
        """ 使用非迭代法获取二叉树的最大深度
        能想到的就是使用层序遍历
        """
        if not root:
            return 0
        depth = 1
        queue = deque()
        queue.append(root)
        while len(queue):
            size = len(queue)
            # 迭代法就是使用层序遍历，没遍历一层，二叉树的深度+1
            depth += 1
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
