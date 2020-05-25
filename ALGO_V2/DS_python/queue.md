##定义
队列为一种先进先出的线性表
只允许在表的一端进行入队，在另一端进行出队操作。在队列中，允许插入的一端叫队尾，允许删除的一端叫队头，即入队只能从队尾入，出队只能从队头出

### 思路
1. 需要两个节点，一个头部节点，也就是dummy节点，它是在加入的第一个元素的前面，也就是dummy.next=第一个元素，这样做是为了方便我们删除元素，还有一个尾部节点，也就是tail节点，表示的是最后一个元素的节点
2. 初始时，tail节点跟dummy节点重合
3. 当我们要加入一个元素时，也就是从队尾中加入一个元素，只需要新建一个值为val的node节点，然后tail.next=node，再移动tail节点到tail.next
4. 当我们需要删除队头元素时，只需要将dummy.next变为dummy.next.next，这样就删掉了第一个元素，这里需要注意的是，如果删掉的是队列中唯一的一个元素，那么需要将tail重新与dummy节点重合
5. 当我们需要得到队头元素而不删除这个元素时，只需要获得dummy.next.val就可以了

```commandline
class QueueNode:
    def __init__(self, value):
        self.val = value
        self.next = None


class Queue:
    def __init__(self):
        self.dummy = QueueNode(-1)
        self.tail = self.dummy

    def enqueue(self, val):
        node = QueueNode(val)
        self.tail.next = node
        self.tail = node

    def dequeue(self):
        ele = self.dummy.next.val
        self.dummy.next = self.dummy.next.next

        if not self.dummy.next:
            self.tail = self.dummy
        return ele

    def peek(self):
        return self.dummy.next.val

    def isEmpty(self):
        return self.dummy.next == None

```

## 什么是循环数组，如何用循环数组实现队列？
什么是循环数组
Circular array = a data structure that used a array as if it were connected end-to-end

可以图示为：

如何实现队列
1. 我们需要知道队列的入队操作是只在队尾进行的，相对的出队操作是只在队头进行的，所以需要两个变量front与rear分别来指向队头与队尾
2. 由于是循环队列，我们在增加元素时，如果此时 rear = array.length - 1 ，rear 需要更新为 0；同理，在元素出队时，如果 front = array.length - 1, front 需要更新为 0. 对此，我们可以通过对数组容量取模来更新。

```commandline
class CircularQueue:
    def __init__(self, n):
        self.circularArray = [0]*n
        self.front = 0
        self.rear = 0
        self.size = 0
        
    """
    @return:  return true if the array is full
    """
    def isFull(self):
        return self.size == len(self.circularArray)

    """
    @return: return true if there is no element in the array
    """
    def isEmpty(self):
        return self.size == 0
```