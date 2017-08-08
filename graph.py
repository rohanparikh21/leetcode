# Implements a Graph data structure using an adjacency list


class Graph(object):

    def __init__(self, v):
        self.num_of_vertices = v
        self.num_of_edges = 0
        self.adj_list = []
        for i in range(v):
            self.adj_list.append([])

    def V(self):
        """
        Returns the number of vertices.
        :return: int
        """
        return self.num_of_vertices

    def E(self):
        """
        Returns number of edges.
        :return:
        """
        return self.num_of_edges

    def addEdge(self, v, w):
        self.adj_list[v].append(w)
        self.adj_list[w].append(v)

    def adj(self, v):
        return self.adj_list[v]

    def toString(self):
        return ''


class GraphFromFile(Graph):

    def __init__(self, file_name):
        with file(file_name) as f:
            lines = f.readlines()
            v = int(lines[0].strip('\n'))
            super(GraphFromFile, self).__init__(v)
            self.num_of_edges = int(lines[1].strip('\n'))
            for i in range(2, len(lines)):
                vertices = lines[i].strip('\n').split(' ')
                self.addEdge(int(vertices[0]), int(vertices[1]))

if __name__ == '__main__':
    g = GraphFromFile('tinyG.txt')
    print g.num_of_edges
    print g.num_of_vertices
    for i in range(g.num_of_vertices):
        print g.adj(i)