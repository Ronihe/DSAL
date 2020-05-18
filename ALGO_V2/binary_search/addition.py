# 三步翻转法及相关练习题
# 矩阵找数问题的Follow up
# 快速幂算法
# 辗转相除法

# recover roated array
# [4,5,1,2,3]
# [4, 5] [1, 2, 3]
# [5, 4], [3,2,1]
# [1,2,3,4,5]
# https://www.lintcode.com/problem/recover-rotated-sorted-array/description

def recoverRotatedSortedArray(nums):
    # write your code here

    # find the place recover
    i = 1
    while 1 <= i < len(nums):
        if nums[i - 1] > nums[i]:
            break
        i += 1

    print((nums[:i][::-1] + nums[i:][::-1])[::-1])
    return -1

recoverRotatedSortedArray([4,5,1,2,3])

# 写法力求优美，用三段反转法，先用一个O(LogN)求最小值的辅助子程序，你要是用O(N)迭代法或Python的min函数就失分了。
#
# Reverse显然要单放一个函数。面试时可以最后实现。
#
# 三段反转法构成主程序，这要先在白板上写下来，目的是展示你的思维层次感。
#
# 最后，复杂度分析：O(LogN) + 2 * O(N)，和理论上的最低复杂度O(N)无限接近。
class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """

    def recoverRotatedSortedArray(self, nums):
        minIndex = self.findMinimum(nums)
        if minIndex == 0:
            return

        start, end = 0, len(nums) - 1
        self.rotateArray(nums, start, minIndex - 1)
        self.rotateArray(nums, minIndex, end)
        self.rotateArray(nums, start, end)

    """
    @param nums: An integer array
    @return: The index to the left most minimum element
    """

    def findMinimum(self, nums):
        if nums is None or len(nums) < 2:
            return 0

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right = right - 1

        return left

    # if there is repetitive numbers
    # 套用二分法 find min in RSA的前提条件是：没有重复数！这题目遇到 1 1 1 1 1 1 1 1 1 0 1 1 1 1，用二分法会找错地方.
    def find_split(self, nums):
        # DO NOT use binary search!
        # Binary Search does not work on this prob
        if nums is None or len(nums) < 2:
            return 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return i
                # return i = len()-1 if it's already a sorted array
        return i

    """
    @param nums: An integer array
    @param left: The start index into the array, inclusive
    @param right: The end index into the array, inclusive
    @return: nothing
    """

    def rotateArray(self, nums, left, right):
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# 算法课教程教的三步翻转。
# 注意！重要的事情说两遍：
# 找那个断点的地方不能用二分法！不要被楼上一些解答误导了！
# 找那个断点的地方不能用二分法！不要被楼上一些解答误导了！
# 套用二分法 find min in RSA的前提条件是：没有重复数！这题目遇到 1 1 1 1 1 1 1 1 1 0 1 1 1 1，用二分法会找错地方.
# 具体例题见find min in RSA II。
# 所以只能用打擂台！

