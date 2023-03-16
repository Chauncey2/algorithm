#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   翻转二叉树.py
@Time    :   2023/03/16 22:06:19
@Author  :   gaochangju
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
from . import BinaryTree
from . import TreeNode


class Solution:
    def invert_preorder(self, root: TreeNode) -> TreeNode:

        if root is None:
            return None

        stack = []
        stack.append(root)

        while len(stack):
            node = stack.pop()
            # 交换子节点左右位置
            node.left, node.right = node.right, node.left
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root

    def invert_inorder_recursion(self, root: TreeNode) -> TreeNode:
        """使用中序遍历翻转二叉树非常不方便，因为中间左右子树会被
        翻转两遍，但是可以通过魔改，达到翻转的目的，但是严格来说，也就不是
        中序遍历了"""
        if root is None: return root

        if root.left:
            self.invert_inorder_recursion(root.left)
        root.left, root.right = root.right, root.left
        # 因为上一步已经讲叶子节点翻转过了，所以这一步还是翻转左子树（原右子树）
        if root.left:
            self.invert_inorder_recursion(root.left)

    def invert_postorder(self, root: TreeNode) -> TreeNode:
        # 这里使用后续遍历的统一迭代法
        # 统一迭代法的关键就在需要添加一个空指针作为是否操作的标志
        if root is None:
            return root
        stack = []
        stack.append(root)
        while len(stack):
            node = stack.pop()
            if node is not None:
                stack.append(node)
                stack.append(None) # 添加标记
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            else:
                stack.pop()
                node= stack.pop()
                node.left,node.right = node.right, node.left
        return root

    '''前序和后序递归遍历方法 省略'''

    def invert_level_order(self,root:TreeNode)->TreeNode:
        if root is None:
            return root
        from collections import deque
        queue = deque()
        queue.append(root)
        while len(queue):
            node = queue.popleft()
            node.left,node.right = node.right,node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)









