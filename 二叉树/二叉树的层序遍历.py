#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   二叉树的层序遍历.py
@Time    :   2023/03/16 18:13:40
@Author  :   gaochangju 
@Version :   1.0
'''
from typing import List # 参数注解
from . import BinaryTree
from . import TreeNode


class BinaryTreelevleOrder(BinaryTree):
    def __init__(self, nodes:List[TreeNode]) -> None:
        super().__init__(nodes)

    def level_order(self, root: TreeNode) -> list:
        if root is None:
            return []

        queue = []
        queue.append(root)
        result = []
        while queue:
            node = queue.pop(0)  # 出队首元素
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
