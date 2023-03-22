#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   二叉搜索树的最小绝对差.py
@Time    :   2023/03/22 16:44:41
@Author  :   gaochangju 
@Version :   1.0
'''
""" 
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

bst 是有序的，所有不用每个元素两两组合

中序遍历的
"""

# here put the import lib




from . import TreeNode
class Solution:
    def getMinimumDifference_recursion(self, root: TreeNode) -> TreeNode:
        # 使用中序遍历

        min_value = float("INF")
        pre = None
        # 定义递归函数

        def _inorder_(node):
            nonlocal min_value
            if not node:
                return
            _inorder_(node.left)
            if pre:
                min_value = min(min_value, abs(node.value-pre.value))
            pre = node  # 使用pre 记录前一个节点（对下一次递归体来说，当前记录的就是下次的前一个节点）
            _inorder_(node.right)
        _inorder_(root)
        # 返回结果
        return min_value

    def getMinimumDifference_iteration(self, root: TreeNode) -> TreeNode:
        # 中序遍历的迭代写法
        if not root:
            return
        stack = []
        cur = root
        pre = None
        min_value = float("INF")
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre:
                    min_value = min(min_value,abs(cur.value - pre.value))
                pre = cur  # 保存上一个节点
                cur.right
        return min_value
