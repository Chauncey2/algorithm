#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   二分法.py
@Time    :   2023/02/21 15:30:00
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib

"""
不重复数组，递增，二分法找元素
开区间的界定要注意的是临界条件的判断

"""

def func1(nums:list,target:int) -> int:
    
    left = 0 
    right = len(nums) - 1
    while left <= right:
        # python3中需要使用地板除
        # middle = (left + right) // 2
        middle = left + (right - left ) // 2
        if nums[middle] > target:
            right = middle -1
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle
        
    return -1

def func2(nums:list,target:int) -> int:
    """开区间二分法表示"""
    left = 0
    right = len(nums)
    while left < right:
        middle = left + (right - left) // 2
        if nums[middle] > target:
            right = middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1
    


if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    result = func1(nums=nums,target=target)
    print(result)
    result = func2(nums=nums,target=target)
    print(result)
    