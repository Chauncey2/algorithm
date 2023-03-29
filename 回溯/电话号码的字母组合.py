#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   电话号码的字母组合.py
@Time    :   2023/03/28 18:17:16
@Author  :   gaochangju 
@Version :   1.0
'''


""" 
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
"""


class Solution:
    def __init__(self) -> None:
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        self.answer = ""
        self.result = []
    def function(self,digits,index):
        if not len(digits):
            return []
        self.backtracting(digits,index)
        return self.result
        
        
        
    def backtracting(self, digits:str, index:int)-> None:
        # 回溯中止条件
        if index == len(digits):
            self.result.append(self.answer[:])
            return 
        letters = self.letter_map[digits[index]] # 获取语料
        for i in letters:
            self.answer +=i
            self.backtracting(digits,index+1)
            self.answer = self.answer[:-1] # 回溯

if __name__ == "__main__":
    print(Solution().function("23",0))
        
