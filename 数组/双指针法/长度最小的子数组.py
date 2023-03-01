#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   长度最小的子数组.py
@Time    :   2023/02/22 15:31:18
@Author  :   gaochangju 
@Version :   1.0
'''
"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，
并返回其长度。如果不存在符合条件的子数组，返回 0。
示例:
输入：s = 7, nums = [2,3,1,2,4,3] 输出：2 解释：子数组 [4,3] 是该条件下的长度最小的子数组。

注意：题设中设定是连续子数组，所以子数组的长度最小为2
#
"""

# here put the import lib


def func1(nums: list, s: int) -> int:
    """暴力破解法：
    双层for循环： 时间复杂度(O(n^2))、空间复杂度为 O(1)
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):  # 内层循环必须从i 的后一个位置开始
            # 很典型的错误，题设没读清楚，边界条件不明
            # if nums[i] + nums[j] > s:
            #     continue
            # else:
            #     return j - i + 1
            if sum(nums[i:j+1]) > s:
                continue
            else:
                # 如果 sum(nums[i:j+1] <= s) 满足题设条件
                return j - i + 1

    return 0


def func2(nums: list, s: int) -> int:
    """double pointer
    双指针:
    时间复杂度为O(1)
    空间复杂度为O(1)
    """
    start = 0
    end = 1
    size = len(nums)
    # 判断循环的临街条件，如果不带= ，则当end = size -1 ,即最后一个元素就会被跳过
    while end <= size - 1:
        if sum(nums[start:end+1]) > s:
            start += 1
            end += 1
        else:
            return end - start + 1
        # 错的很典型，留着
        # if nums[start] + nums[end] > s: 这个判断条件式错的，题目要求的是，区间内的元素之和，而不是首位之和
        #     start += 1
        #     end += 1
        # else:
        #     return end - start + 1
    return 0


# 引申：求 <= S 的最长子串(返回最长子串的长度) (最长子串就必须是小于s的了)
"""使用滑动窗口（双指针法）解决问题"""


def func3(nums: list, s: int) -> int:
    """
    最长子串还要有个记录器，记录最长的长度
    """
    sub_len = 0
    i = 0
    j = 1
    size = len(nums)
    while j < size:
        if sum(nums[i:j+1]) <= s:
            # 满足小于条件，则继续探索
            # sub_len_func = lambda x,y:x if x> y else y # 定义了一个获取最大值的lambda函数
            sub_len = max(sub_len, j-i+1)  # 每次循环都执行一次最长子串值的更新
            j += 1
        else:
            # 当条件不再满足时，则需要重置指针我只
            i += 1
            j = i+1
    return sub_len


if __name__ == "__main__":
    nums = [2, 3, 1, 2, 4, 3]
    s = 7
    print(func1(nums=nums, s=s))
    print(func2(nums=nums, s=s))
    print(func3(nums=nums, s=s))
