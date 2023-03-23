#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   二叉搜索树的最近公共祖先.py
@Time    :   2023/03/23 11:33:12
@Author  :   gaochangju 
@Version :   1.0
'''
""" 
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先

关键词
bst 有序 最近公共子节点

因为不涉及节点的操作，所以不需要对
"""

# here put the import lib
from . import TreeNode

class Solution:
    def lowestCommonAncestor(self,root:TreeNode,p:TreeNode,q:TreeNode)->TreeNode:
        # 搜索左子树
        if root.value > p.value and root.value >q.value:
            return self.lowestCommonAncestor(root.left,p,q)
        # 搜索右子树
        if root.value < p.value and root.value < q.value:
            return self.lowestCommonAncestor(root.right,p,q)
        # root 在区间[p,q]内
        return root
    
    def lowestCommonAncestor_iteration(self,root:TreeNode,p:TreeNode,q:TreeNode)->TreeNode:
        # 迭代法遍历
        while True:
            if root.value> p.value and root.value>q.value:
                root = root.left
            elif root.value <p.value and root.value <q.value:
                root = root.right
            else:
                return root
            
            