#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   二叉搜索树转换成累加树.py
@Time    :   2023/03/24 16:46:54
@Author  :   gaochangju 
@Version :   1.0
'''
 
"""
给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），
使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
提醒一下，二叉搜索树满足下列约束条件
节点的左子树仅包含键 小于 节点键的节点。 节点的右子树仅包含键 大于 节点键的节点。 左右子树也必须是二叉搜索树。

对于bst而言 累加树的本质其实就是倒序相加
"""

# here put the import lib
from . import TreeNode

class Solution:
    def __init__(self) -> None:
        self._count = 0
    
    def convert_bst(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.convert_bst(root.right)
        self._count += root.val
        root.val = self._count
        self.convert_bst(root.left)
    
        return root

    