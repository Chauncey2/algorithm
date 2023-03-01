#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   删除倒数第N个节点.py
@Time    :   2023/02/28 11:04:03
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
'''
删除链表倒数第N个节点
'''




from list_node_init import ListNode
from list_node_init import init_single
from list_node_init import traversal
def remove(head: ListNode, n: int):
    pre = head
    tail = head
    # tail 指针先行n步骤
    for _ in range(n):
        tail = tail.next
    # 双指针一起移动
    while tail.next:
        pre = pre.next
        tail = tail.next
    # 此时 pre 的后一个节点就是需要删除的节点
    pre.next = pre.next.next
    return head


if __name__ == "__main__":
    vals = [1, 2, 3, 4, 5, 6]
    n = 2
    head_node = init_single(vals=vals)
    traversal(head_node)
    head_node = remove(head=head_node,n=n)
    traversal(head_node)
    
