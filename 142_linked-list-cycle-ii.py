#!/usr/bin/env python
#-*- coding=utf8 -*-


class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    """
    参考题解141快慢指针判断是否有环

    假设head到环起始点距离x，环起始点距离相遇点y，相遇点到环起始点z
                  x                    y
    head ———————————————————> entry ————————> meet
                                |              |
                              z |              |
                                |<—————————————|
    相遇时：
    slow走过路程：x+y
    fast走过路程：x+y+z+y

    相同时间内，fast走的路程是slow的两倍：
    2(x+y) = x+y+z+y ===> x=z

    所以判断有环时，head和slow(此时在相遇点)同时出发，再次相遇时，即为环起始点
    """

    def detectCycle1(self, head: ListNode) -> ListNode:
        slow = fast = head
        has_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break

        if has_cycle:
            while head:
                if head == slow:
                    return head
                head = head.next
                slow = slow.next
        else:
            return


    def detectCycle2(self, head: ListNode) -> ListNode:
        """
        了解 while...else 用法:
        else只有在while判断为false时执行，如果break或exception时不执行
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return

        while head != slow:
            head = head.next
            slow = slow.next
        return head


def test1():
    s = Solution()
    a, b, c, d = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    a.next, b.next, c.next, d.next = b, c, d, b
    assert s.detectCycle1(a).val == 2
    
    
def test2():
    s = Solution()
    a, b,  = ListNode(1), ListNode(2)
    a.next, b.next = b, a
    assert s.detectCycle2(a).val == 1


def test3():
    s = Solution()
    a = ListNode(1)
    assert not s.detectCycle2(a)
