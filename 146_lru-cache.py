#!/usr/bin/env python
# -*- coding=utf8 -*-


class LRUCache1:
    """
    OrderedDict 内部由hash+双向链表实现
    """

    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value


class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache2:
    """
    手动实现哈希+双向链表
    最新使用移动到链表尾部，超出容量移除链表头部
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head, self.tail = ListNode(), ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 先移除
            node = self.cache[key]
            self._remove(node)

        node = ListNode(key, value)
        # 加入链表尾部
        self._add(node)
        # 刷新字典
        self.cache[key] = node

        # 加入后超出容量则移除
        if len(self.cache) > self.capacity:
            first_node = self.head.next
            self._remove(first_node)
            del self.cache[first_node.key]

    def _remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node: ListNode):
        """
        从尾部新增
        """
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node


def test1():
    cache = LRUCache1(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test2():
    cache = LRUCache2(2)
    cache.put(2, 0)
    cache.put(2, 1)
    cache.put(2, 2)
    assert cache.get(2) == 2
    cache.put(1, 1)
    cache.put(4, 1)
    assert cache.get(2) == -1
