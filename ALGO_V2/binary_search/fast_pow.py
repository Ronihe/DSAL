



class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):
        # write your code here

        ans = 1
        tmp = a

        while n != 0:
            if n % 2 != 0:
                ans = tmp * ans % b
            tmp *= tmp % b
            n //= 2
        return ans % b



s = Solution()

fp = s.fastPower(2, 10, 1)
print(fp)




