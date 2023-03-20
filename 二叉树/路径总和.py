#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   l路径总和.py
@Time    :   2023/03/20 16:38:12
@Author  :   gaochangju 
@Version :   1.0
'''
""" 
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，
这条路径上所有节点值相加等于目标和。

题设要求的是判断是否存在这样一条路径，拓展部分可以讲该路径返回

"""

# here put the import lib




from collections import deque
from . import TreeNode
class Solution:

    def has_path_sum(self, root: TreeNode, target_number: int) -> bool:
        if not root:
            return False
        is_exit = self.traversal(root,target_number-root.value) # 进入递归要将根节点的值减去
        return is_exit

    def traversal(self, node: TreeNode, count: int) -> int:
        
        # 如果是叶子节点且计数为0
        if not node.left and not node.right and count == 0:
            return True
        # 如果叶子节点且计数不为0
        if not node.left and not node.right:
            return False
        
        if node.left:
            count -= node.left.value
            self.traversal(node.left,count)
            count += node.left.value # 回溯 
        if node.right:
            count -= node.right
            self.traversal(node.right,count)
            count += node.right # 回溯

    # 错误处理
    """
    def has_path_sum_levelOrder(self,root:TreeNode,target_number:int)->bool:
        if not root:
            return False
        que = deque()
        que.append(root)
        count = target_number
        while len(que):
            size  = len(que)
            for _ in range(size):
                node = que.popleft()
                count -= node.value # 不能这样处理，这样处理的话，count就是一个全局变量了
                # 如果当前节点是叶子节点
                if not node.left and not node.right and count ==0 :
                    return True
        
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return False
        """ 
    def has_path_sum_by_stack(self,root:TreeNode,target_number:int)->bool:
        if not root:
            return False
        stack = []
        stack.append((root,root.value))
        while stack:
            node,path_sum = stack.pop()
            # 如果是叶子节点且 路径和同target_number相同
            if not node.left and not node.right and path_sum == target_number:
                return True
            # 因为是层序遍历，其实从左边开始还是从右边开始都可以，但是为了保持统一的编码风格，这里使用前序遍历的方法
            if node.right:
                stack.append(node.right,path_sum+node.right.value)
            if node.left:
                stack.append(node.left,path_sum+node.left.value)
            
        return False
                