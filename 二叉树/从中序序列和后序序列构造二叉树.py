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
    def build_tree_by_ip(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """使用中序序列和后续序列构建二叉树

        Args:
            inorders (List[int]): 中序序列
            preorders (List[int]): 后序序列

        Returns:
            TreeNode: 根节点
        """
        # 第一步，特殊情况讨论：树为空，或递归终止条件
        if not len(inorder) or not len(postorder):
            return None
        # 第二步,后序遍历的最后一个节点就是当前的中间节点
        root_value = postorder[-1]
        root = TreeNode(root_value)
        # 第三步，找切割点
        root_index = inorder.index(root_value)
        # 第四步，切割inorder数组，得到inorder数组的左，右半边
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]
        # 第五步，切割 postorder 数组，得到 postorder数组的左，右半边
        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):len(postorder)]
        # 第六步，递归
        root.left = self.build_tree_by_ip(left_inorder, left_postorder)
        root.right = self.build_tree_by_ip(right_inorder, right_postorder)
        # 第七步,返回答案
        return root

    def build_tree_by_pi(self, inorder: List[int], preorder: List[int]) -> TreeNode:
        # 使用前序和中序序列构建二叉树
        # 第一步，边界调价判断
        if not len(inorder) or not len(preorder):
            return None
        # 第二步，从前序序列中获取中间节点，在中序序列中的下标
        root_value = preorder[0]
        root = TreeNode(root_value)
        root_index = inorder.index(root_value)
        # 第三步，切割中序序列为左边序列和右边序列
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]
        # 第四步，切割前序序列为左右序列
        left_preorder = preorder[1:len(left_inorder)+1] # 不要漏掉数组的最后一个
        right_preorder = preorder[len(left_inorder)+1:]
        # 第五步，递归
        root.left = self.build_tree_by_pi(left_inorder,right_preorder)
        root.right = self.build_tree_by_pi(right_inorder,right_preorder)
        # 第六步，返回结果
        return root


if __name__ == "__main__":
    inorder = [4, 2, 5, 1, 6, 3, 7]
    postorder = [4, 5, 2, 6, 7, 3, 1]
    root = Solution().build_tree_by_ip(inorder, postorder)
    # 验证
    result = BinaryTree().inorder_traversal(root)
    print(result)
