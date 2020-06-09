# using quque to implement a stack:

# 算法步骤
# 队列的知识请看：http://www.jiuzhang.com/tutorial/algorithm/391
# 两个队列实现一个栈，其实并没有什么优雅的办法。就看大家怎么去写这个东西了。

# 构造的时候，初始化两个队列，queue1，queue2。queue1主要用来存储，queue2则主要用来帮助queue1弹出元素以及访问栈顶。
# push：将元素推入queue1当中。
# pop：注意要弹出的元素在queue1末端，故将queue1中元素弹出，并直接推入queue2，当queue1只剩一个元素时，把它pop出来，并作为结果。而后交换两个队列。
# top：类似pop，不过不扔掉queue1中最后一个元素，而是把它也推入queue2当中。
# isEmpty：判断queue1是否为空即可。

from collections import deque


class Stack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    # 将queue1中元素移入queue2,留下最后一个。
    def move_items(self):
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.popleft())

    def swap_queues(self):
        self.queue1, self.queue2 = self.queue2, self.queue1

    def push(self, x):
        self.queue1.append(x)

    def pop(self):
        self.move_items()
        self.queue1.popleft()
        self.swap_queues()

    def top(self):
        self.move_items()
        item = self.queue1.popleft()
        self.swap_queues()
        self.queue1.append(item)
        return item

    def is_empty(self):
        return len(self.queue1) == 0
