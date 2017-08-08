import string

CHAR_LIST = [i for i in string.ascii_lowercase]

class TrieNode(object):

    def __init__(self):
        self.child_node_refs = [None]*26
        self.is_leaf = False


class Trie(object):

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word):
        curr = self.head
        for c in word:
            node = curr.child_node_refs[CHAR_LIST.index(c.lower())]
            if not node:
                node = TrieNode()
                curr.child_node_refs[CHAR_LIST.index(c.lower())] = node
            curr = node

        curr.is_leaf = True

    def find(self, word):
        curr = self.head
        for c in word:
            node = curr.child_node_refs[CHAR_LIST.index(c.lower())]
            if node is None:
                return False

            curr = node

        if not curr.is_leaf:
            return False

        return True

if __name__ == '__main__':
     t = Trie()
     word = 'Rohan'
     t.insert('Rohan')
     t.insert('Rohini')
     t.insert('Roh')
     print t.find('Rohi')



