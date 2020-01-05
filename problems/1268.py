class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.possible_words = []


class Trie:
    def __init__(self):
        self.trie = TrieNode('head')

    def add_word(self, word):
        trie = self.trie
        for char in word:
            if char in trie.children:
                trie = trie.children[char]
            else:
                trie.children[char] = TrieNode(char)
                trie = trie.children[char]
            if len(trie.possible_words) < 3:
                trie.possible_words.append(word)

    def get_suggestions(self, word):
        trie = self.trie
        for char in word:
            if char in trie.children:
                trie = trie.children[char]
            else:
                return []
        return trie.possible_words


class Solution:
    def suggestedProducts(self, products, searchWord):
        trie = Trie()
        products.sort()
        for word in products:
            trie.add_word(word)

        current_word = ''
        result = []
        for char in searchWord:
            current_word += char
            result.append(trie.get_suggestions(current_word))

        return result