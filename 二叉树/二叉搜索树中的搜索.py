#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   二叉搜索树中的搜索.py
@Time    :   2023/03/22 15:27:09
@Author  :   gaochangju 
@Version :   1.0
'''

""" 
题设：
    给定二叉搜索树（BST）的根节点和一个值。 
    你需要在BST中找到节点值等于给定值的节点。 
    返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

二叉搜索树(BST)
bst是一个这样的二叉树，
若左子树不为空，则左子树的所有节点的值均小于根节点
若右子树不空，则右子树中的所有节点的值均大于根节点的值
左右子树又分别是一颗BST


"""

# here put the import lib
from typing import List
from . import TreeNode

class Solution:
    def search_bst(self,root:TreeNode,value:int)->TreeNode:
        """
        使用递归法在bst中搜索索需要的值
        Args:
            root (TreeNode): bst根节点
            value (int)：目标值

        Returns:
            TreeNode: 子树
        """
        if not root or root.value == value :
            return root
        
        if root.value > value:
            result = self.search_bst(root.left,value)
        if root.value < value:
            result = self.search_bst(root.right,value)
        
        return result
    def search_bst_iteration(self,root:TreeNode,value:int)->TreeNode:
        """使用迭代法搜索bst

        Args:
            root (TreeNode): bst根节点
            value (int): 目标值

        Returns:
            TreeNode: 子树根节点
        """
        # 因为二叉搜索树的性质（有序），所以遍历bst要比遍历普通二叉树简单很多（不需要回溯）
        while root is not None:
            if root.value > value:
                root = root.left
            elif root.value < value:
                root = root.right
            else:
                return root
        
        return None
        