
# https://www.lintcode.com/problem/partition-array/description?_from=ladder&&fromId=1
# https://www.jiuzhang.com/solution/partition-array/

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """

    # 只需要将小的不停的向前

    def partitionArray(self, nums, k):
        # write your code here
        if not nums:
            return 0

        left, right = 0, len(nums) - 1

        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        print(nums)
        return right + 1