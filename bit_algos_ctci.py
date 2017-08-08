def problem1(n, m, i, j):
    mask1 = ~0
    mask1 <<= (j+1)

    mask2 = 1 << i
    mask2 -= 1

    mask = mask1 | mask2
    n &= mask
    return n | m << 1


def flip_bit_to_win(num):
    num_bit_arr = []
    for i in range(32):
        b = num & 1
        num_bit_arr.append(b)
        num >>= 1

    bit_sequences = [0]
    for b in num_bit_arr:
        if len(bit_sequences) % 2 == 0:
            if b == 1:
                temp_v = bit_sequences[-1]
                temp_v += 1
                bit_sequences[-1] = temp_v
            else:
                bit_sequences.append(1)
        else:
            if b == 0:
                temp_v = bit_sequences[-1]
                temp_v += 1
                bit_sequences[-1] = temp_v
            else:
                bit_sequences.append(1)

    max_seq = 0
    for i in range(0, len(bit_sequences), 2):
        zero_right_seq = 0
        zero_left_seq = 0
        zero_seq = bit_sequences[i]
        if i-1 > 0:
            zero_left_seq = bit_sequences[i-1]
        if i+1 < len(bit_sequences):
            zero_right_seq = bit_sequences[i+1]

        this_seq = 0
        if zero_seq == 1:
            this_seq = zero_left_seq + this_seq + zero_right_seq
        else:
            this_seq = 1 + max(zero_left_seq, zero_right_seq)

        max_seq = max(this_seq, max_seq)

    return max_seq


def hamming_weight(n):
    cnt = 0
    for i in range(32):
        if n & (1 << 0):
            cnt += 1
        n >>= 1
    return cnt


if __name__ == '__main__':
    print hamming_weight(int('0b000000011100', 2))



