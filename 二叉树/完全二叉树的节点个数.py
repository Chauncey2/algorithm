#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   完全二叉树的节点个数.py
@Time    :   2023/03/18 14:31:15
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
from . import TreeNode

""" 
给出一个完全二叉树，计算该完全二叉树的节点个数
计算完全二叉树的节点个数可以根据二叉树的性质去做处理
题目又分为计算普通二叉树和完全二叉树
"""


class Solution:
    # 使用递归方法实现
    def get_tree_num_recursion(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_node_number = self.get_tree_num_recursion(root.left)
        right_node_number = self.get_tree_num_recursion(root.right)
        return left_node_number + right_node_number + 1

    def get_num(self, root: TreeNode) -> int:
        return self.get_tree_num_recursion(root)

    def get_node_num_levelorder(self, root: TreeNode) -> int:
        # 迭代法，其实迭代法不管是使用那种遍历方法，只要每访问一个节点，就记录一次也可以完成
        if not root:
            return 0
        from collections import deque
        que = deque()
        que.append(root)
        result = 0
        while len(que):
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                result += 1
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return result

    # 完全二叉树独有的方法，使用公式进行计算 2^n -1
    def countNodes(self, root: TreeNode) -> int:
        # 终止条件
        if not root:
            return 0
        left_node = root.left
        right_node = root.right
        left_depth = 0
        right_depth = 0
        while left_node:
            left_node = left_node.left
            left_depth += 1
        while right_depth:
            right_node = right_node.right
            right_depth += 1
        if left_depth == right_depth:
            # 如果不使用位运算，则 左右子树的初始值应设为1
            # 2<< 0 相当于 2^1
            return (2 << left_depth) - 1
        # 如果此层递归的子树不是完全二叉树
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
