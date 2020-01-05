class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.is_word_end = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = TrieNode('head')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie_node = self.tree
        for letter in word:
            if letter not in trie_node.children:
                trie_node.children[letter] = TrieNode(letter)
            trie_node = trie_node.children[letter]

        trie_node.is_word_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie_node = self.tree

        for letter in word:
            if letter not in trie_node.children:
                return False
            trie_node = trie_node.children[letter]

        return trie_node.is_word_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie_node = self.tree
        for letter in prefix:
            if letter not in trie_node.children:
                return False
            trie_node = trie_node.children[letter]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)