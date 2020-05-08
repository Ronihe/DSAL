# https://www.lintcode.com/problem/valid-palindrome/description?_from=ladder&&fromId=1
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Have you consider that the string might be empty? This is a good question to ask during an interview.
# For the purpose of this problem, we define empty string as valid palindrome.

# example:
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama"

# Challenge
# O(n) time without extra memory.

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        if not s:
            return True

#         two pointers
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


s1 = "A man, a plan, a canal: Panama"
s2 = "1a2"
solution = Solution()
print(solution.isPalindrome(s1))

print(solution.isPalindrome(s2))


