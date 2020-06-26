
# question: array of integers, find the subway wth the max_sum
# greedy algorithm
# just need to get the sum of the sun array
# 1. max_sum to keep track the max of the subarray, sum to keep trck of the current array
# 2. init max_sum = interger.min_value, sum = 0
# 3. iterate through the array
#     - sum += element
#     - if sum > max_sum, update the max_sum
#     - if sum < 0, means the current sub_array is already negative, sum=0, to restart the sub_array
#       time complexity: O(n)
#       space complexity:   O(1)
#

# 
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        # prefix_sum记录前i个数的和，max_Sum记录全局最大值，min_Sum记录前i个数中0-k的最小值
        min_sum, max_sum = 0, -sys.maxsize
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)

        return max_sum
