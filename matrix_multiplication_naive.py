import numpy
from collections import defaultdict


def mul(a, b):  # each matrix is a list of lists, eg [[1, 2], [3, 4]] is a 2*2 matrix
    c = defaultdict(list)

    if len(a[0]) != len(b):
        raise Exception('Matrices are not compatible.')

    for i in range(len(a)):
        a_row = a[i]
        for j in range(len(b)):
            b_col = [b_row[j] for b_row in b]
            c_elem = 0
            for k in range(len(a_row)):
                c_elem = c_elem + a_row[k]*b_col[k]
            c[i].append(c_elem)
    return c.values()


if __name__ == '__main__':
    print mul([[1,2], [3,4]], [[5,6], [7,8]])
    print numpy.dot([[1,2], [3,4]], [[5,6], [7,8]])