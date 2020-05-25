# https://www.lintcode.com/problem/subsets/description

# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.

# https://www.lintcode.com/problem/subsets/my-submissions?_from=ladder&&fromId=1
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        nums.sort()

        if nums is None:
            return []
        if not nums:
            return [[]]

        result = []

        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, start_id, curr_list, result):
        print(curr_list)
        result.append(list(curr_list))

        for i in range(start_id, len(nums)):
            curr_list.append(nums[i])
            self.dfs(nums, i + 1, curr_list, result)
            curr_list.pop()

    #     nums.sort()
    #     combinations = []
    #     self.dfs(nums, 0, [], combinations)
    #     return combinations

    # def dfs(self, nums, idx, combination, combinations):
    #     combinations.append(list(combination)) # 这里牵扯到一个copy问题，如果不加list，那么copy的就是combination的reference，因此list之后的改变都会导致之前加入值的改变，加上list()之后就是建立了一个当前combination的copy，之后无论list如何改变，就不变了

    #     for i in range(idx, len(nums)):
    #         combination.append(nums[i])
    #         self.dfs(nums, i + 1, combination, combinations)
    #         combination.pop()
