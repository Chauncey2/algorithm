#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   用队列实现栈.py
@Time    :   2023/03/12 14:34:22
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
""" 
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空

只能使用队列的基本操作，不能使用不属于队列的性质
队列的方法：
push to back, 
peek/pop from front, 
size,  i
s empty
"""




from collections import deque

class MyStack:
    def __init__(self) -> None:
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, val):
        self.queue_in.append(val)

    def pop(self):
        if self.empty():
            return None

        for _ in range(len(self.queue_in)-1):
            self.queue_out.append(self.queue_in.popleft())
        ans = self.queue_in.pop()
        # 交换 两个队列的“位置”
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return ans

    def empty(self):
        # 两个队列实现栈的方法中，只有一个队列（in队列）是时刻存了元素的

        # 在返回值中，可以直接返回队列的长度，但是从标准上来说，empty返回的是bool
        # 所以在返回值的时候要做布尔运算
        return len(self.queue_in) == 0
    
    def top(self):
        # 从栈顶获取元素
        return self.queue_in[-1]
        # 以下方法一样可以实现top，但是想多了，大可不必如此实现
        # if self.empty():
        #     return None
        # ans = self.pop()
        # self.queue_in.append(ans)
        # return ans
    
    def __str__(self) -> str:
        pass
        # print(self.queue_in)


if __name__ == "__main__":
    my_stack = MyStack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    print(my_stack.top())
    print(my_stack.top())
    # print(my_stack)
    
