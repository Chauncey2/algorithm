#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   有序数组的平方.py
@Time    :   2023/02/22 14:29:11
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
示例 1： 输入：nums = [-4,-1,0,3,10] 输出：[0,1,9,16,100] 解释：平方后，数组变为 [16,1,0,9,100]，排序后，数组变为 [0,1,9,16,100]
示例 2： 输入：nums = [-7,-3,2,3,11] 输出：[4,9,9,49,121]
"""


def func1(nums: list) -> list:
    """暴力解法"""
    result = list(map(lambda x: pow(x, 2), nums))
    result.sort()  # list 自带的排序方法默认递增排序
    return result


def func2(nums: list) -> list:
    """双指针法"""
    result = list()
    left = 0
    right = len(nums) - 1
    # 注意 left = right 的临界条件，如果缺少，会漏掉最后一个数
    while left <= right:
        pow_left = pow(nums[left], 2)
        pow_right = pow(nums[right], 2)
        if pow_left < pow_right:
            result.insert(0, pow_right)
            right -= 1
        else:
            result.insert(0, pow_left)
            left += 1
    return result


if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    print(func1(nums=nums))
    print(func2(nums=nums))
