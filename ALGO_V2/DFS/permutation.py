
# https://www.lintcode.com/problem/permutations/description?_from=ladder&&fromId=1
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        if not nums:
            return [[]]

        permutations = []
        self.dfs(nums, [], set(), permutations)
        return permutations

    def dfs(self, nums, permutation, visited, permutations):
        print(visited, permutations)
        if len(nums) == len(permutation):
            permutations.append(list(permutation))
            return
        for i, num in enumerate(nums):
            if i in visited:
                continue

            permutation.append(num)
            visited.add(i)
            self.dfs(nums, permutation, visited, permutations)
            visited.remove(i)
            permutation.pop()


