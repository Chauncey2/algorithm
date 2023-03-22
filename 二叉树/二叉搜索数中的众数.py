#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   二叉搜索数中的重数.py
@Time    :   2023/03/22 21:29:51
@Author  :   gaochangju
@Version :   1.0
@Desc    :   None
'''
"""
给定一个有相同值的二叉搜索树(BST)找出BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
"""
# here put the import lib
from typing import List
from . import TreeNode

class Solution:

    def __init__(self) -> None:
        self._count = 0 # 统计节点出现的频率
        self._max_count = 0
        self.pre = TreeNode()
        self.result = []

    def find_mode(self,root:TreeNode)->List[int]:
        if not root:
            return []
        self.search_BST(root)
        return self.result
        

    def search_BST(self,root:TreeNode):
        """使用中序遍历递归的方法遍历每一个节点"""
        if not root:
            return 
        # 左子树递归
        self.search_BST(root.left)
        # 中序遍历处理逻辑
        if not self.pre:
            self._count =1
        elif self.pre.value == root.value:
            self._count +=1
        else:
            self._count =1
        self.pre = root
        
        if self._count == self._max_count:
            self.result.append(root.value)
        
        if self._count > self._max_count:
            self._max_count = self._count
            self.result = [root.value]
        # 右子树递归
        self.search_BST(root.right)
     
