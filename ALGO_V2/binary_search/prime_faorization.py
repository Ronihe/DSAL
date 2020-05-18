# 在线评测地址: https://www.lintcode.com/problem/prime-factorization/

# the naive way:
import math


def prieFactorzation_v1(num):
    prime_list = []
    k = 2  # k should be equal or larget then the last prime facotor
    times = 0

    while num > 1:
        up = int(math.sqrt(num))
        if num == k or k > up:
            times += 1
            prime_list.append(num)
            break

        while k <= up:

            if num % k == 0:
                prime_list.append(k)
                num = num // k
                break
            times += 1
            k += 1
    return prime_list, times


# test--

test1 = 100891891  # would cause too many time to run
test2 = 100
# r1= prieFactorzation(test1)
# print(r1)
r2 = prieFactorzation_v1(test2)
print(r2)


# for cleaner codes:
# Time: square n
# #space square n
def primeFactorization_v2(num):
    prime_list = []
    k = 2
    times = 0

    # while k ^2  is bigger than num, there is no more prom factor after that
    while k ** 2 <= num:
        print(k, num)
        while num % k == 0:
            prime_list.append(k)
            num = num // k
        k += 1

    if num > 1:
        prime_list.append(num)

    return prime_list


r3 = primeFactorization_v2(test2)
print(r3)
