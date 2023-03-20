#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   从中序序列和后序序列构造二叉树.py
@Time    :   2023/03/20 17:44:32
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
from typing import List
from . import TreeNode
from . import BinaryTree


class Solution:
    def build_tree_by_ip(self, inorders: List[int], preorders: List[int]) -> TreeNode:
        """使用中序序列和后续序列构建二叉树

        Args:
            inorders (List[int]): 中序序列
            preorders (List[int]): 后序序列

        Returns:
            TreeNode: 根节点
        """
        # 如果序列为空则返回空
        if not len(inorders) or not len(preorders):
            return None



if __name__ == "__main__":
    pass
