class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_s = ''
        words = s.split(' ')
        for word in words:
            reverse_word = ''.join(list(reversed(list(word))))
            if new_s:
                new_s = new_s + ' ' + reverse_word
            else:
                new_s = new_s + reverse_word
        return new_s