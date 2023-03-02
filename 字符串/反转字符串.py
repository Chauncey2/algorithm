#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   反转字符串.py
@Time    :   2023/03/02 21:09:57
@Author  :   gaochangju
@Version :   1.0
@Desc    :   None
'''
"""
编写一个函数，其作用是将输入的字符串反转过来。
输入字符串以字符数组 char[] 的形式给出。
示例 1：
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]

示例 2：
输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]

"""


def function(char: list) -> list:
    """
    这题很简单：
    使用双指针法既可以在O(n)的时间复杂度
    O(1)的空间复杂度下就可以完成字符的反转
    """
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


if __name__ == "__main__":
    char = ["h","e","l","l","o"]
    print(function(char=char))
