#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   左旋转字符串.py
@Time    :   2023/03/03 13:57:33
@Author  :   gaochangju 
@Version :   1.0
'''
""" 
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：
输入: s = "abcdefg", k = 2
输出: "cdefgab"

示例 2：
输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"

限制：
1 <= k < s.length <= 10000
"""


def function(s: str, k: int) -> str:
    # 要求，在不借助辅助空间的前提下进行操作
    # 解法：
    #   翻转前k个字符
    #   翻转后n-k个字符
    #   翻转全部字符

    def reverse(char):
        n = len(char)
        _left = 0
        _right = n - 1
        while _left < _right:
            tmep = char[_left]
            char[_left] = char[_right]
            char[_right] = char[_left]
            _left += 1
            _right -= 1

    s_list = list(s)
    n = len(s_list)
    s_list[:k] = s_list[:k][::-1]
    s_list[k:] = s_list[k:][::-1]
    s_list = s_list[::-1]
    # 是的，我没有用定义的内函数reverse，用了python中切片，写reverse纯属娱乐。
    return "".join(s_list)
    


if __name__ == "__main__":
    s = "lrloseumgh"
    k = 6
    print(function(s, k))
