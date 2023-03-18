#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   二叉树的最小深度.py
@Time    :   2023/03/18 13:41:40
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
from . import TreeNode

"""
最小深度指的是从根节点到最近一个叶子节点的路径上的节点个数
拓展：
二叉树节点的深度，从根节点到该节点的最简单路径边的总数或节点数
二叉树节点的高度，从该节点到叶子节点的最简单路径边的总数或节点数

最小深度 和该节点的高度一致

递归法比较难理解，迭代法比较好理解
"""


class Solution:
    # todo: 获取最小深度的递归法需要仔细研究一下
    def get_min_depth_recursion(self, root: TreeNode, depth: int) -> int:
        # 使用后续遍历
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        min_depth = 10**9 # 定义一个足够大的变量，起到占位符的作用，
        if root.left:
            min_depth = self.get_min_depth_iteration(root.left, min_depth) # 获取左子树的最小深度
        if root.right:
            min_depth = self.get_min_depth_iteration(root.right, min_depth) # 获取右子树的最小深度
        return min_depth + 1

    def get_min_depth_iteration(self, root: TreeNode) -> int:
        # 层序遍历获取最小深度
        if not root:
            return 0
        from collections import deque
        que = deque()
        que.append(root)
        depth = 1
        while len(que):
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            depth += 1
        return depth
