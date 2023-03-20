#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   二叉树的所有路径.py
@Time    :   2023/03/18 16:04:10
@Author  :   gaochangju 
@Version :   1.0
'''

""" 
给定一个二叉树，返回二叉树中所有根节点到叶子节点的路径
"""

# here put the import lib




from typing import List
from collections import deque
from . import TreeNode
class Solution:
    """ 
    不管是迭代法还是，递归法，这一题都使用到了回溯的思想
    """
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        "使用先序遍历获取路径"
        path = ""
        result = []
        if not root:
            return result
        self.traversal_recursion(root, path, result)
        return result

    def traversal_recursion(self, root: TreeNode, path: str, result: List[str]):
        path += str(root.value)
        # 如果是叶子节点则直接返回结果
        if not root.left and not root.right:
            result.append(path)
        if not root.left:
            self.traversal_recursion(root.left, path+"->", result)

        if not root.right:
            self.traversal_recursion(root.right, path+"->", result)

    def traversal_by_stack(self,root:TreeNode)->List[str]:
        #  使用栈模拟二叉树的前序遍历
        if not root:
            return []
        path = ""
        result = []
        stack = []
        stack.append(root)
        path_st = []
        path_st.append(str(root.value))
        while len(stack):
            node = stack.pop()
            path = path_st.pop()
            if not node.left and not node.right:
                result.append(path)
            if node.right:
                stack.append(node.right)
                path_st.append(path+"->"+node.right.value)
            if node.left:
                stack.append(node.left)
                path_st.append(path+'->'+node.left.value)
        return result
            