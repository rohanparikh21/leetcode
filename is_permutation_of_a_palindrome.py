from collections import defaultdict


def is_permutation_of_a_palindrome(s):
    count_dict = defaultdict(int)
    for i in range(len(s)):
        count_dict[s[i].lower()] += 1

    set_vs = set(count_dict.values())
    print count_dict
    if len(set_vs) == 2 and 1 in set_vs:
        return True
    else:
        return False


if __name__ == '__main__':
    print is_permutation_of_a_palindrome("Tact Coa")