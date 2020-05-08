# https://www.lintcode.com/problem/implement-strstr/description?_from=ladder&&fromId=1
#  For a given source string and a target string, you should output the first index(from 0) of target string in source string.

class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """

    def strStr(self, source, target):
        # Write your code here
        if len(target) > len(source):
            return -1

        # loop to compare by chunks
        # Attention to the additional +1 here
        for i in range(len(source) - len(target) + 1):
            if target == source[i: (i + len(target))]:
                return True
        return False
