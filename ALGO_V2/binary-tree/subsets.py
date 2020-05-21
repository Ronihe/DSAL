# https://www.lintcode.com/problem/subsets/description

def subset(nums):
    combinations = []
    dfs(nums, 0, [], combinations)
    return combinations


def dfs(nums, idx, combination, combinations):
    combinations.append(list(combination)) # 这里牵扯到一个copy问题，如果不加list，那么copy的就是combination的reference，因此list之后的改变都会导致之前加入值的改变，加上list()之后就是建立了一个当前combination的copy，之后无论list如何改变，就不变了

    for i in range(idx, len(nums)):
        combination.append(nums[i])
        dfs(nums, i + 1, combination, combinations)
        combination.pop()

test = [1,2,3]
r = subset(test)
print(r)