# https://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array/description?_from=ladder&&fromId=1
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin_v1(self, nums):
        # write your code here
        # BINARY SEARCH to the num which left neighbour is bigger than that number

        left, right = 0, len(nums) - 1
        rightMost = nums[-1]

        while left + 1 < right:
            mid = (left + right) // 2

            print(left, right, mid)
            if nums[mid] > rightMost:
                left = mid
            else:
                if nums[mid] > nums[mid - 1]:
                    right = mid
                else:
                    left = mid

        print(left, right)

        return min(nums[left], nums[right])

    def findMin_v2(self, nums):
        # compare with the right most
        if not nums:
            return -1
        rightmost = nums[-1]

        left, right = 0, len(nums) - 1
        while left + 1 > right:
            mid = (left + right) // 2
            if nums[mid] < rightmost:
                right = mid
            else:
                left = mid
        return min(nums[left], nums[right])
