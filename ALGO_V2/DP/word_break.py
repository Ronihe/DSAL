# https://www.lintcode.com/problem/word-break/description

# dfs
class Solution:
    """
    time complexity:   n**n
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, dict):
        # write your code here
        # use dfs
        return self.dfs(s, 0, dict)

    def dfs(self, s, start_idx, dict):
        if start_idx == len(s):
            return True

        for word in dict:
            if start_idx + len(word) > len(s):
                continue

            if s[start_idx: start_idx + len(word)] == word:
                if self.dfs(s, start_idx + len(word), dict):
                    return True
        return False

# dfs + dp

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        return self.helper(0, s, wordDict, {})


    def helper(self, k, s, wordDict, cache):
        if k == len(s):
            return True
        elif k in cache:
            return cache[k]
        else:
            for i in range(k, len(s)):
                if s[k:i+1] in wordDict:
                    if self.helper(i+1, s, wordDict, cache):
                        cache[k] = True
                        return True
        cache[k] = False
        return cache[k]

    def dp(self, s, dict):
        n = len()





