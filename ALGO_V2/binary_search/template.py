# template

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        # 用 start + 1 < end 而不是 start < end 的目的是为了避免死循环
        # 在 first position of target 的情况下不会出现死循环
        # 但是在 last position of target 的情况下会出现死循环
        # 样例：nums=[1，1] target = 1
        # 为了统一模板，我们就都采用 start + 1 < end，就保证不会出现死循环
        while start + 1 < end:
            # python 没有 overflow 的问题，直接 // 2 就可以了
            # java和C++ 最好写成 mid = start + (end - start) / 2
            # 防止在 start = 2^31 - 1, end = 2^31 - 1 的情况下出现加法 overflow
            mid = (start + end) // 2

            # > , =, < 的逻辑先分开写，然后在看看 = 的情况是否能合并到其他分支里
            if nums[mid] < target:
                # 写作 start = mid + 1 也是正确的
                # 只是可以偷懒不写，因为不写也没问题，不会影响时间复杂度
                # 不写的好处是，万一你不小心写成了 mid - 1 你就错了
                start = mid
            elif nums[mid] == target:
                end = mid
            else:
                # 写作 end = mid - 1 也是正确的
                # 只是可以偷懒不写，因为不写也没问题，不会影响时间复杂度
                # 不写的好处是，万一你不小心写成了 mid + 1 你就错了
                end = mid

        # 因为上面的循环退出条件是 start + 1 < end
        # 因此这里循环结束的时候，start 和 end 的关系是相邻关系（1和2，3和4这种）
        # 因此需要再单独判断 start 和 end 这两个数谁是我们要的答案
        # 如果是找 first position of target 就先看 start，否则就先看 end
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1


# Q: 为什么要用 start + 1 < end？而不是 start < end 或者 start <= end？
#
# A: 为了避免死循环。二分法的模板中，整个程序架构分为两个部分：
#
# 通过 while 循环，将区间范围从 n 缩小到 2 （只有 start 和 end 两个点）。
# 在 start 和 end 中判断是否有解。
# start < end 或者 start <= end 在寻找目标最后一次出现的位置的时候，出现死循环。
#
# Q: 为什么明明可以 start = mid + 1 偏偏要写成 start = mid?
#
# A: 大部分时候，mid 是可以 +1 和 -1 的。在一些特殊情况下，比如寻找目标的最后一次出现的位置时，当 target 与 nums[mid] 相等的时候，是不能够使用 mid + 1 或者 mid - 1 的。因为会导致漏掉解。那么为了节省脑力，统一写成 start = mid / end = mid 并不会造成任何解的丢失，并且也不会损失效率——log(n) 和 log(n+1) 没有区别。

# https://www.lintcode.com/problem/last-position-of-target/description
def lastPosition(nums, target):
    if not nums or target is None:
        return -1

    start, end = 0, len(nums) - 1
    while start + 1 < end:
        print("start", start, "end", end)
        mid = (start + end) // 2
        if nums[mid] > target:
            # move left
            end = mid
        elif nums[mid] < target:
            # move to the right
            start = mid
        else:
            start = mid

    if nums[end] == target:
        return end
    elif nums[start] == target:
        return start
    return -1

r = lastPosition([], None)
print(r)

# 在做 last position of target 这种模型下的二分法时，使用 while (start < end) 就容易出现超时。
# start, end = 0, len(nums) - 1
# while start <end:
#     mid = start + (end - start) // 2
#     if nums[mid] == target:
#         start = mid
#     else if nums[mid] < target:
#         start = mid + 1
#     else:
#         end = mid - 1

# example: nums = [1,1], target = 1









