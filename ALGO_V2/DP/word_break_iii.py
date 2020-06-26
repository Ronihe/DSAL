# https://www.lintcode.com/problem/word-break-iii/description?_from=ladder&&fromId=1
#

# input: sentence without space and list of words, case is ignored
# output: how many ways the sentences can be formed formed from the list

# Idea:
# s sentence and be seperated as s1 and s2
# so the ways can be (the ways to get s1) * (the ways to get s2)

# dp[i][j] =


def word_break3(s, dict):
    if not s or not dict:
        return 0

    n, hash = len(s), set()
    lowerS = s.lower()
    for d in dict:
        hash.add(d.lower())

    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            sub = lowerS[i:j + 1]
            if sub in hash:
                dp[i][j] = 1

    for i in range(n):
        for j in range(i, n):
            for k in range(i, j):
                dp[i][j] += dp[i][k] * dp[k + 1][j]

    print(dp)

    return dp[0][-1]


test = "CatMat"
dict = ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]

count = word_break3(test, dict)
print(count)
