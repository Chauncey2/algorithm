#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   设计链表.py
@Time    :   2023/02/24 12:08:27
@Author  :   gaochangju 
@Version :   1.0
'''

# here put the import lib
'''
在链表类中实现这些功能：

get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。

都是对一些链表的基础功能进行编码，基础操作

'''




from list_node_init import ListNode
from list_node_init import init_single
from list_node_init import traversal
class MyLinkedList:
    """"""

    def __init__(self) -> None:
        self._head = ListNode(0)  # 虚拟节点
        self._size = 0  # 添加节点数

    def get(self, index: int):
        if index < 0 and index > self._size:
            return -1
        cur = self._head.next
        count = 1 
        while count == index:
            cur = cur.next
            count += 1

        return cur

    def addAtHead(self, val):
        """头插法将节点插入链表"""
        node = ListNode(val)
        cur = self._head.next  # 记录节点
        self._head.next = node
        self._head.next.next = cur
        self._size += 1

    def addAtTail(self, val):
        node = ListNode(val)
        cur = self._head.next
        # cur 指针运动到链表末尾
        while cur.next:
            cur = cur.next
        cur.next = node
        self._size += 1

    def addAtIndex(self, val, index):
        # 在链表中的第 index 个节点之前添加值为 val  的节点。
        # 如果 index 等于链表的长度，则该节点将附加到链表的末尾。
        # 如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。nt
        if index < 0:
            self.addAtHead(val)
        elif index > self._size:
            self.addAtTail(val)
        else:
            cur = ListNode(0)  # 虚拟节点
            new_node = ListNode(val)
            cur = self._head.next
            count = 1
            while count != index - 1:
                cur = cur.next
                count += 1
            new_node.next = cur.next
            cur.next = new_node

    def deleteAtIndex(self, index):
        # 如果索引 index 有效，则删除链表中的第 index 个节点。
        if index < 0 or index > self._size:
            return None
        count = 1
        cur = self._head.next
        while count != index - 1:
            # 将cur移动到第 index -1 点位置
            cur = cur.next
            count += 1
        # 删除第index位置的节点
        cur.next = cur.next.next


if __name__ == "__main__":
    vals = [1, 2, 6, 3, 4, 5, 6]
    # head = init_single(vals)
    # traversal(head)
    my_link = MyLinkedList()
    for val in vals:
        # 头插法
        my_link.addAtHead(val=val)
    my_link.addAtTail(val=10)
    my_link.addAtIndex('a',6) 
    node = my_link.get(5)
    print(node.val)
    my_link.deleteAtIndex(6)
    traversal(my_link._head)
