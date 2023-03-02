#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   三数之和.py
@Time    :   2023/03/02 14:22:13
@Author  :   gaochangju 
@Version :   1.0
'''

"""
给你一个包含 n 个整数的数组 nums，
判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 
请你找出所有满足条件且不重复的三元组。

注意： 答案中不可以包含重复的三元组 （不能有重复的三元组，但是三元组中的元素可以重复）
"""
# 能够想到的方法比暴力解法优化一点的就是双指针解法


def functionA(nums: list) -> list:
    # 对数组进行递增排序
    nums = sorted(nums)
    n = len(nums)
    ans = []
    for i in range(n):
        left = i+1
        right = n-1
        if nums[i] > 0:
            break
        # a 去重
        if i >= 1 and nums[i] == nums[i-1]:
            continue
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                ans.append([nums[i], nums[left], nums[right]])
                # b 去重
                while left != right and nums[left] == nums[left+1]:
                    left += 1
                # c 去重
                while left != right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return ans



if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(functionA(nums))
