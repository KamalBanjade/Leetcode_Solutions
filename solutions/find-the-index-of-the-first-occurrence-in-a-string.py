class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        n = len(needle)
        for i in range(len(haystack)-n+1):
            if haystack[i:i+n]==needle:
                return i
        return -1
        