#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   滑动窗口最大值.py
@Time    :   2023/03/12 16:10:01
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
from collections import deque


class myQueue:
    def __init__(self):
        self.queue = deque()
    
    def push(self,val):
        # 窗口队列只需要保证每队首的元素最大
        # 比较的方法是从队尾依次比较，这一步骤是为了保证队列有序（降序）
        while self.queue and val > self.queue[-1]:
            self.queue.pop()
        self.queue.append(val)
    
    def pop(self,val):
        # 如果滑动窗口移除的值比队首的小，则不需要做任何操作
        if self.queue and val == self.queue[0]:
            self.queue.popleft()
        
    def front(self):
        # 返回当前chuang口的最大值
        return self.queue[0]

def function(nums:list,k:int):
    windows = myQueue()
    ans = []
    # 前k个值先入队列
    for i in range(k):
        windows.push(nums[i])
    ans.append(windows.front())
    for i in range(k,len(nums)):
        # 每滑动一次就有一个元素出窗口(逻辑上，队列末尾的元素出队，但是原则上)
        windows.pop(nums[i-k])
        windows.push(nums[i])
        ans.append(windows.front())
    return ans


if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(function(nums=nums,k=k))
