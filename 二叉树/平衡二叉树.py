#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   平衡二叉树.py
@Time    :   2023/03/18 15:12:55
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
from . import TreeNode

""" 
平很二叉树：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1
注意： 空树也算是一个平衡二叉树
"""


class Solution:
    def is_balance(self, root: TreeNode) -> bool:
        
        if self.get_hight(root)!=-1:
            return True
        else:
            return False
        

    def get_hight(self, root: TreeNode) -> int:
        # 返回当前节点的高度
        if not root:
            return 0
        # 海象表达式是python3.8引入的新语法
        if (left_higt := self.get_hight(root.left)) == -1:
            return -1
        if (right_high := self.get_hight(root.right)) == -1:
            return -1
        #  如果子树不是一个平衡二叉树，则返回 -1 
        if abs(left_higt-right_high) > 1:
            return -1
        
        return 1 + max(left_higt,right_high)

""" 
迭代法：
二叉树的深度使用前序遍历（先序遍历）
二叉树的高度使用后续遍历
原因在于 二叉树的深度和高度的定义是不同的
"""