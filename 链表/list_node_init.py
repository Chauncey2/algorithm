#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   list_node_init.py
@Time    :   2023/02/23 11:10:10
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib

# 定义节点类


class ListNode(object):
    def __init__(self, val, next=None, nums=0):
        self.val = val
        self.next = next
        self.nums = 0  # 用于记录编表中节点个数的变量，一般node无需定义，但是可以在head中使用


def init_single(vals: list, head=True):
    """单链表初始函数,
    Args:
        node (ListNode): 节点
        vals (list): 节点个数
        head (bool):生成的链表是否带头指针
    """
    # 定义头指针
    head_node = ListNode(0)
    # p = ListNode(0)
    p = head_node
    # 头插法创建
    for val in vals:
        node = ListNode(val)
        p.next = node
        p = node
    if not head:
        return head_node.next
    return head_node


class ListNode2(object):
    def __init__(self, val, next=None, per=None) -> None:
        self.val = val
        self.per = per
        self.next = next


def init_double(vals: list, head=True):
    """初始化双链表

    Args:
        node (ListNode): 节点
        vals (list): 链表的初始化值
        head (bool, optional): 返回的链表是否带头指针
    """
    # 定义头指针
    head_node = ListNode2(-1)
    p = head_node
    # 尾插法
    for val in vals:
        node = ListNode2(val)
        p.next = node
        node.per = p
        p = p.next  # 标记节点后移

    if not head_node:
        return head_node.next
    return head_node


def init_loop(vals: list,):
    """循环链表
    循环链表必须带头指针

    Args:
        vals (list): 链表的初始化值集合
    """
    head_node = ListNode(-1)
    p = head_node
    for val in vals:
        node = ListNode(val)
        p.next = node
        p = p.next

    # 单链表成环
    p.next = head_node.next

    return head_node


def traversal(head: ListNode) -> None:
    """遍历链表

    Args:
        head (ListNode): 链表头指针
    """
    p = head.next
    vals = []
    while p:
        # 这个循环条件无法处理循环链表 
        vals.append(str(p.val))
        p = p.next
    list_str = " -> ".join(vals)
    print(list_str)


def traversal_loop(head: ListNode) -> None:
    """遍历循环链表

    Args:
        head (ListNode): 头指针
    """
    p = head.next
    while p.next != head.next:
        print(p.val)
        p = p.next
    # 输出循环链表的 最后一位
    print(p.val)


def init_intersect(listA:list,listB:list,skipa:int,skipb:int):
    # 根据传入的值，构造交叉列表
    pass

if __name__ == "__main__":
    vals = [1, 2, 3, 4]
    # head = init_single(vals)
    # traversal(head=head)
    # head_double = init_double(vals)
    # traversal(head_double)
    head_loop = init_loop(vals)
    traversal_loop(head_loop)
