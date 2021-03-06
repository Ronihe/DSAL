# 外排序与K路归并算法

# intro:
# External sorting:
# use cases:
# 外排序算法（External Sorting），是指在内存不够的情况下，如何对存储在一个或者多个大文件中的数据进行排序的算法。外排序算法通常是解决一些大数据处理问题的第一个步骤，或者是面试官所会考察的算法基本功。外排序算法是海量数据处理算法中十分重要的一块。
# 在学习这类大数据算法时，经常要考虑到内存、缓存、准确度等因素，这和我们之前见到的算法都略有差别。

# 基本步骤
# 外排序算法分为两个基本步骤：
# 1. 将大文件切割成若干个小文件， 并分别使用内存排好序
# 2. 使用k路归并 K-way merge， 将若干排好序的小文件归并到一个大文件中

# 文件拆分：
# 根据内存的小小， 尽可能多的分批次将数据load到内存中， 并使用系统自带的内存排函数（或者自己快速写的排序函数）， 将其排好序并输出到一个个小文件中。
# 比如一个文件有1T，内存有1G，那么我们就这个大文件中的内容按照 1G 的大小，分批次的导入内存，排序之后输出得到 1024 个 1G 的小文件。

# k 路归并算法
# K路归并算法使用的是数据结构堆（Heap）来完成的，使用 Java 或者 C++ 的同学可以直接用语言自带的 PriorityQueue（C++中叫priority_queue）来代替。
# 我们将 K 个文件中的第一个元素加入到堆里，假设数据是从小到大排序的话，那么这个堆是一个最小堆（Min Heap）。每次从堆中选出最小的元素，输出到目标结果文件中，然后如果这个元素来自第 x 个文件，则从第 x 个文件中继续读入一个新的数进来放到堆里，并重复上述操作，直到所有元素都被输出到目标结果文件中。

# follow up
# 如果我们每个文件只读入1个元素并放入堆里的话，总共只用到了 1024 个元素，这很小，没有充分的利用好内存。另外，单个读入和单个输出的方式也不是磁盘的高效使用方式。因此我们可以为输入和输出都分别加入一个缓冲（Buffer）。假如一个元素有10个字节大小的话，1024 个元素一共 10K，1G的内存可以支持约 100K 组这样的数据，那么我们就为每个文件设置一个 100K 大小的 Buffer，每次需要从某个文件中读数据，都将这个 Buffer 装满。当然 Buffer 中的数据都用完的时候，再批量的从文件中读入。输出同理，设置一个 Buffer 来避免单个输出带来的效率缓慢。


# https://www.lintcode.com/problem/merge-k-sorted-lists/description?_from=ladder&&fromId=1
# https://www.jiuzhang.com/solution/merge-k-sorted-lists/
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


ListNode.__lt__ = lambda x, y: (x.val < y.val)

# using heap:
import heapq


def merge_k_lists(lists):
    if not lists:
        return None
    dummy_header = ListNode(0)
    tail = dummy_header
    heap = []

    for head in lists:
        if head:
            heapq.heappush(heap, head)
    while heap:
        head= heapq.heappop(heap)
        tail.next = head
        tail = head
        if head.next:
            heapq.heappush(heap, head.next)
    return dummy_header.next


# need to know:
def merge_two_linkedL(head1, head2):
    dummy = tail = ListNode(0)
    while head1 and head2:
        if head1.val < head2.val:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    if head1:
        tail.next = head1
    if head2:
        tail.next = head2
    return dummy.next






