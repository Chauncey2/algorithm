#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   合并二叉树.py
@Time    :   2023/03/22 10:04:18
@Author  :   gaochangju 
@Version :   1.0
'''

""" 
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，
两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，
那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

注意： 
树相关的题目遍历是基础，几乎所有题目的解题方式都离不开遍历
"""

# here put the import lib
from typing import List
from . import TreeNode

class Solution:
    """使用迭代法也是建立在遍历的基础上"""
    
    def merge_binary_tree(self,root1:TreeNode,root2:TreeNode)->TreeNode:
        """合并两个二叉树

        Args:
            root1 (TreeNode): 树1根节点
            root2 (TreeNode): 数2根节点

        Returns:
            TreeNode: 合并后根节点
        """
        # 终止条件 保证进入单层循环的两根都非空
        if not root1:
            return root2
        if not root2:
            return root1
        # 确定单层循环逻辑
        root1.value+=root2.value
        root1.left = self.merge_binary_tree(root1.left,root2.left)
        root1.right = self.merge_binary_tree(root1.right,root2.right)
        # 返回值
        return root1
