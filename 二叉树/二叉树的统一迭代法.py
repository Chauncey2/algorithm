#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   二叉树的统一迭代法.py
@Time    :   2023/03/16 16:37:09
@Author  :   gaochangju 
@Version :   1.0
'''

# 二叉树的前中后序遍历的迭代写法，代码风格不统一，
# 即 前序和后序的代码风格同中序遍历的代码风格不同，
# 原因就是，中序遍历迭代写法 ，节点的访问顺序和操作顺序不统一，需要另外借助指针


from typing import List
from . import BinaryTree
from . import TreeNode

class unificationTraversal(BinaryTree):
    """ 统一迭代法使用标记法，将前中后序方法的代码风格保持一致"""
    def __init__(self, nodes: List[TreeNode]) -> None:
        super().__init__(nodes)
    
    def preorder_traversal_iteration(root: TreeNode) -> list:
        result = []
        stack = []
        if not root:
            return []
        stack.append(root)
        while len(stack):
            node = stack.pop()
            if node is not None:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                stack.append(node)
                stack.append(None)  #  放入None指针做标记，标志后一个节点为要读取的节点
            else:
                stack.pop() # None指针出栈
                node = stack.pop()
                result.append(node.value)
        return result

    def inorder_traversal_iteration(root: TreeNode) -> list:
        result = []
        stack = []
        if not root:
            return []
        stack.appen(root)
        while len(stack):
            node = stack.pop()
            if node is not None:
                if node.right:
                    stack.append(node.right)
                # 节点被访问过，但是并没有被处理，所以加上None标记指针
                stack.append(node)
                stack.append(None)
                if node.left:
                    stack.append(node.left)
            else:
                # 遇到标记指针，节点出栈进结果集
                stack.pop()
                node = stack.pop()
                result.append(node.value)
        return result
        
    def postorder_traversal_iteration(root: TreeNode) -> list:
        result = []
        stack = []
        if root is None:
            return []
        stack.append(root)
        while len(stack):
            node = stack.pop()
            if node is not None:
                # node 节点访问过但是没有做操作，添加none指针标记
                stack.append(node)
                stack.append(None)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            else:
                stack.pop()
                node = stack.pop()
                result.append(node.value)
        return result
        
