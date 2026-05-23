class TrieNode:

    def __init__(self):
        self.children = dict()
        self.end_of_word = False



class PrefixTree:

    def __init__(self):
        self.trie = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.trie
        for i in range(len(word)):
            if not word[i] in curr.children:
                curr.children[word[i]] = TrieNode()
            curr = curr.children[word[i]]
        
        curr.end_of_word = True




    def search(self, word: str) -> bool:
        curr = self.trie
        for i in range(len(word)):
            if not word[i] in curr.children:
                return False
            curr = curr.children[word[i]]
        if curr.end_of_word:
            return True
        return False


        

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for i in range(len(prefix)):
            if not prefix[i] in curr.children:
                return False
            curr = curr.children[prefix[i]]
        return True
        
        