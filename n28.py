class Solution(object):
    def strStr(self, haystack, needle):

        a, q = len(needle), len(haystack)

        if a == 0:
            return a
        if q < a:
            return -1

        for i in range(q - a + 1):
            if haystack[i:i+a] == needle:
                return i
        return -1