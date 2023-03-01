#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   链表相交.py
@Time    :   2023/02/28 13:56:36
@Author  :   gaochangju 
@Version :   1.0
'''

""" 
默认链表相交是两条链表相交，且有链表相交
"""




from list_node_init import ListNode
from list_node_init import init_single
from list_node_init import traversal
def interfect(headA: ListNode, headB: ListNode):
    # 计算两个节点的长度
    cur_a = headA.next
    cur_b = headB.next
    # 计算两个链表的长度
    len_a = 0
    len_b = 0
    while cur_a.next:
        cur_a = cur_a.next
        len_a += 1

    while cur_b.next:
        cur_b = cur_b.next
        len_b += 1
    cur_a = headA.next
    cur_b = headB.next

    def swap(a, b):
        temp = a
        a = b
        b = temp
    # 默认A链是最长的
    if len_a < len_b:
        swap(len_a, len_b)
        swap(cur_a, cur_b)
    garp = len_a - len_b

    # 将A链的指针和B同步
    for _ in range(garp):
        cur_a = cur_a.next

    while cur_a.next:
        if cur_a == cur_b:
            return cur_a
        cur_a = cur_a.next
        cur_b = cur_b.next
    return None


# here put the import lib
if __name__ == "__main__":
    pass
