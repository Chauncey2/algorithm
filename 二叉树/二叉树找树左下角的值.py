#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   二叉树找树左下角的值.py
@Time    :   2023/03/20 15:50:32
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
from collections import deque
from . import TreeNode

class Solution:
    
    def find_bottom_left_leaves_recursion(self,root:TreeNode)->int:
        # 使用递归
        
        max_depth = float("INF") # 定义一个最小值
        left_leaves_value  = 0 
        
        def travesal(node,cur_depth):
            nonlocal max_depth,left_leaves_value  # 使用nonlocal关键字在局部函数中引用外部变量
            # 如果当前节点是叶子节点
            if not node.left and not node.right:
                if cur_depth > max_depth:
                    left_leaves_value = node.value
                
                if node.left:
                    cur_depth += 1
                    travesal(node.left,cur_depth)  
                    cur_depth -=1 # 回溯
                    
                if  node.right:
                    cur_depth +=1
                    travesal(node.right,cur_depth)
                    cur_depth -=1 # 回溯
            
        travesal(root,0)
        return left_leaves_value
    
    def find_bottom_left_leaves_iteration(self,root:TreeNode)->int:
        # 使用层序遍历找到最后一层的左下角的值
        if  not root:
            return 0 # 如果节点不存在，则返回0 ，具体返回值需要根据题设调整
        que = deque()
        que.append(root)
        result = 0 
        while len(que):
            size = len(que)
            for i in range(size):
                if i == 0: # 每次都取每一层的最左边的值
                    result = que[0]  
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return result
                
            
            