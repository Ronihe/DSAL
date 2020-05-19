
# https://www.lintcode.com/problem/search-in-a-big-sorted-array/description?_from=ladder&&fromId=1

#  a big sorted array with non-negative integers
# 给一个按照升序排序的非负整数数组。这个数组很大以至于你只能通过固定的接口 ArrayReader.get(k) 来访问第k个数(或者C++里是ArrayReader->get(k))，并且你也没有办法得知这个数组有多大。
# 找到给出的整数target第一次出现的位置。你的算法需要在O(logk)的时间复杂度内完成，k为target第一次出现的位置的下标。


class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """

    def searchBigSortedArray(self, reader, target):
        # write your code here
        # find the first number > target
        # search from idx/2 - index/2

        kth = 1
        while reader.get(kth - 1) < target:
            kth = kth * 2

        left = int((kth / 2) - 1) #note to change the type to int
        right = kth - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if reader.get(mid) > target:
                # move to the left
                right = mid
            else:
                right = mid

        if reader.get(left) == target:
            return left
        if reader.get(right) == target:
            return right

        return -1
