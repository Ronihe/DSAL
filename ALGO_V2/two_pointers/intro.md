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
#### Follow up 1: 不区分大小写，忽略非英文字母
完整的题目描述请见：
http://www.lintcode.com/problem/valid-palindrome/

这个问题本身没有太大难度，只是为了给过于简单的 isPalindrome 函数增加一些实现技巧罢了。
代码上和上面的 isPalindrome 函数主要有2个区别：

在 i++ 和 j-- 的时候，要用 while 循环不断的跳过非英文字母
比较的时候要都变成小写之后再比较

#### Follow up 2: 允许删掉一个字母（类似的，允许插入一个字母）

完整的题目描述请见：
http://www.lintcode.com/problem/valid-palindrome-ii/

FLAG 的面经中出现过此题。一个简单直观的粗暴想法是，既然要删除一个字母，那么我们就 for 循环枚举（Enumerate）每个字母，试试看删掉这个字母之后，该字符串是否为一个回文串。

上述粗暴算法的时间复杂度是 O(n^2)O(n 
2
 )，因为 for 循环枚举被删除字母的复杂度为 O(n)O(n)，判断剩余字符构成的字符串是否为回文串的复杂度为 O(n)O(n)，总共花费 O(n^2)O(n 
2
 )。这显然一猜就应该不符合面试官的要求。

正确的算法如下：

依然用相向双指针的方式从两头出发，两根指针设为 L 和 R。
如果 s[L] 和 s[R] 相同的话，L++, R--
如果 s[L] 和 s[R] 不同的话，停下来，此时可以证明，如果能够通过删除一个字符使得整个字符串变成回文串的话，那么一定要么是 s[L]，要么是 s[R]。
简单的来说，这个算法就是依然按照原来的算法走一遍，然后碰到不一样的字符的时候，从总选一个删除，如果删除之后的字符换可以是 Palindrome 那就可以，都不行的话，那就不行。

这个需要一点数学证明来证明为什么是对的，大家可以先尝试自己证明一下，再来看下面的答案：

## 双指针的鼻祖：两数之和

题目描述
给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。
返回这两个数。

#### hash map
```commandline
def twoSum(numbers, target):
    hash_set = set()
    
    for i in range(len(numbers)):
        if target-numbers[i] in hash_set:
            return (numbers[i], target-numbers[i])
        hash_set.add(numbers[i])

    return None
```
我们使用一个HashSet，来记录每个值是否存在。
每次查找 target - numbers[i] 是否存在，存在即说明找到了，返回两个数即可。

#### 使用双指针算法来解决
```commandline
class Solution:
    def twoSum(self, numbers, target):
        numbers.sort()

        L, R = 0, len(numbers)-1
        while L < R:
            if numbers[L]+numbers[R] == target:
                return (numbers[L], numbers[R])
            if numbers[L]+numbers[R] < target:
                L += 1
            else:
                R -= 1
        return None
```
首先我们对数组进行排序。
用两个指针(L, R)从左右开始：
如果numbers[L] + numbers[R] == target, 说明找到，返回对应的数。
如果numbers[L] + numbers[R] < target, 此时L指针右移，只有这样才可能让和更大。
反之使R左移。
L和R相遇还没有找到就说明没有解。

#### 两个算法的对比
Hash方法使用一个Hashmap结构来记录对应的数字是否出现，以及其下标。时间复杂度为O(n)O(n)。空间上需要开辟Hashmap来存储, 空间复杂度是O(n)O(n)。

Two pointers方法，基于有序数组的特性，不断移动左右指针，减少不必要的遍历，时间复杂度为O(nlogn)O(nlogn)， 主要是排序的复杂度。但是在空间上，不需要额外空间，因此额外空间复杂度是 O(1)O(1)

## 同向双指针
同向双指针的问题，是指两根指针都从头出发，朝着同一个方向前进。我们通过下面 5 个题目来初步认识同向双指针：

1. 数组去重问题 Remove duplicates in an array
问题描述
给你一个数组，要求去除重复的元素后，将不重复的元素挪到数组前段，并返回不重复的元素个数。
https://www.jiuzhang.com/solution/remove-duplicate-numbers-in-array/#tag-highlight-lang-python


```
问题描述
给你一个数组，要求去除重复的元素后，将不重复的元素挪到数组前段，并返回不重复的元素个数。

LintCode 练习地址：http://www.lintcode.com/problem/remove-duplicate-numbers-in-array/

问题分析
这个问题有两种做法，第一种做法比较容易想到的是，把所有的数扔到 hash 表里，然后就能找到不同的整数有哪些。但是这种做法会耗费额外空间 O(n)O(n)。面试官会追问，如何不耗费额外空间。

此时我们需要用到双指针算法，首先将数组排序，这样那些重复的整数就会被挤在一起。然后用两根指针，一根指针走得快一些遍历整个数组，另外一根指针，一直指向当前不重复部分的最后一个数。快指针发现一个和慢指针指向的数不同的数之后，就可以把这个数丢到慢指针的后面一个位置，并把慢指针++。

参考程序

```

