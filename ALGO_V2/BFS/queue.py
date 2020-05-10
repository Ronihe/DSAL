# FIFO: first in first out.
# bfs 中记录带扩展的节点

# array： easy to find
# linked list：easy to insert and delete

# methods:
# add()队尾追加元素
# poll()弹出队首元素
# size()返回队列长度
# empty()判断队列为空

# use cases: message queue, 当消息产生和消费the速度不一致时， 就需要message queue,
# “消息”是计算机间传送的数据，可以只包含文本；也可复杂到包含嵌入对象。当消息“生产”和“消费”的速度不一致时，就需要消息队列，临时保存那些已经发送而并未接收的消息。例如集体打包调度，服务器繁忙时的任务处理，事件驱动等等。
#
# 常用的消息队列实现包括RabbitMQ，ZeroMQ等等。
# https://blog.csdn.net/whoamiyang/article/details/54954780




class Queue:
    def __init__(self):
        self._elements = []
        self.pointer = 0  # head position

    @property
    def elements(self):
        print(not self._elements)
        if not self._elements:
            return []
        return self._elements[self.pointer:]

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return self.size() == 0

    def add(self, e):
        self._elements.append(e)

    def poll(self):
        if self.isEmpty():
            return None

        self.pointer += 1
        return self.elements[self.pointer - 2]

my_queue = Queue()
my_queue.add(34)
size = size = my_queue.size()
print(size)
