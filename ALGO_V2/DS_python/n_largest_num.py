# find the k largest number
import heapq


def top_k(nums, k):
    '''

    Args:
        nums: list of numbers
        k: num

    Returns:

    '''
    top_k_nums = heapq.nlargest(k, nums)
    print(top_k_nums)
    return top_k_nums


def quick_top_k(nums, k):
    quick_select(nums, 0, len(nums) - 1, k)
    print(nums)


def quick_select(nums, left, right, k):
    print(left, right)
    pivot = nums[int((left + right) / 2)]

    print("the pivot", pivot)
    i, j = left, right
    while i <= j:
        while i <= j and nums[i] > pivot:
            i += 1
        while i <= j and nums[j] < pivot:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    print(i, j, nums)

    if i == k:
        return
    if i > k:
        quick_select(nums, left, j, k)
    else:
        quick_select(nums, i, right, k)


test_case = [3, 10, 1000, -99, 4, 100]
k = 3
# top_k(test_case, k)
quick_top_k(test_case, k)
