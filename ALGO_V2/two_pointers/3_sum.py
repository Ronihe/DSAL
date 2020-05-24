
# https://www.lintcode.com/problem/3sum/description?_from=ladder&&fromId=1

def three_Sum(nums):
    # sort nlong(n)
    nums.sort()
    result = []
    length = len(nums)
    for i in range(0, length-2):

        if i > 0 and nums[i] == nums[i-1]:
            continue
        find_two_sum(nums, i+1, length-1, -nums[i], result)
    return result

def find_two_sum(self, nums, left, right, target, results):
    while left < right:
        if nums[left] + nums[right] == target:
            results.append([-target, nums[left], nums[right]])
            right -= 1
            left += 1
            while left < right and nums[left] == nums[left-1]:
                left += 1
            while left < right and nums[right] == nums[right+1]:
                right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1


# time: N ^ 2



