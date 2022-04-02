class TrieNode():
    def __init__(self) -> None:
        self.children = {}
        self.char = None
        self.end = False

class Trie():
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word : str) -> None:
        curr : TrieNode = self.root

        for character in word : 
            if not curr.children.__contains__(character):
                new_node = TrieNode()
                new_node.char = character
                curr.children[character] = new_node

            curr = curr.children[character]        
        curr.end = True

    def search(self, word : str) -> bool:
        curr : TrieNode = self.root
        
        for character in word:
            if not curr.children.__contains__(character):
                return False
            curr = curr.children[character]
        return curr.end

    def starts_with(self, prefix : str) -> None:
        curr : TrieNode = self.root
        
        for character in prefix:
            if not curr.children.__contains__(character):
                return False
            curr = curr.children[character]
        return True

trie = Trie()        
trie.insert("hell")

print(trie.search("hel"))
print(trie.starts_with("he"))
print(trie.starts_with("hellp"))