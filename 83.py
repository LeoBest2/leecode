#!/bin/python3
"""
    LeetCode 83.py
    ~~~~~
    @Description:
        给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

        示例 1:

        输入: 1->1->2
        输出: 1->2
        示例 2:

        输入: 1->1->2->3->3
        输出: 1->2->3

    @CreateTime: 2019/12/14 12:37
    @Author: leo
    @License: MIT
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list_to_node(li: [int]):
    ret = ListNode(None)
    ret_bak = ret
    for _ in li:
        ret.next = ListNode(_)
        ret = ret.next
    return ret_bak.next


def print_node(node: ListNode):
    while node is not None:
        print(node.val, end=' -> ')
        node = node.next
    print('')


def deleteDuplicates(head: ListNode) -> ListNode:
    head_bak = head
    while head and head.next is not None:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return head_bak


print_node(deleteDuplicates(list_to_node([1, 1, 2])))
print_node(deleteDuplicates(list_to_node([1, 1, 2, 3, 3])))
print_node(deleteDuplicates(list_to_node([1, 1, 1, 1, 1])))
