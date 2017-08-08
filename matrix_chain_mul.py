def matrix_chain_mul(*args):     # don't know the number of matrices to be passed
    rows_cols_tup = []
    for arg in args:
        num_rows = len(arg)
        num_cols = len(arg[0])
        rows_cols_tup.append((num_rows, num_cols))

    dp_table = []
    for i in range(len(args)):
        arr = [float('inf')]*i if i > 0 else []
        arr.append(0)
        arr.extend([float('inf')]*(len(args)-(i+1)))
        dp_table.append(arr)

    for chain_len in range(1, len(args)):
        for i in range(0, len(args)-chain_len):
            j=i+chain_len
            for cut in range(i,j):
                q = dp_table[i][cut] + dp_table[cut+1][j] + \
                    rows_cols_tup[i][0]*rows_cols_tup[cut][1]*rows_cols_tup[j][1]
                if q < dp_table[i][j]:
                    dp_table[i][j] = q

    print dp_table


if __name__ == '__main__':
    matrix_chain_mul([[1]*35]*30, [[1]*15]*35, [[1]*5]*15, [[1]*10]*5)



