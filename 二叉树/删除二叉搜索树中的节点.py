#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   删除二叉搜索树中的节点.py
@Time    :   2023/03/23 16:56:51
@Author  :   gaochangju 
@Version :   1.0
'''
""" 
给定一个二叉搜索树的根节点 root 和一个值 key，
删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。
返回二叉搜索树（有可能被更新）的根节点的引用。


"""

# here put the import lib
from . import TreeNode

class Solution:
    def delete_node_recursion(self,root:TreeNode,k:int)->TreeNode:
        if not root :
            return root
        # 如果节点值小于k，则遍历右子树
        if root.value < k:
            root.right = self.delete_node(root.right,k)
        # 入股节点值大学k，则遍历左子树
        elif root.value > k:
            root.left = self.delete_node(root.left,k)
        # 找到需要删除的值
        else:
            # 第一种情况：是叶子节点，直接删除
            if not root.left and not root.right:
                return None
            # 第二种情况：左子树为空，右子树不空，用右子树替换节点
            if not root.left and root.right:
                return root.right
            # 第三种情况：左子树不空，右子树为空，用左子树替换节点
            if root.left and not root.right:
                return root.left
            # 左右子树都不空，则找到右子树最左侧的节点 (1)，
            # 将待删除的节点记挂在最左侧上(2)
            # 并使用右节点替换当前节点(3)
            
            node = root.right
            # (1)
            while node.left:
                node = node.left
            # (2)
            node.left = root.left
            # (3)
            root = root.right
        
        return root
    
    def delete_node_iteration(self,root:TreeNode,k:int)->TreeNode:
        """使用迭代法删除bst中的节点
        迭代法的步骤分为两步骤:第一步，将左子树和右子树连接，第二步，将右子树和父节点连接起来
        Args:
            root (TreeNode): bst根节点
            k (int): 待删除的节点值

        Returns:
            TreeNode: 删除后的根节点
        """
        if not root:
            return root
        p = root
        last = None  # last 节点是用来保存待删除节点的父节点
        while p:
            if p.value == k:
                if p.right:
                    if p.left: # 左右子树都不为空
                        node = p.right
                        while node.left:
                            node = node.left
                        node.left = p.left 
                    right = p.right
                else:
                    right = p.left
                
                if last is None:
                    last = right # 删除的节点是原bst的根节点
                elif last.value >k:
                    last.left = right
                elif last.value <k:
                    last.right = right
                # 节点删除已经连接，返回
                break
            else:
                last = p
                if p.value > k:
                    p = p.left
                else:
                    p = p.right
        
        return root
        
            
    