#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   四叔之和ll.py
@Time    :   2023/03/02 13:18:49
@Author  :   gaochangju 
@Version :   1.0
'''

"""
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，
使得 A[i] + B[j] + C[k] + D[l] = 0。
为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。
所有整数的范围在 -2^28 到 2^28 - 1 之间，最终结果不会超过 2^31 - 1 。

例如:

输入:

A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2] 

难度升级：
在一个数组中，挑选出和为0的四个元素组合的个数，并且要求出现的元组不能重复

"""


def function(A: list[int], B: list[int], C: list[int], D: list[int]) -> int:
    """ 
    将问题简化成两个”数“之和，即两组数字进行操作,那么这个问题就变成了 ”两数之和.py“
    """
    hash_map = dict()
    for a in A:
        for b in B:
            if a+b not in hash_map:
                hash_map[a+b] = 1
            else:
                hash_map[a+b] += 1
    # 验证 -（c+d）是否在集合中
    count = 0
    for c in C:
        for d in D:
            nums = 0 - (c+d)
            if nums in hash_map:
                count += hash_map[nums]
    return count


if __name__ == "__main__":
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(function(A, B, C, D))
