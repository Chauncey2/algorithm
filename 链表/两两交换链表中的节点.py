#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   两两交换链表中的节点.py
@Time    :   2023/02/27 11:20:32
@Author  :   gaochangju 
@Version :   1.0
'''
""" 
两两交换链表中的节点 遇到奇数如何处理
"""

# here put the import lib
from list_node_init import init_single
from list_node_init import traversal
from list_node_init import ListNode

def reverse_pair(head:ListNode):
    """ 
    两两翻转链表
    翻转的时候是可以使用临时变量保存链表中的节点的，思想上不要受到限制
    """
    cur = head.next
    pre = cur
    while not pre.next and pre.next.next:
        pass
    

if __name__ == "__main__":
    pass