class ZigZag(object):

    def longestZigZag(self, sequence):
        states = []   # stores a tuple consisting of length of the longest sequence at that position and last diff type
        for i in range(len(sequence)):
            print i
            if i == 0:
                states.append((1, None))
            else:
                curr_state = (1, None)
                for j in range(i-1, -1, -1):
                    prev_state = states[j]
                    diff_type = prev_state[1]
                    if diff_type is None:
                        diff = sequence[i] - sequence[j]
                        if diff == 0:
                            break
                        elif diff > 0:
                            if curr_state[0] < 2:
                                curr_state = (2, 1)
                        else:
                            if curr_state[0] < 2:
                                curr_state = (2, -1)
                    else:
                        diff = sequence[i] - sequence[j]
                        if diff == 0:
                            break
                        elif diff_type == 1 and diff > 0:
                            if curr_state[0] == 1:
                                curr_state = (2, 1)
                        elif diff_type == -1 and diff < 0:
                            if curr_state[0] == 1:
                                curr_state = (2, -1)
                        else:
                            if curr_state[0] < prev_state[0] + 1:
                                curr_state = (prev_state[0] + 1, 1 if diff > 0 else -1)
                states.append(curr_state)

        biggest_state = None
        for state in states:
            if biggest_state is None:
                biggest_state = state
            else:
                if state[0] > biggest_state[0]:
                    biggest_state = state
        print states
        return biggest_state[0]

if __name__ == '__main__':
    print ZigZag().longestZigZag(( 374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 249, 22, 176, 279, 23, 22, 617, 462, 459, 244))

