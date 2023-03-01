#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   翻转链表.py
@Time    :   2023/02/26 18:30:45
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
""" 
两种方法反转一个单链表
"""


# 双指针法
# 递归法
# 使用栈解决反转链表的问题（栈解决）

from list_node_init import ListNode
from list_node_init import traversal
from list_node_init import init_single

def double_pointer(head:ListNode):
    """ 
    双指针法倒转单链表，需要另外的一个临时变量保存节点预防断链
    """
    cur = head.next
    per = None
    while cur:
        # 保存cur的下一个节点
        temp = cur.next
        # 反转链表
        cur.next = per
        # per 移动到cur到位置，cur移动大下一个位置
        per = cur
        cur = temp
    # 跳出循环此时 per指向的就是链表的第一个节点
    head.next = per
    # 传入的链表是带头节点的，如果不带头节点，则可直接返回per
    return head
    
        
def reverse(pre,cur):
    # 临界条件
    if not cur:
        return pre
    # 执行体
    temp = cur.next
    cur.next = pre
    # 返回体
    return reverse(cur,temp)
    

def reverseList(head:ListNode):
    # 递归体返回的是不带头节点的，在执行结束后，给链表添加上头节点
    head.next = reverse(None,head.next)
    return head


def stack_func(head:ListNode):
    """ 
    递归的本质可以通过栈实现
    """
    # 定义逻辑栈
    stack = list()
    cur = head.next
    # 将节点依次入栈
    while cur:
        temp = cur.next
        cur.next = None
        stack.insert(0,cur)
        cur = temp
    # 依次出栈并使用尾插法重构链表
    tail = head
    while len(stack):
        node = stack.pop()
        tail.next = node
        # tail 后移
        tail = node 
    return head
    
 

if __name__ == "__main__":
    vals = [1, 2, 3, 4, 5, 6]
    head = init_single(vals)
    traversal(head)
    
    # print("双指针法翻转链表")
    # head_node = double_pointer(head)
    # traversal(head_node)
    
    print("递归法反转链表")
    head_node = reverseList(head)
    traversal(head_node)
    
    print("栈")
    head_ode = stack_func(head)
    traversal(head_node)