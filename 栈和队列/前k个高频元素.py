#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   前k个高频元素.py
@Time    :   2023/03/13 11:49:44
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
""" 
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
提示：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 $O(n \log n)$ , n 是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。

"""
import heapq

def function(nums:list[int],k:int):
    # 统计元素出现的频率
    map_ = {}
    for i in range(len(nums)):
        map_[nums[i]] = map_.get(nums[i],0) + 1
        
    # 用固定大小为k的小顶堆,扫描所有元素的数值
    heaq_list = []
    for item,freq in map_.items():
        heapq.heappush(heaq_list,(freq,item))
        if len(heaq_list) > k:
            heapq.heappop(heaq_list)
    # 因为是小顶堆，所以倒序输出,
    print(heaq_list)
    result = [0]*k
    # range(start,stop[,step]) stop的值不会访问，所以在做倒序输出的时候是要注意（我总结这种特性叫 顾头不顾腚）
    for i in range(k-1,-1,-1):
        result[i] = heapq.heappop(heaq_list)[1]
 

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    function(nums=nums,k=k)
    