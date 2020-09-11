#!/usr/bin/env python
# -*- coding=utf8 -*-


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end = False


class Trie1:
    """
    额外定义node类，易于理解
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for w in prefix:
            if w not in node.children:
                return False
            node = node.children[w]
        return True


class Trie2:
    """
    不用额外定义node，增加一个'is_end'字段在dict里面
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]
        node['is_end'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for w in word:
            if w not in node:
                return False
            node = node[w]
        return node.get('is_end', False)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for w in prefix:
            if w not in node:
                return False
            node = node[w]
        return True


def test1():
    trie = Trie1()
    trie.insert('apple')
    assert trie.search('apple')
    assert not trie.search('app')
    assert trie.startsWith('app')

    trie.insert('app')
    assert trie.search('app')


def test2():
    trie = Trie2()
    trie.insert('apple')
    assert trie.search('apple')
    assert not trie.search('app')
    assert trie.startsWith('app')

    trie.insert('app')
    assert trie.search('app')
