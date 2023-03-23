#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   二叉搜索树的最近公共祖先.py
@Time    :   2023/03/23 09:55:02
@Author  :   gaochangju 
@Version :   1.0
'''

""" 
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

关键词：
二叉树 后续遍历 递归 回溯

"""

# here put the import lib
from . import TreeNode

class Solution:
    def lowestCommonAncestor(self,root:TreeNode,p:TreeNode,q:TreeNode) ->TreeNode:
        if not p or not q or not root:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        # 操作返回的左右分支结果
        
        if not left and not right: # 表示左右分支都没有找到p，q
            return None
        elif not left and right: # 标志在右分找到一个，要向上返回
            return right
        elif left and not right: # 标志在左分支找到一个，向上返回
            return left
        else:  
            # 左右分支找到结果，此时的root就是最近公共祖先
            return root 
    