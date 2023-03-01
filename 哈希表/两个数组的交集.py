#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   两个数组的交集.py
@Time    :   2023/03/01 17:13:59
@Author  :   gaochangju 
@Version :   1.0
'''
""" 
给定两个数组输出两个数组的交集，输出的交集元素唯一，且可以无序

"""

""" 
为什么没有使用python中自带的in操作符进行操作？

python中的in运算，本质上调用的是对象的__contains__方法，对于list来讲，__contains__方法
的时间复杂度为O(n), 结合本题，如果要使用in 时间复杂度就是O(n^2)

"""
def function(list_a: list, list_b: list) -> list:
    value_dict = dict()
    for i in list_a:
        value_dict[i] = 1

    intersection = []
    for i in list_b:
        # if i in value_dict.keys() and value_dict[i] == 1:
        if i in value_dict.keys():
            intersection.append(i)
    return intersection


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]
    b = [7, 8]
    print(function(a, b))
