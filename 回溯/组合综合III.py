#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   组合综合III.py
@Time    :   2023/03/27 10:09:25
@Author  :   gaochangju 
@Version :   1.0
'''

""" 
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
说明：
所有数字都是正整数。
解集不能包含重复的组合。
示例 1: 输入: k = 3, n = 7 输出: [[1,2,4]]
示例 2: 输入: k = 3, n = 9 输出: [[1,2,6], [1,3,5], [2,3,4]]
"""

from typing import List
class Solution:
    def __init__(self) -> None:
        self.path = []
        self.result = []
        self.sum = 0
    
    def combinationSum(self,n:int,k:int)->List[list]:
        """调用回溯结果

        Args:
            n (int): 
            k (int): 

        Returns:
            List[list]: 
        """
        self.backtracking()
        return self.result
    
    def backtracking(self,n:int,k:int,start_num:int):
        """使用回溯法解决问题
        """
        # 如果当前的和已经大于n了，那么后续的结果也就没有必要遍历了
        if self.sum > n:
            return 
        
        if len(self.path) == k:
            if self.sum == n:
                self.result.append(self.path[:])
                return 
        for i in range(start_num,n-(k-len(self.path)+1)):
            self.path.append(i)
            self.sum+=i
            # 递归
            self.backtracking(n,k,i+1)
            # 回溯
            self.path.pop()
            self.sum -=i
        

