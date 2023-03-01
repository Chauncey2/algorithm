#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   移除链表元素.py
@Time    :   2023/02/24 11:21:37
@Author  :   gaochangju 
@Version :   1.0
'''

'''
移除链表中元素等于val的节点
'''

# here put the import lib




from list_node_init import ListNode
from list_node_init import init_single
from list_node_init import traversal
def remove(head: ListNode, value: int) -> ListNode:
    """移除链表中元素值为value的节点

    Args:
        head (ListNode): 头节点
        value (int): 元素值

    Returns:
        ListNode: 头节点
    """
    # 单链表的删除元素，不需要另外的节点变量做保存，使用next就可以做，
    # 在其他语言中，尤其是在C中，需要另外的变量保存并回收内存，否则会造成内存溢出
    cur = head
    while cur.next:
        if cur.next.val == value:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


if __name__ == "__main__":
    head_list = [1, 2, 6, 3, 4, 5, 6]
    val = 6
    head_node = init_single(vals=head_list)
    # traversal(head_node)
    head_node = remove(head_node, val)
    traversal(head_node)
