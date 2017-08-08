class DirectedEdge(object):

    def __init__(self, v, w, weight):
        self._from = v
        self._to = w
        self._weight = weight

    @ property
    def weight(self):
        return self._weight

    @property
    def from_(self):
        return self._from

    @property
    def to(self):
        return self._to

    def __repr__(self):
        return "[{0}-{1}->{2}]".format(self._from, self._weight, self._to)


