#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   二叉搜索树中的插入操作.py
@Time    :   2023/03/23 13:38:05
@Author  :   gaochangju 
@Version :   1.0
'''

""" 
给定二叉搜索树(BST)的根节点和要插入树中的值，
将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。
输入数据保证，新值和原始二叉搜索树中的任意节点值都不同

bst原本就是有序的

"""

# here put the import lib
from . import TreeNode

class Solution:
    
    def main(self,root:TreeNode,value:int)->TreeNode:
        bst_root = self.insert_into_bst(root,value)
        return bst_root
    
    def insert_into_bst(self,root:TreeNode,value:int)->TreeNode:
        """向二叉搜索树中插入元素值

        Args:
            root (TreeNode): bst的根节点
            value (int): 插入值

        Returns:
            TreeNode: 根节点
        """
        # 终止条件
        if not root:
            node = TreeNode(value)
            return node
        
        if root.value > value :
            # 用left接住返回值，这个返回值就是终止条件创建的插入节点
            root.left = self.insert_into_bst(root.left,value) 
        if root.value< value:
            root.right = self.insert_into_bst(root.right,value)
        
        return root

    def insert_into_bst_inner(self,root:TreeNode,value:int)->TreeNode:
        if not root:
            return TreeNode(value)

        parent = None
        def _traversal(cur,value):
            nonlocal parent
            if not cur:
                node = TreeNode(value)
                if parent.value < value:
                    parent.right = node
                else:
                    parent.left = node
                return 
            parent = cur
            if cur.valuet < value:
                _traversal(cur.left)
            if cur.val > value:
                _traversal(cur.right)
            return 
        _traversal(root,value)
        return root
