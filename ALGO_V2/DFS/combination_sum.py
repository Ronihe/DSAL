
# https://leetcode.com/problems/combination-sum/

# my solution
class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """

    def combinationSum2(self, num, target):
        # write your code here
        result = []
        num.sort()
        self.dfs(num, 0, [], result, target)
        return result

    def dfs(self, num, start_id, curr_list, result, target):

        if target == 0:
            result.append(list(curr_list))
            return

        if start_id >= len(num) or num[start_id] > target:
            return

        for i in range(start_id, len(num)):
            if i > start_id and num[i] == num[i-1]:
                continue

            curr_list.append(num[i])

            self.dfs(num, i + 1, curr_list, result, target - num[i])
            curr_list.pop()
