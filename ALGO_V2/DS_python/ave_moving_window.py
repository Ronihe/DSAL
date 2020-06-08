# 解题思路
# 我们需要一个数据结构来维护在窗口中的值，这个数据结构有一个要求，当存储的数个数大于窗口大小m时，需要弹出最先进入的数，这正好时队列的性质，所以可以用队列来维护。
#
# 算法：队列模拟滑动窗口
# 初始化时新建一个队列。
# 每次调用next(x)时，将x加入队列。
# 如果队列长度大于m，弹出队首。
# 计算结果并返回。
# 复杂度分析
# 设窗口大小为m。
#
# 单次next()时间复杂度O(1)
#
# 队列插入和弹出都是O(1)。
# 空间复杂度O(m)
#
# 最多存储m个数，空间复杂度为O(m)。
import collections
class MovingAverage:
    """
    @param: size: An integer
    """

    def __init__(self, size):
        self.sum = 0
        self.max_size = size
        self.queue = collections.deque()

    """
    @param: val: An integer
    @return:  
    """

    def next(self, val):
        self.sum = self.sum + val
        self.queue.append(val)

        # 队列中的元素过多时，弹出队首元素
        if len(self.queue) > self.max_size:
            self.sum = self.sum - self.queue.popleft()

        return self.sum / len(self.queue)
