#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   替换空格.py
@Time    :   2023/03/02 22:48:29
@Author  :   gaochangju
@Version :   1.0
@Desc    :   None
'''
"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"
例如：
s = "We are happy."
输出："We%20are%20happy."
"""


# 双指针的用法
def function(s: str) -> str:
    count = s.count(" ")
    char = list(s)
    # 每遇到一个空字符串，就将链表库哟冲两个位置
    char.extend([" "] * count * 2)
    left = len(s) - 1
    right = len(char) - 1
    # 终止条件是 left指针不越界
    while left >= 0:
        if char[left] != ' ':
            char[right] = char[left]
            right -= 1
        else:
            # 每次遇到空格需要覆盖三个位置
            char[right - 2:right + 1] = "%20"
            # right 指针前移三个位置
            right -= 3
        left -= 1
    return ''.join(char)


# here put the import lib
if __name__ == "__main__":
    s = "We are happy."
    print(function(s))