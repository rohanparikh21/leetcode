# Implementation of an algorithm to find connected components using DFS
from graph import GraphFromFile


class CC(object):

    def __init__(self, g):
        self.g = g
        self.marked = {}
        self.component = {}
        self.count = 0
        for i in range(self.g.V()):
            self.marked[i] = False
            self.component[i] = None
        for v in range(self.g.V()):
            if not self.marked[v]:
                self._dfs(v)
                self.count += 1

    def _dfs(self, v):
        for pair in self.g.adj_list[v]:
            if not self.marked.get(pair):
                self.marked[pair] = True
                self.component[pair] = self.count
                self._dfs(pair)

    def connected(self, v, w):
        return bool(self.component[v] == self.component[w])

    def count(self):
        return self.count

    def id(self, v):
        return self.component[v]

if __name__ == '__main__':
    cc = CC(GraphFromFile('tinyG.txt'))
    print cc.count

