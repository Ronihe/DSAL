# https://leetcode.com/problems/longest-palindromic-substring/
# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
# Input: "cbbd"
# Output: "bb"

# logics: find the center of palindrom, and expand to the two sides
def longestPalindrome(s):
    """
    time complexity:O(n^2)
    space complexity: O(n) since it created s substrings
    """
    # edge cases:
    if not s:
        return ""

    # core logics: iterable through the string
    longest = ""
    for mid in range(len(s)):
        substring = find_palindrome_from(s, mid, mid)
        # print(substring)
        if len(substring) > len(longest):
            longest = substring

    # space between core logics and return value
    return longest


def find_palindrome_from(s, left, right):
    # passed left and right are both center of the
    while left >= 0 and right < len(s):
        #print(s[left], s[right])
        if s[left] != s[right]:
            break
        left -= 1
        right += 1

    # be careful about the last left and right
    palindrome_str = s[left+1: right]
    return palindrome_str if len(palindrome_str) != 1 else ""


# test cases:
s1 = "ababbb"
s2 = "ahdllfjaksfljadlao3uhfdjbskjlcvughjb,mndakjslaflajsdflkd"
print(longestPalindrome(s1))
print(longestPalindrome(s2))
