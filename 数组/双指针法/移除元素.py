#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   移除元素.py
@Time    :   2023/02/21 17:38:00
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
"""
原地移除元素，要求空间复杂度O(1)
不需要考虑新数组中超出新长度后面的元素
"""


def func(nums: list, val: int) -> int:
    fast = 0
    slow = 0
    size = len(nums)
    while fast < size:
        # slow 用于保存非val值，fast用于寻找val
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast +=1
    return slow


if __name__ == "__main__":
    pass
