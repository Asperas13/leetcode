from math import log2


class TrieNode:
    def __init__(self):
        self.associated_value = None
        self.children = {}


class Trie:
    def __init__(self):
        self.trie_head = TrieNode()

    def add_word(self, word, val):
        trie = self.trie_head
        for ch in word:
            if ch not in trie.children:
                trie.children[ch] = TrieNode()

            trie = trie.children[ch]

        trie.associated_value = val

    def search(self, word, val):
        trie = self.trie_head
        for ch in word:
            if ch == 0:
                if trie.children.get(1):
                    trie = trie.children[1]
                else:
                    trie = trie.children[0]
            else:
                if trie.children.get(0):
                    trie = trie.children[0]
                else:
                    trie = trie.children[1]
        if trie.associated_value:
            return val ^ trie.associated_value
        return 0


def calculate_binary(num, max_depth):
    binary = []
    while num > 0:
        binary.append(num % 2)
        num //= 2

    if len(binary) < max_depth:
        binary = [0] * (max_depth - len(binary)) + binary

    return binary


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        max_xor = 0
        max_depth = round(log2(max(nums))) + 1
        nums = {num: calculate_binary(num, max_depth) for num in nums}
        trie = Trie()
        for num, binary in nums.items():
            print(num, binary)
            trie.add_word(binary, num)

        for num, binary in nums.items():
            max_xor = max(max_xor, trie.search(binary, num))

        return max_xor


