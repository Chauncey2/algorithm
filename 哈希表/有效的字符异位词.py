#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   有效的字符异位词.py
@Time    :   2023/03/01 16:30:42
@Author  :   gaochangju 
@Version :   1.0
'''

"""
题设：
两个字符串，s和t ，判断t是否为s的字母异位词
分析：
（1）满足这个条件有个先决条件，就是 len(s)=len(t)；
（2）判断一个字符串是否在另一个“集合”中，首先想到使用hash表，这题就是使用hash表，用空间换时间。

使用数组来做哈希的题目，是因为题目都限制了数值的大小,
如果题设中没有规定字符的大概长度，则不适合用这种方法
"""


def function(s: list, t: list) -> bool:

    if len(t) != len(s):
        return False
    # 26个位置的记录器
    record = [0 for _ in range(26)]
    # 统计s中字符出现的位置和次数
    for c in s:
        record[ord(c)-ord("a")] += 1
    # t进行对比
    for c in t:
        record[ord(c)-ord("a")] -= 1
    # 统计record中 值为1的个数
    
    for i in range(26):
        if record[i]!=0:
            return False
    return True


if __name__ == "__main__":
    s = "anagram"
    t = "nagaran"
    print(function(s, t))
