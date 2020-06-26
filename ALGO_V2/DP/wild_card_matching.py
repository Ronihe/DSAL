 # "?" can replace any single char
 # "*" can replace any chars

# idea:
# 1. if s == p: return true
# 2. if p = "*", return true
# 3. if p or s is empty, return false.

# iterate through s: if 


# dp[i][j] s the first i chars and first j chars are matching

def remove_dup_start(self,p):
    if p == "":
        return p
    