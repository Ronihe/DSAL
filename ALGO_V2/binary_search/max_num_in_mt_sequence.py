
# https://www.lintcode.com/problem/maximum-number-in-mountain-sequence/description?_from=ladder&&fromId=1
# Input: nums = [1, 2, 4, 8, 6, 3]
# Output: 8

# logics: the max num > list[num+1]

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """

    def mountainSequence(self, nums):
        # write your code here

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid
        return max(nums[left], nums[right])


