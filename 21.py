#!/bin/python3
"""
    LeetCode 21.py
    ~~~~~
    @Description:
        将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

        示例：

        输入：1->2->4, 1->3->4
        输出：1->1->2->3->4->4

    @CreateTime: 2019/12/13 12:06 上午
    @Author: leo
    @License: MIT
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def list_to_ListNode(li: list) -> ListNode:
    head = ListNode(None)
    head_bak = head
    for _ in li:
        head.next = ListNode(_)
        head = head.next
    return head_bak.next


def listNodeToString(node):
    if node is None:
        print(None)
    while node is not None:
        print(node.val, end='->')
        node = node.next
    print('\n')


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    ret = ListNode(None)
    ret_bak = ret
    while l1 and l2 is not None:
        if l1.val > l2.val:
            ret.next = l2
            l2 = l2.next
        else:
            ret.next = l1
            l1 = l1.next
        ret = ret.next
    rest = l1 or l2
    while rest is not None:
        ret.next, ret, rest = rest, rest, rest.next
    return ret_bak.next


listNodeToString(mergeTwoLists(list_to_ListNode([1, 2, 4]), list_to_ListNode([1, 3, 4])))
listNodeToString(mergeTwoLists(list_to_ListNode([-9, 3]), list_to_ListNode([5, 7])))
