# what is priority queue:
# normal queue: FIFO
# priority queue: abstract data structure. FIFO and and each item has a special key for its priority level


# List:
# A very simple and straightforward way is to use the normal list but sort it every time an item is added. Here’s an example:

def pq_list():
    customers = []
    customers.append((2, "Harry"))  # no sort needed here because 1 item.
    customers.append((3, "Charles"))
    customers.sort(reverse=True)

    customers.append((1, "Riya"))
    customers.sort(reverse=False)
    return customers


c = pq_list()
print(c)

# USING heapq
import heapq


# time complex would be logn
def pq_heapq():
    customers = []
    heapq.heappush(customers, (10, "jim"))
    heapq.heappush(customers, (8, "hana"))
    heapq.heappush(customers, (11, "why"))

    print(customers)
pq_heapq()

# Using priorityqueeu
from queue import PriorityQueue

def pq_priorityQueue():
    customer = PriorityQueue()

    customer.put((2, "two"))
    customer.put((3, "three"))
    customer.put((1, "one"))

    while customer:
        c = customer.get()



pq_priorityQueue()

