#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   环形链表.py
@Time    :   2023/02/28 17:44:37
@Author  :   gaochangju 
@Version :   1.0
'''
""" 
给定一个链表，返回链表开始入环的第一个节点
如果链表无环，则返回null
快慢指针判断链表的

"""




from list_node_init import init_loop
from list_node_init import traversal
from list_node_init import ListNode
def loop_chain(head: ListNode):
    """ 
    环形链表找到如环的第一个节点
    """
    # 快慢指针判断是否是环链
    fast = head.next
    slow = head.next
    while fast != slow:
        if not fast:
            return None
        # 快指针每次移动2个位置
        fast = fast.next.next
        slow = slow.next
    # 跳出循环表示链表存在环，记录此时的相遇点
    index2 = fast
    index1 = head.next
    while index1 != index2:
        index1 = index1.next
        index2 = index2.next
    res = index1
    return res


if __name__ == "__main__":
    pass
