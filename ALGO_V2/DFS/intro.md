##  隐式图深度优先搜索
在非二叉树上的深度优先搜索（Depth-first Search）中，90%的问题，不是求组合（Combination）就是求排列（Permutation）。特别是组合类的深度优先搜索的问题特别的多。而排列组合类的搜索问题，本质上是一个“隐式图”的搜索问题。

### 什么是隐式图？

一个问题如果没有明确的告诉你什么是点，什么是边，但是又需要你进行搜索的话，那就是一个隐式图搜索问题了。
所以隐式图搜索的问题，首先要分析清楚什么是点什么是边。这部分内容我们将在课上进行讲解。

章节的先修内容有：

通过全子集问题 Subsets 了解组合类搜索的两种形式
通过全子集问题 II 了解如何在搜索中去重
通过全排列问题 Permutations 学习排列式搜索
课后补充内容有：

使用非递归的方法实现全子集问题
下一个排列
第几个排列

题目的意思就是求出一个集合的所有子集。假设这个集合中是没有重复元素的。你可能已经会做这个问题，但是你知道么，这个问题存在 4 种解法么？

我们将从下面的 3 个方面来讲解这个问题：

1. 如何用最简单的递归方式来实现？
2. 如何用可以推广到排列类搜索问题的递归方式来实现？
3. 如果集合中有重复元素如何处理？


### non-recursion
用非递归（Non-recursion / Iteration）的方式实现全子集问题，有两种方式：

进制转换（binary）
宽度优先搜索（Breadth-first Search）

基于 BFS 的方法
在 BFS 那节课的讲解中，我们很少提到用 BFS 来解决找所有的方案的问题。事实上 BFS 也是可以用来做这件事情的。
用 BFS 来解决该问题时，层级关系如下：
```commandline
第一层: []
第二层: [1] [2] [3]
第三层: [1, 2] [1, 3], [2, 3]
第四层: [1, 2, 3]

```

每一层的节点都是上一层的节点拓展而来。
```commandline
class Solution:
    def subsets(self, nums):
        results = []

        if not nums:
            return results

        nums.sort()

        # BFS
        queue = deque()
        queue.append([])

        while queue:
            subset = queue.popleft()
            results.append(subset)

            for i in range(len(nums)):
                if not subset or subset[-1] < nums[i]:
                    nextSubset = list(subset)
                    nextSubset.append(nums[i])
                    queue.append(nextSubset)

        return results

```

如何求一个排列是第几个排列？
题目描述
给出一个不含重复数字的排列，求这些数字的所有排列按字典序排序后该排列的编号，编号从1开始。
例如排列[1,2,4]是第1个排列。
http://www.lintcode.com/zh-cn/problem/permutation-index/

算法描述
只需计算有多少个排列在当前排列A的前面即可。如何算呢?举个例子，[3,7,4,9,1]，在它前面的必然是某位置i对应元素比原数组小，而i左侧和原数组一样。也即[3,7,4,1,X]，[3,7,1,X,X]，[3,1或4,X,X,X]，[1,X,X,X,X]。
而第i个元素，比原数组小的情况有多少种，其实就是A[i]右侧有多少元素比A[i]小，乘上A[i]右侧元素全排列数，即A[i]右侧元素数量的阶乘。i从右往左看，比当前A[i]小的右侧元素数量分别为1,1,2,1，所以最终字典序在当前A之前的数量为1×1!+1×2!+2×3!+1×4!=39，故当前A的字典序为40。

具体步骤：

用permutation表示当前阶乘，初始化为1,result表示最终结果，初始化为0。由于最终结果可能巨大，所以用long类型。
i从右往左遍历A，循环中计算A[i]右侧有多少元素比A[i]小，计为smaller，result += smaller * permutation。之后permutation *= A.length - i，为下次循环i左移一位后的排列数。
已算出多少字典序在A之前，返回result+1。
参考代码
```commandline
class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        permutation = 1
        result = 0
        for i in range(len(A) - 2, -1, -1):
            smaller = 0
            for j in range(i + 1, len(A)):
                if A[j] < A[i]:
                    smaller += 1
            result += smaller * permutation
            permutation *= len(A) - i
        return result + 1
```
：为了找寻每个元素右侧有多少元素比自己小，用了O(n^2)O(n 
2
 )的时间，能不能更快些？
A：可以做到O(nlogn)O(nlogn)！但是很复杂，这是另外一个问题了，可以使用BST，归并排序或者线段树，详见http://www.lintcode.com/zh-cn/problem/count-of-smaller-number-before-itself/

Q：元素有重复怎么办？
A：好问题！元素有重复，情况会复杂的多。因为这会影响A[i]右侧元素的排列数，此时的排列数计算方法为总元素数的阶乘，除以各元素值个数的阶乘，例如[1,1,1,2,2,3]，排列数为6!\div(3!\times2!\times1!)6!÷(3!×2!×1!)。
为了正确计算阶乘数，需要用哈系表记录A[i]及右侧的元素值个数，并考虑到A[i]与右侧比其小的元素A[k]交换后，要把A[k]的计数减一。用该哈系表计算正确的阶乘数。
而且要注意，右侧比A[i]小的重复元素值只能计算一次，不要重复计算！

### 如何求下一个排列

问题描述

给定一个若干整数的排列，给出按整数大小进行字典序从小到大排序后的下一个排列。若没有下一个排列，则输出字典序最小的序列。
例如1,2,3 → 1,3,2，3,2,1 → 1,2,3，1,1,5 → 1,5,1
原题链接：
http://www.lintcode.com/problem/next-permutation-ii/
http://www.lintcode.com/problem/next-permutation/
（两题类似，一个要求原地修改，一个要求返回新的排列）

算法描述
如果上来想不出方法，可以试着找找规律，我们关注的重点应是原数组末尾。

从末尾往左走，如果一直递增，例如...9,7,5，那么下一个排列一定会牵扯到左边更多的数，直到一个非递增数为止，例如...6,9,7,5。对于原数组的变化就只到6这里，和左侧其他数再无关系。6这个位置会变成6右侧所有数中比6大的最小的数，而6会进入最后3个数中，且后3个数必是升序数组。

所以算法步骤如下：

从右往左遍历数组nums，直到找到一个位置i，满足nums[i] > nums[i - 1]或者i为0。
i不为0时，用j再次从右到左遍历nums，寻找第一个nums[j] > nums[i - 1]。而后交换nums[j]和nums[i - 1]。注意，满足要求的j一定存在！且交换后nums[i]及右侧数组仍为降序数组。
将nums[i]及右侧的数组翻转，使其升序。
Q：i为0怎么办？
A：i为0说明整个数组是降序的，直接翻转整个数组即可。

Q：有重复元素怎么办？
A：在遍历时只要严格满足nums[i] > nums[i - 1]和nums[j] > nums[i - 1]就不会有问题。

Q：元素过少是否要单独考虑？
A：当元素个数小于等于1个时，可以直接返回。
```commandline
class Solution:
    # 用于翻转nums[i]到nums[j]，包含两端的这一小段数组
    def swapList(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
    """
    @param nums: An array of integers
    @return: nothing
    """
    def nextPermutation(self, nums):
        n = len(nums)
        if n <= 1:
            return
        
        i = n-1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1

        if i != 0:
            j = n-1
            while nums[j] <= nums[i-1]:
                j -= 1
            nums[j], nums[i-1] = nums[i-1], nums[j]
        self.swapList(nums, i, n-1)
```