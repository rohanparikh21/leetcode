from copy import copy

def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    dp = []
    dp.append([[]])
    for index in range(1, len(nums) + 1):
        new_sets = []
        prev_sets = dp[index - 1]
        num = nums[index - 1]
        print 'num:' + str(num)
        for s in prev_sets:
            new_s = copy(s)
            print 'new_s:' + str(new_s)
            new_s.append(num)
            print 'new_s:' + str(new_s)
            new_sets.append(new_s)
        print 'new_sets:' + str(new_sets)
        dp.append(prev_sets + new_sets)
    return dp[len(nums)]


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    dp = [[[]]]
    for i in range(1, len(nums)+1):
        new_permutations = []
        prev_permutations = dp[i-1]
        for pp in prev_permutations:
            for j in range(len(pp)+1):
                print j
                temp = pp[:j] + [nums[i-1]] + pp[j:]
                print temp
                new_permutations.append(temp)
        dp.append(new_permutations)
    return dp[-1]


def permute(chars):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    dp = [['']]
    for i in range(1, len(chars)+1):
        new_permutations = []
        prev_permutations = dp[i-1]
        for pp in prev_permutations:
            for j in range(len(pp)+1):
                temp = list(pp[:j]) + [chars[i-1]] + list(pp[j:])
                new_permutations.append(''.join(temp))
        dp.append(new_permutations)
    return dp[-1]


def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def longest_palindrome_substring(s):
    len_s = len(s)
    max_sub_str_len = 0
    for i in range(len_s):
        for j in range(i, len_s):
            sub_str_len = len(s[i:j])
            if is_palindrome(s[i:j]):
                max_sub_str_len = max(max_sub_str_len, sub_str_len)
    return max_sub_str_len


def longest_palindrome_substring_dp(s):
    len_s = len(s)
    dp = [[0 for _ in range(len_s)] for _ in range(len_s)]

    for i in range(len_s):
        dp[i][i] = 1

    max_sub_str = 1
    for i in range(len_s - 1):
        j = i+1
        if s[i] == s[j]:
            dp[i][j] = True
            max_sub_str = 2

    for k in range(3, len_s):
        for i in range(len_s-3):
            j = i + k - 1
            if j<len_s and dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] = True
                max_sub_str = max(max_sub_str, k)
    return max_sub_str


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    for bracket in s:
        if bracket in opening_brackets:
            stack.append(bracket)
        else:
            prev_bracket = stack[-1]
            print closing_brackets[opening_brackets.index(prev_bracket)]
            if prev_bracket and bracket == closing_brackets[opening_brackets.index(prev_bracket)]:
                print closing_brackets[opening_brackets.index(prev_bracket)]
                del stack[-1]
                print stack
            else:
                return False
    print stack
    return not len(stack) > 0

if __name__ == '__main__':
    print isValid('[]')