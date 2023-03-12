#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   用栈实现队列.py
@Time    :   2023/03/03 17:58:51
@Author  :   gaochangju 
@Version :   1.0
'''

""" 
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。

注：
目的仅仅是 弄清stack 和 queue的性质
"""

class myQueue:
    def __init__(self) -> None:
        self.stack_in = []
        self.stack_out = []
    
    def push(self,val):
        # 入就是向stack_i中存
        self.stack_in.append(val)
        
    def pop(self):
        if self.empty():
            return None
        # 判断stack in是否含有元素
        if self.stack_out:
            return self.stack_out.pop() # list pop 是从末尾取元素
        else:
            for  _ in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
    
    def peek(self):
        # peek 函数从队首获取元素，但是并不从队列中删除
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self):
        return not (self.stack_in or self.stack_out)

if __name__ =="__main__":
    pass