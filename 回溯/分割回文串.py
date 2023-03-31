#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   切割回文串.py
@Time    :   2023/03/31 14:24:33
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
""" 
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。
示例: 输入: "aab" 输出: [ ["aa","b"], ["a","a","b"] ]
"""
from typing import List

class Solution:
    def __init__(self) -> None:
        self.path = []
        self.result = []
        
    def partition(self,s:str)->List[int]:
        if not len(s):
           return []
        self.path=[]
        self.result =[]
        self.backtracking(s,0)
        return self.result 
    
    def backtracking(self,s:str,start_index:int):
        if start_index >= len(s):
            self.result.append(self.path[:])
            return
        
        for i in range(start_index,len(s)):
            temp = s[start_index:i+1]
            if temp == temp[::-1]:
                self.path.append(temp)
                self.backtracking(s,i+1)
                # 回溯
                self.path.pop()
            else:
                continue
            
if __name__ == "__main__":
    s = "aab"
    print(Solution().partition(s))