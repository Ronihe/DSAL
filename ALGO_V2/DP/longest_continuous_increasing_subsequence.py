# iterate through the array, keep track of the longest incresing par and decreasing part
# we can use three var to keep track of them
# longest, curr_incre, curr_decre



class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """

    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        if not A:
            return 0

        longest, incre, decre = 1, 1, 1

        for i in range(1, len(A)):
            curr = A[i]
            last = A[i - 1]

            if last < curr:
                incre += 1
                decre = 1
            elif last > curr:
                incre = 1
                decre += 1
            else:
                incre = 1
                decre = 1
            longest = max(longest, max(incre, decre))

        return longest



