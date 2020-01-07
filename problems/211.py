class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.is_word_end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_head = TrieNode("head")

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        trie = self.trie_head
        for letter in word:
            if letter not in trie.children:
                trie.children[letter] = TrieNode(letter)
            trie = trie.children[letter]

        trie.is_word_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def _search(trie_node, i):
            if i >= len(word):
                if trie_node and trie_node.is_word_end:
                    return True
                return False

            if word[i] != '.':
                if word[i] not in trie_node.children:
                    return False
                return _search(trie_node.children[word[i]], i + 1)
            else:
                for child_node in trie_node.children.values():
                    if _search(child_node, i + 1):
                        return True

                return False

        return _search(self.trie_head, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)