import sys
class recursionlimit:
    def __init__(self, limit):
        self.limit = limit
        self.old_limit = sys.getrecursionlimit()

    def __enter__(self):
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)

class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        """
        @param: word: a word
        @return: nothing
        """
        def dfs(start, trie):
            if start == len(word):
                trie[''] = {}
                return
            ch = word[start]
            if ch not in trie:
                trie[ch] = {}
            dfs(start+1, trie[ch])

        dfs(0, self.trie)

    def search(self, word):
        """
        @param: word: A string
        @return: if the word is in the trie.
        """
        def helper(start, trie):
            if start == len(word):
                return '' in trie
            ch = word[start]
            if ch not in trie:
                return False
            return helper(start+1, trie[ch])

        return helper(0, self.trie)

    def startsWith(self, prefix):
        """
        @param: prefix: A string
        @return: if there is any word in the trie that starts with the given prefix.
        """
        def helper(start, trie):
            if start == len(prefix):
                return True
            ch = prefix[start]
            if ch not in trie:
                return False
            return helper(start+1, trie[ch])

        return helper(0, self.trie)

if __name__ =="__main__":

    with recursionlimit(2500):
        s = Trie()
        s.insert("aaa")
        s.insert("aaaz")
        print s.search("aaa")
