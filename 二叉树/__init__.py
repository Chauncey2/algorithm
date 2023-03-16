#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   common.py
@Time    :   2023/03/16 11:16:28
@Author  :   gaochangju 
@Version :   1.0
'''
""" 
二叉树的构造和一般通用函数定义
"""


class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """构造二叉树的函数"""

    def __init__(self, nodes: list[TreeNode]) -> None:
        self.root = None
        self.nums = 0  # 记录二叉树中节点个数
        self.heigh = 0  # 记录二叉树层高

    def preorder_traversal(root: TreeNode) -> list:
        """二叉树前序遍历递归写法

        Args:
            root (TreeNode): 二叉树根节点

        Returns:
            list: 前序遍历结果
        """
        result = []

        def traversal(cur: TreeNode):
            if cur == None:
                return
            # 前序遍历的顺序：中左右
            result.append(cur.value)
            traversal(cur.left)
            traversal(cur.right)

        return result
    def inorder_traversal(root: TreeNode) -> list:
        """二叉树的中序遍历递归写法

        Args:
            root (TreeNode): 二叉树根节点

        Returns:
            list: 中序遍历结果
        """
        result = []

        def traversal(cur: TreeNode):
            if cur == None:
                return
            # 前序遍历的顺序：左中右
            traversal(cur.left)
            result.append(cur.value)
            traversal(cur.right)

        return result
    def postorder_traversal(root: TreeNode) -> list:
        """二叉树的后序遍历递归写法

        Args:
            root (TreeNode): 根节点

        Returns:
            list: 后序遍历结果
        """
        result = []

        def traversal(cur: TreeNode):
            if cur == None:
                return
            # 前序遍历的顺序：左中右
            traversal(cur.left)
            traversal(cur.right)
            result.append(cur.value)

        return result

