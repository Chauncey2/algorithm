#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   二叉树左叶子之和.py
@Time    :   2023/03/20 12:32:56
@Author  :   gaochangju 
@Version :   1.0
'''

"""计算给定二叉树的所有左叶子之和。"""
# here put the import lib




from . import TreeNode
class Solution:
    def sum_of_left_leaves_recursion(self, root: TreeNode):
        # 递归解法（返回值不一定是整数，也有可能是浮点数）
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        # 通过父节点判断 节点是否为左子叶
        left_leaves_sum = self.sum_of_left_leaves_recursion(root.left)
        right_leaves_sum = self.sum_of_left_leaves_recursion(root.right)

        cur_leaves_value = 0
        # 如果该节点的左节点为叶子节点
        if root.left and not root.left.left and not root.left.right:
            cur_leaves_value = root.left.value

        return cur_leaves_value + left_leaves_sum + right_leaves_sum
    
    def sum_of_left_leaves_iteration(self,root:TreeNode):
        # 使用栈模拟递归方法。同样是使用父节点判断是否为左叶子节点
        if not root:
            return 0 
        
        stack = []
        stack.append(root)
        res = 0
        while len(stack):
            node = stack.pop()
            if node.left and not node.left.left and node.left.right:
                res += node.left.value
            # 认为,这里
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
        return res

            