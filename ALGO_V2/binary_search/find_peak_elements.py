
# https://www.lintcode.com/problem/find-peak-element/description?_from=ladder&&fromId=1
# 这个题 LintCode 和 LeetCode 的 find peak element 是有区别的。
# 数据上，LintCode 保证数据第一个数比第二个数小，倒数第一个数比到倒数第二个数小。
# 因此 start, end 的范围要取 1, len(A) - 2
#
# 二分法。
# 每次取中间元素，如果大于左右，则这就是peek。
# 否则取大的一边，两个都大，可以随便取一边。最终会找到peek。

# 正确性证明：
#
# A[0] < A[1] && A[n-2] > A[n-1] 所以一定存在一个peek元素。
# 二分时，选择大的一边, 则留下的部分仍然满足1 的条件，即最两边的元素都小于相邻的元素。所以仍然必然存在peek。
# 二分至区间足够小，长度为3, 则中间元素就是peek。

# compare left and right same time, can just return
class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        # write your code here

        # compare with left and right
        start, end = 1, len(A) - 2
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < A[mid - 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid
            else:
                return mid

        print(start, end)
        if A[start] > A[end]:
            return start

        return end