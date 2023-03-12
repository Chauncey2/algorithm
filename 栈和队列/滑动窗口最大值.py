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
        pass
    
    def front(self):
        # 返回当前chuang口的最大值
        pass

def function(nums:list):
    pass
    


if __name__ == "__main__":
    pass
