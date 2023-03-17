#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   对称二叉树.py
@Time    :   2023/03/17 10:25:39
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
from . import BinaryTree
from . import TreeNode
from collections import deque

""" 
给定一个二叉树，检查它是否是镜像对称的

"""


class Solution:

    def is_symmetric_recursion(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.compare(root.left, root.right)

    def compare(self, left: TreeNode, right: TreeNode) -> bool:
        # 排除节点为空的情况
        if left is None and right is not None:
            return False
        elif left is not None and right is None:
            return False
        elif left is None and right is None:
            return True
        # 排除数值不相同的节点
        elif left.value != right.value:
            return False

        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        # 左右子树逻辑处理
        is_same = outside and inside

        return is_same

    def is_symmetric_itersion(self, root: TreeNode):
        # 迭代法，使用队列按照层序遍历进行操作
        if root is None:
            return True
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)

        while len(queue):
            left_node = queue.popleft()
            right_node = queue.popleft()
            # 左右节点为空，则表示对称
            if not left_node and not right_node:
                continue
            # 排除不对称的情况
            if not left_node or not right_node or left_node.value != right_node.value:
                return False
            # outside
            queue.append(left_node.left)
            queue.append(right_node.right)
            # inside
            queue.append(left_node.right)
            queue.append(right_node.left)
        return True

    def is_symmetric_leveOrder(self, root: TreeNode) -> bool:
        # 层序遍历比较树是否wield堆成
        if not root:
            return True
        queue = []
        queue.append(root)

        while len(queue):
            # 获取当前层的节点个数
            this_level_length = len(queue)
            for i in range(this_level_length//2):
                # 两个节点一个是None ，一个不是None
                if (not queue[i] and queue[this_level_length-i-1]) or \
                        (queue[i] and not queue[this_level_length-i-1]):
                    return False
                # 两个节点都不为None
                if queue[i] and queue[i].value != queue[this_level_length-i-1].value:
                    return False
            # 下一层进队
            for i in range(this_level_length):
                if not queue[i]:
                    continue

                queue.append(queue[i].left)
                queue.append(queue[i].right)
            # 让下一层节点进入循环
            queue = queue[this_level_length:]
        return True

    def is_symmetric_by_stack(self, root: TreeNode) -> bool:
        # 使用栈判断（模拟递归进行实现）
        if root is None:
            return True

        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while len(stack):
            right_node = stack.pop()
            left_node = stack.pop()
            # 如果左右节点为空则表示对称
            if not right_node and not left_node:
                continue

            if not left_node or not right_node or left_node.value != right_node.value:
                return False

            # outside
            stack.append(left_node.left)
            stack.append(right_node.right)
            # inside
            stack.append(left_node.right)
            stack.append(right_node.left)

        return True
