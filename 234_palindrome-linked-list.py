#!/usr/bin/env python
# -*- coding=utf8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        利用栈“先进后出，后进先出”的特点，判断前半段和后半段是否相等。
        注意：需要判断奇偶两种场景，如果是奇数场景，中间数字需要从栈中先弹出，再开始判断。
        """
        if not head or not head.next:
            return True
        stack = []
        slow = fast = head
        stack.append(slow.val)
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            stack.append(slow.val)
            if not fast.next:
                stack.pop()
        while slow.next:
            if slow.next.val != stack.pop():
                return False
            slow = slow.next
        return True


def test1():
    s = Solution()
    a, b, c, d = ListNode(1), ListNode(2), ListNode(2), ListNode(1)
    a.next, b.next, c.next = b, c, d
    assert s.isPalindrome(a) == True

    a, b, c, d, e = ListNode(1), ListNode(
        2), ListNode(3), ListNode(2), ListNode(1)
    a.next, b.next, c.next, d.next = b, c, d, e
    assert s.isPalindrome(a) == True


def test2():
    s = Solution()
    e, f = ListNode(1), ListNode(2)
    e.next = f
    assert s.isPalindrome(e) == False

    e, f = ListNode(1), ListNode(1)
    e.next = f
    assert s.isPalindrome(e) == True

    e = ListNode(1)
    assert s.isPalindrome(e) == True
