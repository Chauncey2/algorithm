#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   螺旋矩阵2.py
@Time    :   2023/02/22 16:50:54
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
"""
给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
示例:
输入: 3 输出: [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] 
"""


def func(n: int) -> list:
    """螺旋矩阵
    螺旋矩阵考察的是coder对代码的掌控程度，
    对各种边界条件的感知程度：

    """
    # 初始化一个n*n维矩阵
    matrix = [[0] * n for _ in range(n)]
    print(matrix)
    # 定义初始位置
    left = 0
    down = n-1
    right = n - 1
    up = 0

    number = 1
    while left < right and up < down:  # 循环的终止条件：

        # 从左到右
        for i in range(left, right):
            matrix[up][i] = number  # 从左到右，行不变
            number += 1
        # 从上到下
        for i in range(up, down):
            matrix[i][right] = number # 从上到下，列不变
            number += 1
        # 从右向左
        for i in range(right, left, -1):
            matrix[down][i] = number
            number += 1
        # 从下向上
        for i in range(down, up, -1):
            matrix[i][left] = number
            number += 1

        # 矩阵画下一圈的起始位置，可以想象所有的起始点都向内部”坍塌“一层
        left += 1
        right -= 1
        up += 1
        down -= 1

    # 当n 为奇数时候，最后剩下一个元素需要处理
    if n % 2 != 0:
        matrix[n//2][n//2] = number
    return matrix


if __name__ == "__main__":
    result = func(3)
    print(result)
