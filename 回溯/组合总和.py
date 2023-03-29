#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   组合总和.py
@Time    :   2023/03/29 16:40:51
@Author  :   gaochangju 
@Version :   1.0
'''

""" 
给定一个无重复元素的数组 candidates 和一个目标数 target
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为： [ [7], [2,2,3] ]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为： [ [2,2,2,2], [2,3,3], [3,5] ]
#
"""

# here put the import lib
from typing import List
class Solution:
    def __init__(self) -> None:
        # self._sum = 0 不能设置为全局变量，因为每一个递归路径得到的sum都不同
        self.path = []
        self.result = []
        
    def backtracing(self,candidates:List[int],target:int,_sum:int,start_index:int)->None:
        # if len(candidates) == len(self.path): # 题设规定可以重复
        #     return 
        if _sum == target:
            self.result.append(self.path[:])
            return 
        if _sum > target:  # 和已经大于目标值了，剪纸
            return 
        for i in range(start_index,len(candidates)):
            _sum += candidates[i]
            self.path.append(candidates[i])
            self.backtracing(candidates,target,_sum,i)
            # 回溯
            _sum -= candidates[i]
            self.path.pop()
        
    def combination_sum(self,candidates:List[int],target:int)->List[list]:
        if not len(candidates):
            return []
        self.backtracing(candidates,target,0,0)
        return self.result

if __name__ == "__main__":
    candidates = [2,3,5]
    target = 8
    print(Solution().combination_sum(candidates,target))
            