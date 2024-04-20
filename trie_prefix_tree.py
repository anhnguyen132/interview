class TrieNode:
    def __init__(self, character=None):
        # self.character = character # Don't need this bc each node is linked to a key containing the character in the CHILDREN hash map
        self.children = {}
        self.isEndofWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word to the trie
        """
        if word == "":
            return

        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.isEndofWord = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie
        """
        if word == "":
            return True

        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        if curr.isEndofWord:
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts with prefix
        """
        if prefix == "":
            return True

        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True


def main():

    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any", "by", "their"]
    output = ["Not present in trie", "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}. Expect: Present ".format("the", output[t.search("the")]))
    print("{} ---- {}. Expect: Not present ".format("these", output[t.search("these")]))
    print("{} ---- {}. Expect: Present".format("their", output[t.search("their")]))
    print("{} ---- {}. Expect: Not present".format("thaw", output[t.search("thaw")]))

    # Search for words with prefix
    print(
        "Prefix {} ---- {}. Expect: Present".format("the", output[t.startsWith("the")])
    )
    print(
        "Prefix {} ---- {}. Expect: Present".format(
            "thei", output[t.startsWith("thei")]
        )
    )
    print("Prefix {} ---- {}. Expect: Present".format("an", output[t.startsWith("an")]))
    print("Prefix {} ---- {}. Expect: Present".format("", output[t.startsWith("")]))
    print(
        "Prefix {} ---- {}. Expect: Present".format("any", output[t.startsWith("any")])
    )
    print("Prefix {} ---- {}. Expect: Present".format("b", output[t.startsWith("b")]))

    print(
        "Prefix {} ---- {}. Expect: Not present".format(
            "bi", output[t.startsWith("bi")]
        )
    )
    print(
        "Prefix {} ---- {}. Expect: Not present".format(
            "anti", output[t.startsWith("anti")]
        )
    )
    print(
        "Prefix {} ---- {}. Expect: Not present".format(
            "do", output[t.startsWith("do")]
        )
    )


if __name__ == "__main__":
    main()
