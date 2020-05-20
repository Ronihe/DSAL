# https://www.lintcode.com/problem/powx-n/description?_from=ladder&&fromId=1
# Implement pow(x, n). (n is an integer.)


# note what is n is negative

# assume n is positiove

# 5 ^5 = 5 ^2 * 5 ^2  * 5
# inititial r = x =5
# 3%2=1 r = 5*5  n = 3//2 =1
# 1%2 =1 r= 5*5 n = 1 //2 =0


# recurion
def myPow(x, n):
    # write your code here
    if x == 0:
        return 0

    if n < 0:
        x = 1 / x
        n = -n

    if n == 0:
        return 1 % x

    if n == 1:
        return x

    print(x, n)
    if n % 2 == 1:
        return myPow(x, n // 2) * myPow(x, n // 2) * x
    return myPow(x, n // 2) * myPow(x, n // 2)


r = myPow(2, -147483648) #stack overflow no idea why
# print(r)


# 5^14 = (5^2)^7 = (5^2)*((5^2)^3
def myPow_v2(x, n):
    if n < 0:
        x = 1 / x
        n = -n

    ans = 1
    tmp = x
    while n != 0:
        print(n, tmp, ans)
        if n % 2 == 1:
            ans *= tmp
        tmp *= tmp
        n //= 2
    return ans


r = myPow_v2(2, 14)  # stack overflow no idea why
print(r)
