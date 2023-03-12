#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   有效的括号.py
@Time    :   2023/03/12 15:23:17
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
 
"""
def is_valid(s:str)->bool:
    stack = []
    
    for item in s:
        if item == "(":
            stack.append(")")
        elif item == "{":
            stack.append("}")
        elif item == "[":
            stack.append("]")
        else:
            # if not stack or stack.pop() != item: (比较值不用取出来，减少不必要的性能损耗)
            if not stack or stack[-1] != item:
                return False
            stack.pop()
        return len(stack) == 0

if __name__ == "__main__":
    pass
