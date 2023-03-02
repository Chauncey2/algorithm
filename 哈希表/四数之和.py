#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   四数之和.py
@Time    :   2023/03/02 15:51:19
@Author  :   gaochangju 
@Version :   1.0
'''

"""
题意：给定一个包含 n 个整数的数组 nums 和一个目标值 target，
判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？
找出所有满足条件且不重复的四元组。

注意：
答案中不可以包含重复的四元组。
示例： 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
满足要求的四元组集合为： [ [-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2] ]
#
"""

# 四数之和的处理方法和三数之和类似，只是 多了一成for循环，
# 但是需要注意的一点是，


def function(nums: list, target: int) -> list:
    """ 
    """
    nums = sorted(nums)
    print(nums)
    ans = []
    n = len(nums)
    for i in range(n):
        # a 去重
        if i > 1 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n):
            # b 去重
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            left = j+1
            right = n-1
            while left < right:
                
                count = nums[i] + nums[j] + nums[left] + nums[right]
                if count > target:
                    right -= 1
                elif count < target:
                    left += 1
                else:
                    ans.append([nums[i], nums[j], nums[left], nums[right]])
                    # c 去重
                    while left != right and nums[left] == nums[left-1]:
                        left += 1
                    # d 去重
                    while left != right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
    return ans


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(function(nums,target))
