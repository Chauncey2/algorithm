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
from typing import List

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """构造二叉树的函数"""

    def __init__(self, nodes: List[TreeNode]) -> None:
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

    def preorder_traversal_iteration(root: TreeNode) -> list:
        """二叉树前序遍历迭代写法

        Args:
            root (TreeNode): 根节点

        Returns:
            list: 遍历结果
        """
        if root is None:
            return []
        stack = []
        stack.append(root)
        result = []
        while len(stack):
            node = stack.pop()  # 当前节点出栈
            result.append(node.value)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
        return result

    def inorder_traversal_iteration(root: TreeNode) -> list:
        """二叉树中序遍历迭代写法
        
        Args:
            root (TreeNode): 根节点

        Returns:
            list: 遍历结果
        """
        #  中序遍历的迭代写法借助了指针，不同于前序的迭代写法，
        # 前序访问节点的顺序和操作节点的顺序是一致的
        if root is None:
            return []
        stack = []
        cur = root
        result = []
        while cur is not None or len(stack):
            # 中序遍历是先找到左末尾叶子节点
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                # 当访问到最左侧叶子节点后，出栈顶元素访问
                cur = stack.pop()
                result.append(cur.value)
                cur = cur.right
        return result

    def postorder_traversal_iteration(root: TreeNode) -> list:
        """二叉树后序遍历迭代写法

        Args:
            root (TreeNode): 根节点

        Returns:
            list: 结果列表
        """
        if root is None:
            return []

        stack = []
        stack.append(root)
        result = []
        while len(stack):
            node = stack.pop()
            result.append(node.value)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]
