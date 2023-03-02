#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   反转字符串2.py
@Time    :   2023/03/02 21:26:38
@Author  :   gaochangju
@Version :   1.0
@Desc    :   None
'''
"""
给定一个字符串 s 和一个整数 k，从字符串开头算起, 
每计数至 2k 个字符，就反转这 2k 个字符中的前 k 个字符。
如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例:
输入: s = "abcdefg", k = 2
输出: "bacdfeg"   // bacd feg

"""


def function(s: str, k: int) -> list:
    # 定义反转单个字符串函数
    def reversal(char):
        if len(char) <= 1:
            return char
        left = 0
        right = len(char) - 1
        while left < right:
            # 每次交换 left 和right指针的两个位置
            temp = char[left]
            char[left] = char[right]
            char[right] = temp
            left += 1
            right -= 1
        return char

    n = len(s)
    if k >= n:
        return reversal(list(s))
    ans = list(s)
    # 下标i每次移动2k个位置
    for i in range(0, n, 2 * k):
        # 此时反转起始位置i~2k段的i~k，反转之后调到下一个2k起点
        ans[i:i + k] = reversal(ans[i:i + k])

    return "".join(ans)


def functionb(s: str, k: int) -> list:
    # 使用pythonic的写法
    index = 0
    n = len(s)
    while index < n:
        index2 = index + k
        s = s[:index] + s[index:index2][::-1] + s[index2:]
        # 每次向前移动2k步
        index = index + 2*k
    return s


if __name__ == "__main__":
    s = "abcdefg"
    k = 2
    print(function(s, k))
    print(functionb(s, k))