滑动窗口问题 Window Sum
```commandline
问题描述
求出一个数组每 kk 个连续整数的和的数组。如 nums = [1,2,3,4], k = 2 的话，window sum 数组为 [3,5,7]。
http://www.lintcode.com/problem/window-sum/

问题分析
这个问题并没有什么难度，但是如果你过于暴力的用户 O(n * k)O(n∗k) 的算法去做是并不合适的。比如当前的 window 是 |1,2|,3,4。那么当 window 从左往右移动到 1,|2,3|,4 的时候，整个 window 内的整数和是增加了3，减少了1。因此只需要模拟整个窗口在滑动的过程中，整数一进一出的变化即可。这就是滑动窗口问题。

```
滑动窗口类的其他问题
以下两个高频的滑动窗口类问题我们在《九章算法强化班》中会讲解：

http://www.lintcode.com/problem/sliding-window-median/
http://www.lintcode.com/problem/sliding-window-maximum/

在 LintCode 中直接搜索 sliding window 能找到所有和 sliding window 相关的练习题。

链表中点问题 Middle of Linked List

问题描述
求一个链表的中点

LintCode 练习地址：http://www.lintcode.com/problem/middle-of-linked-list/

问题分析
这个问题可能大家会觉得，WTF 这么简单有什么好做的？你可能的想法是：

先遍历一下整个链表，求出长度 L，然后再遍历一下链表找到第 L/2 的那个位置的节点。

但是在你抛出这个想法之后，面试官会追问你：如果只允许遍历链表一次怎么办？

可以看到这种 Follow up 并不是让你优化算法的时间复杂度，而是严格的限制了你遍历整个链表的次数。你可能会认为，这种优化有意义么？事实上是很有意义的。因为遍历一次这种场景，在真实的工程环境中会经常遇到，也就是我们常说的数据流问题（Data Stream Problem）。
```commandline

```
数据流问题 Data Stream Problem

- 所谓的数据流问题，就是说，你需要设计一个在线系统，这个系统不断的接受一些数据，并维护这些数据的一些信息。比如这个问题就是在数据流中维护中点在哪儿。（维护中点的意思就是提供一个接口，来获取中点）

类似的一些数据流问题还有：

数据流中位数 http://www.lintcode.com/problem/data-stream-median/
数据流最大 K 项 http://www.lintcode.com/problem/top-k-largest-numbers-ii/
数据流高频 K 项 http://www.lintcode.com/problem/top-k-frequent-words-ii/

这类问题的特点都是，你没有机会第二次遍历所有数据。上述问题部分将在《九章算法强化班》中讲解。

用双指针算法解决链表中点问题
我们可以使用双指针算法来解决链表中点的问题，更具体的，我们可以称之为快慢指针算法。该算法如下：
https://www.jiuzhang.com/solution/middle-of-linked-list/#tag-highlight-lang-python

- 在上面的程序中，我们将快指针放在第二个节点上，慢指针放在第一个节点上，while 循环中每一次快指针走两步，慢指针走一步。这样当快指针走到头的时候，慢指针就在中点了。

快慢指针的算法，在下一小节的“带环链表”中，也用到了。



















两数之差问题 Two Difference

带环链表问题 Linked List Cycle







#### 在排好序的区间序列中插入新区间
- 问题描述
- 给一个排好序的区间序列，插入一段新区间。求插入之后的区间序列。要求输出的区间序列是没有重叠的。

LintCode 练习地址：http://www.lintcode.com/problem/insert-interval/

算法描述
1. 将该新区间按照左端值插入原区间中，使得原区间左端值是有序的。
2. 遍历原区间列表，并把它复制到一个新的answer区间列表当中，answer是最后要返回的结果。
3. 遍历时，要记录上一次访问的区间last。若当前区间左端值小于等于last区间的右端值，说明这两区间有重叠，此时仅更新last的右端值为这两区间右端值较大者；若当前区间左端值大于last的右端值，则可以直接加入answer。
4. 返回answer。
```commandline
class Solution:
      # @param intervals: Sorted interval list.
      # @param newInterval: new interval.
      # @return: A new interval list.
      def insert(self, intervals, new_interval):
          answer = []

          index = 0
          while index < len(intervals) and intervals[index].start < new_interval.start:
              index += 1
          intervals.insert(index, new_interval)

          last = None
          for item in intervals:
              if last == None or last.end < item.start:
                  answer.append(item)
                  last = item
              else:
                  last.end = max(last.end, item.end)
          return answer
```







