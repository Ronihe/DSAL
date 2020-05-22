## 相向双指针

相向双指针，指的是在算法的一开始，两根指针分别位于数组/字符串的两端，并相向行走。如我们在小学的时候经常遇到的问题：


```buildoutcfg
"""
@param s: a list of characters
"""
def reverse(s):
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

### 判断回文串
另外一个双指针的经典练习题，就是回文串的判断问题。给一个字符串，判断这个字符串是不是回文串。

我们可以用双指针的算法轻易的解决：

```buildoutcfg
def isPalindrome(s):
    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
```
Follow up 1: 不区分大小写，忽略非英文字母
完整的题目描述请见：
http://www.lintcode.com/problem/valid-palindrome/

这个问题本身没有太大难度，只是为了给过于简单的 isPalindrome 函数增加一些实现技巧罢了。
代码上和上面的 isPalindrome 函数主要有2个区别：

在 i++ 和 j-- 的时候，要用 while 循环不断的跳过非英文字母
比较的时候要都变成小写之后再比较






















