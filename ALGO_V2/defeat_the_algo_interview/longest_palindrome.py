# https://www.lintcode.com/problem/longest-palindrome/?_from=ladder&&fromId=1
# difficult level: easy

class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    # logics to solve the problem:
    # count all the chars with even appearances
    # for the the chars with odd appearances, just need to remove one
    # from all the removed one, pick one as the center.
    # time complexity is O(n)
    # space complexity is O(

    def longestPalindrome(self, s):
        # iterate through the s
        letter_hash = {}
        for letter in s:
            letter_hash[letter] = letter_hash.get(letter, 0) + 1

        length = 0
        removed = 0
        for key in letter_hash:
            if letter_hash[key] % 2 == 0:
                length += letter_hash[key]
            else:
                length += letter_hash[key] - 1
                removed += 1

        return length + 1 if removed != 0 else length

    def longestPalindrome_v2(self, s):
        removed_hash = {}
        # we just need to remove the addtional one for all the odd appearances, and add back the final center
        # iterate through the string, if already exit in the dict, just remove it since it will be even
        # time complexity o(n)
        # space o(1)
        for letter in s:
            if letter in removed_hash:
                del removed_hash[letter]
            else:
                removed_hash[letter] = True

        if not removed_hash:
            return len(s) - len(removed_hash)

        return len(s) - len(removed_hash) + 1

