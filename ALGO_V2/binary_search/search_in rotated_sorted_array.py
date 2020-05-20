# https://www.lintcode.com/problem/search-in-rotated-sorted-array/description?_from=ladder&&fromId=1

class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """

    def search(self, A, target):
        # write your code here
        if not A:
            return -1

        left, right = 0, len(A) - 1
        while left + 1 < right:
            # just need to compare with the most left
            mid = (left + right) // 2

            if A[mid] > A[left]:
                if A[left] <= target <= A[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if A[left] >= target >= A[mid]:
                    left = mid
                else:
                    right = mid

        if A[left] == target:
            return left
        if A[right] == target:
            return right
        return -1

    def search_twice(self, A, target):
        if not A:
            return -1
        smalles_idx = self.find_smallest_idx(A)
        if A[smalles_idx] <= target <= A[-1]:
            return self.binary_search(A, smalles_idx, len(A) - 1, target)
        return self.binary_search(A, 0, smalles_idx, target)

    # find the smallest idx
    def find_smallest_idx(self, A):
        #     keep moving to the right , until the left is mid is smaller than the right
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] > A[right]:
                left = mid
            else:
                right = mid
        if A[left] > A[right]:
            return right
        return left

    def binary_search(self, A, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            return start
        if A[start] == target:
            return end
        return -1
