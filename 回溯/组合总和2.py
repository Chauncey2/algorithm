#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   组合总和2.py
@Time    :   2023/03/29 17:57:42
@Author  :   gaochangju 
@Version :   1.0
'''

""" 
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明： 所有数字（包括目标数）都是正整数。解集不能包含重复的组合。

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

【注】

这题是在经典回溯问题上的变化，新增条件，
组合之间不允许有重复（在同一层的递归上，不能选择相同的元素）
同一组合允许元素重复（在同一分支上允许元素重复）

那么去重操作就现在只for loop中，
首先对candidates list 进行排序，然后在for loop中，如果前一个元素已经执行过了（后一个元素和前一个元素相同），
那么后一个迭代应该跳过
"""

# here put the import lib




from typing import List
class Solution:
    def __init__(self) -> None:
        self.path = []
        self.results = []
        self.usage_list = []

    def combination_sum(self, candidates: List[int], target: int) -> List[int]:
        if not len(candidates):
            return []
        self.path =[]
        self.results=[]
        self.usage_list = [False] * len(candidates)
        # 数组提前排序
        candidates.sort()
        self.backtracking_usage(candidates, target, 0, 0)
        return self.results

    def backtracking_usage(self, candidates: List[int], target: int, _sum: int, start_index: int) -> None:

        if _sum == target:
            self.results.append(self.path[:])
            return

        for i in range(start_index, len(candidates)):
            # 剪枝
            if _sum + candidates[i] > target:
                return
           
            # 去除同一层的重复元素
            if i > start_index and candidates[i] == candidates[i-1] and self.usage_list[i-1] == False:
                continue
            _sum += candidates[i]
            self.path.append(candidates[i])
            self.usage_list[i] = True  # 告诉同一枝，这个元素我用过了
            self.backtracking_usage(candidates, target, _sum, i+1)
            # 回溯
            _sum -= candidates[i]
            self.path.pop()
            self.usage_list[i] = False  # 告诉同一层，这个元素用过了
            
    def backtracking(self,candidates:List[int],target:int,_sum:int,start_index)->None:
        """不适用usage_list的实现"""
        
        if _sum == target:
            self.results.append(self.path[:])
            return
        for i in range(start_index,len(candidates)):
            # 剪枝操作放在for循环内部，省去了一步递归操作
            if _sum + candidates[i] >target:
                return
            if i > start_index and candidates[i] == candidates[i-1]:
                continue
            _sum += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates,target,_sum,i+1)
            # 回溯
            _sum -= candidates[i]
            self.path.pop()
            
    def combination_sum2(self,candidates:List[int],target:int)->List[int]:
        if not len(candidates):
            return []
        self.path=[]
        self.results=[]
        candidates.sort()
        self.backtracking(candidates,target,0,0)
        return self.results


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution().combination_sum(candidates, target))
    print(Solution().combination_sum2(candidates,target))
