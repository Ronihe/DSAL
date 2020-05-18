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


recoverRotatedSortedArray([4, 5, 1, 2, 3])


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


# https://www.lintcode.com/problem/rotate-string/description

# https://www.lintcode.com/problem/greatest-common-divisor/description
# 算法介绍
# 辗转相除法， 又名欧几里德算法， 是求最大公约数的一种方法。它的具体做法是：用较大的数除以较小的数，再用除数除以出现的余数（第一余数），再用第一余数除以出现的余数（第二余数），如此反复，直到最后余数是0为止。如果是求两个数的最大公约数，那么最后的除数就是这两个数的最大公约数。

def gcd(big, small):
    if small != 0:
        return gcd(small, big % small)
    else:
        return big


# 基本原理
# 计算x的n次方， 即计算x^nx
# n
#  。
#
# 由公式可知： x^n = x^{n/2} * x^{n/2}x
# n
#  =x
# n/2
#  ∗x
# n/2
#  。
#
# 如果我们求得x^{n/2}x
# n/2
#  ， 则可以O(1)求出x^nx
# n
#  , 而不需要再去循环剩下的n/2n/2次。
#
# 以此类推，若求得x^{n/4}x
# n/4
#  ， 则可以O(1)求出x^{n/2}x
# n/2
#  。
# 。。。
#
# 因此一个原本O(n)O(n)的问题，我们可以用O(logn)O(logn)复杂度的算法来解决。

def power(x, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        tmp = power(x, n // 2)
        return tmp * tmp
    else:
        tmp = power(x, n // 2)
        return tmp * tmp * x


# 注意:
#
# 不要重复计算，在计算x^{n/2} * x^{n/2}x
# n/2
#  ∗x
# n/2
#  的时候，先计算出x^{n/2}x
# n/2
#  ，存下来然后返回tmp*tmptmp∗tmp;
# nn为奇数的时候要记得再乘上一个xx。

# 非递归版本
def power(x, n):
    ans = 1
    base = x
    while n > 0:
        if n % 2 == 1:
            ans *= base
        base *= base
        n = n // 2
    return ans

# 非递归版本与递归版本原理相同，计算顺序略有不同。
#
# 因为递归是从大问题进入，划分子问题然后层层返回再求解大问题。这里要从小问题开始，直接求解大问题。
# 你可以打印出每次循环中 basebase 和 ansans 的值，来理清楚其中的算法思路。
#
# 递归版本和非递归版本都应该熟练掌握，虽然递归版本更容易掌握和理解，且 lognlogn 的计算深度也不会导致 Stack Overflow。但是面试官是很有可能为了加大难度让你在用非递归的版本写一遍的。
