#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   翻转字符串里的单词.py
@Time    :   2023/03/03 10:01:43
@Author  :   gaochangju 
@Version :   1.0
'''
""" 
翻转字符串中的每个单词，（不是翻转单词中的字母顺序，而是翻转字符串宏单词的位置）
示例
输入: "the sky is blue"
输出: "blue is sky the"
"""


def function(s: str) -> str:
    """ 
    一段字符的直接替换，需要注意的是，被替换的两个单词的长度可能不同
    """
    # 将字符串中的单词按照空格切分，如果按照空格进行翻转，那么空间复杂度就变成了O(n)，题目的难度就变小
    # 如果要求空间复杂度为O(1),即不适用辅助空间
    char = []
    temp = ''
    n = len(s)
    right = n - 1
    s.split(" ")


def functionb(string: str) -> str:
    
    def trim_space(s):
        # 定义去除字符串中的空格函数
        temp = list(s)
        n = len(temp)
        left = 0
        right = n - 1
        # 去除首位空白字符
        while left < n and s[left] == " ":
            left += 1
        while right > 0 and s[right] == " ":
            right -= 1

        # 去除字符串中的多余字符
        ans = []
        while left <= right:
            if temp[left] != " ":
                ans.append(temp[left])
            elif ans[-1] != " ":  # 去除字符串中的空格（入股当前的位置上是空格，但是相邻的位置上不是空格，那么这个空格就是单个空格）
                ans.append(temp[left])
            left += 1
        return "".join(ans)

    def reverse_string(s):
        # 定义翻转字符函数
        # 最小操作单元
        char = list(s)
        n = len(char)
        _left = 0
        _right = n - 1
        while _left < _right:
            temp = char[_left]
            char[_left] = char[_right]
            char[_right] = temp
            _left += 1
            _right -= 1
        return "".join(char)

    # 去掉字符串中多余的空格
    string = trim_space(string)
    # 翻转整个字符串
    string = reverse_string(string)
    str_list = list(string)
    n = len(str_list)
    left = 0
    right = 0
    # 翻转单词
    while right <= n-1:
        if str_list[right] == " " or right+1 == n:
            str_list[left:right] = reverse_string(str_list[left:right])
            right +=1
            left = right
        right+=1
    return "".join(str_list)


if __name__ == "__main__":
    s = "the sky is   blue"
    ans = functionb(s)
    print(ans)
