#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   验证二叉搜索树.py
@Time    :   2023/03/22 15:48:42
@Author  :   gaochangju 
@Version :   1.0
'''

""" 
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
"""

# here put the import lib
from typing import List
from . import TreeNode

class Solution:

    def is_valid_bst_1(self,root:TreeNode)->bool:
        """bst的中序遍历序列有序递增数组
        因此可以将bst转换成有序数组进行判断

        Args:
            root (TreeNode): 树根节点

        Returns:
            bool: 验证结果
        """
        result = []
        # 中序遍历获取中序序列
        def _inorder(node):
            # 终止条件
            if not node:
                return 
            self.is_valid_bst_1(node.left)
            result.append(node.value)
            self.is_valid_bst_1(node.right)
        # 判断数组是否有序
        def _issorted(res):
            if not len(res):
                return False
            min_value = res[0]
            for item in res[1:]:
                if min_value < item:
                    min_value = item
                else:
                    return False
            return True
        
        _inorder(root)
        res = _issorted(result)  
        return res         
            
    def is_valid_bst_2(self,root:TreeNode)->bool:
        """ 
        在递归的过程中，验证是否为bst
        bst 中序遍历序列是一个递增数组，意味着，
        递归遍历每一次操作的节点的value必定是比前一个值要大
        """
        # 定义一个最小值
        max_value = - float("INF")
        
        def _inorder(node):
            nonlocal max_value
            if not root:
                return True
            
            is_left_valid = _inorder(node.left)
            # bst的中序遍历每次的节点一定是比前一个大
            if node.value > max_value:
                max_value = node.value
            else:
                return False
            is_right_valid = _inorder(node.right)

            return is_left_valid and is_right_valid
        
        result = _inorder(root)
        return result
         
            
        