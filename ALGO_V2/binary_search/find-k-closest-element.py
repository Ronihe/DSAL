# https://www.lintcode.com/problem/find-k-closest-elements/description?_from=ladder&&fromId=1

# logics: using binary seach to get the smallest number and two pointer to left and right to get the next cloeset number

# Given a target number, a non-negative integer target and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.
# Given A = [1, 2, 3], target = 2 and k = 3, return [2, 1, 3].
# Given A = [1, 4, 6, 8], target = 3 and k = 3, return [4, 1, 6].

# 二分法 和 双指针
# 二分法：确定位置： 找到一个最小大于左侧 < target, 右侧 >= target,
# 双指针 从两边走起: left = right - 1

# Note: if left < 0, so need to always check the

def kCloestNumbers(A, target, k):
    #     because k element, we can just use range

    right = findUpperCloset(A, target)
    left = right - 1

    result = []
    for _ in range(k):
        if isLeftCloser(A, left, right):
            result.append(A[left])
            left -= 1
        else:
            result.append(A[right])
            right += 1
    return result


def findUpperCloset(A, target):
    # find the first right nummber  >= target with binary search
    left, right = 0, len(A) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if A[mid] >= target:
            right = mid
        else:
            left = mid
    #     because it is ascending
    if A[left] >= target:
        return left
    if A[right] >= target:
        return right

    return len(A)


def isLeftCloser(A, left, right):
    if left < 0:
        return False
    if right >= len(A):
        return True
    return target - A[left] <= A[right] - target
