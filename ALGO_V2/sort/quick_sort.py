class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers2(self, A):
        # write your code here
        self.quickSort(A, 0, len(A) - 1)

    def quickSort(self, nums, start, end):
        if start >= end:
            return

        left, right = start, end
        mid = (start + end) // 2
        pivot = nums[mid]
        print("before", nums, left, right)
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        print("after", nums, left, right)
        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)



# Time complexity: nlogn
# worst case: n^2
# best case: n

