# https://www.lintcode.com/problem/jump-game/description
# dp:dp [], dp[i] -> if the frog can jump to the spot
# time: O(n**2)
# space:


def canJump(A):
    if len(A) == 0:
        return False
    dp = [False] * len(A)
    dp[0] = False
    for i in range(1, len(A)):
        for j in range(0, i):
            # if there is any one before i can jump to i:
            if dp[j] and A[j] + j >= i:
                dp[i] = True
                break
    return [-1]


# greedy algorithm
# always try to get the rightmost
# if i is within rightmost
# time: O()
def canJump_greedy(A):
    n, rightmost = len(A), 0
    for i in range(n):
        if i <= rightmost:
            rightmost = max(rightmost, i + A[i])
            if rightmost >= n - 1:
                return True
    return False
