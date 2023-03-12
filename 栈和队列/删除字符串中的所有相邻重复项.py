#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   删除字符串中的所有相邻重复项.py
@Time    :   2023/03/12 15:34:59
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
""" 
题目
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 S 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

示例：

输入："abbaca"
输出："ca"
解释：例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，
这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
提示：

1 <= S.length <= 20000
S 仅由小写英文字母组成。

用栈就可以实现
"""

def function(S:str)->str:
    stack = []
    for s in S:
        if not len(stack):
            stack.append(s)
        elif s == stack[-1]:
            stack.pop()
        else:
            stack.append(s)
    return "".join(stack)


if __name__ == "__main__":
    s = "abbaca"
    print(function(s))