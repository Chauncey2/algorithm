#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   两数之和.py
@Time    :   2023/03/02 10:57:35
@Author  :   gaochangju 
@Version :   1.0
'''
""" 
使用集合做记录，两数之和问题就转换成了，在集合中寻找元素是否存在或者是否出现过
"""

def function(nums:list[int],target:int)->list[int]:
    """在数组nums中找到两个数，他们的和为target
    Args:
        nums (list): 整数数组
        target (int): 目标值

    Returns:
        tuple: 数组下标
    """
    record = dict()
    for i in range(len(nums)):
        need_num = target - nums[i]
        if need_num in record:
            return [record[need_num],i]
        record[nums[i]] = i
    return []
    
    

# here put the import lib
if __name__ == "__main__":
    nums = [2,2,7,8,9]
    target = 9
    print(function(nums,target))