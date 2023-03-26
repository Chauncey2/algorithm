#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   组合问题.py
@Time    :   2023/03/25 16:51:27
@Author  :   gaochangju 
@Version :   1.0
'''
from typing import List

""" 
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
示例: 输入: n = 4, k = 2 输出: [ [2,4], [3,4], [2,3], [1,2], [1,3], [1,4], 
"""

class Solution:
    def __init__(self) -> None:
        self.result =[] # 路径结果集
        self.path =[] # 路径集合
        
    def backtracing_unpruning(self,n:int,k:int,startIndex:int):
        """ 回溯法，没有剪枝"""
        if len(self.path) == k:
            self.result.append(self.path[:])
            return 
        for i in range(startIndex,n+1):
            self.path.append(i)
            self.backtracing_unpruning(n,k,i+1)
            self.path.pop() # 回溯，撤销此次操作
            
    def combination(self,n:int,k:int,startIndex:int)->List[list]:
        result = self.backtracing_unpruning(n,k,startIndex)
        return self.result
    
    def backtracing_pruning(self,n:int,k:int,startIndex:int):
        """ 回溯法，有剪枝"""
        if len(self.path) == k:
            self.result.append(self.path[:])
            return 
        
        for i in range(startIndex,n-(k-len(self.path))+2):
            print(startIndex,n-(k-len(self.path))+2)
            self.path.append(i)
            self.backtracing_pruning(n,k,i+1)
            self.path.pop()
            
    def combination_pruning(self,n,k):
        self.backtracing_pruning(n,k,1)
        return self.result
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]  #存放符合条件结果的集合
        path=[]  #用来存放符合条件结果
        def backtrack(n,k,startIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(startIndex,n-(k-len(path))+2):  #优化的地方
                path.append(i)  #处理节点
                backtrack(n,k,i+1)  #递归
                path.pop()  #回溯，撤销处理的节点
        backtrack(n,k,1)
        return res

if __name__ == "__main__":
    s = Solution()
    # print(s.combination(4,2,1))
    print(s.combination_pruning(4,2))
    # print(s.combine(4,2))
    
    