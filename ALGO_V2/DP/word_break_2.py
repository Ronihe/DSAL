# idea：
# s= s1+s2
# there are differnt ways to seperate the sentence




def workd_break_2(s, dict):
    return dfs(s, dict, {})


def dfs(s, dict, memo):
    print("memo---", memo)
    if s in memo:
        return memo[s]

    if len(s) == 0:
        return []

    partitions = []

    for i in range(1, len(s)):
        prefix = s[:i]

        print("prefix", prefix)
        if prefix not in dict:
            continue
        print("used---", prefix)
        sub_partition = dfs(s[i:], dict, memo)
        print("sub partition", sub_partition)
        for p in sub_partition:
            print("p--", prefix, p)
            partitions.append(prefix + " " + p)

    if s in dict:
        partitions.append(s)
    print("out", partitions)
    memo[s] = partitions
    print("memo", memo)
    return partitions


test = "lintcode"
dict = ["de", "ding", "co", "code", "lint"]

workd_break_2(test, dict)
