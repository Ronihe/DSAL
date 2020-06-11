# k cloest points
# Data structure to use
# priority queue:
# abs(abstract data structure, what is a structure defined by its behavior), FIFO
# which is a normal queue with specified key to quantify its priority

# Given some points and an origin point in two-dimensional space, find k points which are nearest to the origin.
# Return these points sorted by distance, if they are same in distance, sorted by the x-axis, and if they are same in the x-axis, sorted by y-axis.


# implement priority queue


# heapq -> mini queue
# O(logN) for insertion and extraction for the smallest number
import heapq


def heapq_p():
    customers = []
    heapq.heappush(customers, (4, "b"))
    heapq.heappush(customers, (3, "Harry_2"))
    heapq.heappush(customers, (4, "a"))
    print(customers)
    while customers:
        print(heapq.heappop(customers))
    print(customers)


# question example:
# 基于 PriorityQueue 的方法 PriorityQueue 里从远到近排序。当 PQ 里超过 k 个的时候，就 pop 掉一个。 时间复杂度 O(nlogk)O(nlogk)
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

def top_k_points(points, origin, k):
    heap = []

    for p in points:
        dist = (p.x - origin.x) ** 2 + (p.y - origin.y) ** 2
        heapq.heappush(heap, (-dist, -p.x, -p.y))

        if len(heap) > k:
            heapq.heappop(heap)
    r = []
    while len(heap) > 0:
        _, x, y = heapq.heappop(heap)
        r.append(Point(-x, -y))

    return r

if __name__ == "__main__":
    heapq_p()
