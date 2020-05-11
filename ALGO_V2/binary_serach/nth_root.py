# https://leetcode.com/problems/sqrtx/

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# binary search
# time: logx
# space 1

def mySqrt(x):
    left = 1
    right = x

    while left <= right:
        middle = (left + right) // 2

        if middle ** 2 > x:
            right = middle - 1
        elif middle ** 2 < x:
            left = middle + 1
        else:
            return middle
    # left > right
    return right


# modified ;
# input x, nth root,
# output should be less than 0.001 difference

def myNthRoot(x, n):
    # x, n both non-negative int
    # 0.64  2  -> 0.8
    #  assume both > 1
    DIFF = 0.001
    left = 0
    right = x

    while left <= right:
        mid = (left + right) / 2
        print(left, right, mid)
        if mid ** n < x:
            # move to the right
            left = mid + DIFF
        elif mid ** n > x:
            # move to the left
            right = mid -DIFF
        else:
            return mid

    return right

test = myNthRoot(9, 5)
print(9**(1/5))
print(test)
