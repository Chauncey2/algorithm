#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   逆波特兰表达式求值.py
@Time    :   2023/03/12 15:42:29
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
""" 
有效的运算符包括 + ,  - ,  * ,  / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。 给定逆波兰表达式总是有效的。
换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

示例 1：
输入: ["2", "1", "+", "3", " * "]
输出: 9
解释: 该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9

备注：用栈，根据逆波兰运算的性质具体操作如下
 遇到数字入栈，遇到运算符就出栈两个元素，运算结果重新入栈，知道最后获取最后结果
"""


def function(expression: list) -> int:
    stack = []
    # 字符串预处理，去除每个字符前后的空格(字符串操作类型的题目，要注意题设中的特殊字符陷阱)
    expression = [s.strip() for s in expression]
    
    for val in expression:
        if val not in ["+", "-", "*", "/"]:
            stack.append(int(val))
        else:
            if val == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1+num2)
                
            elif val == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1*num2)
                 
            elif val == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2//num1)
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2-num1)

    ans = stack.pop()
    return ans

if __name__ == "__main__":
    express = ["2", "1", "+", "3", " * "]
    print(function(expression=express))
