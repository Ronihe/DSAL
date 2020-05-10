# 如果问题需要你区分开不同层级的结果信息，如 二叉树的分层遍历 Binary Tree Level Order Traversal
# 简单图最短路径问题，如 单词接龙 Word Ladder

# https://www.lintcode.com/problem/binary-tree-level-order-traversal/
# 层级遍历 Level Order Traversa
# https://www.lintcode.com/problem/binary-tree-level-order-traversal/description
# 分析:二叉树的层次遍历通常实现方式为使用队列不断压入节点遍历,每次取出队列首个元素遍历左右子节点，继续压入子节点即可。
# traverse tree with bfs

# bfs withouth levels
import collections


def bfs_wo_levels(start_node):
    visited_set = set([start_node])
    queue = collections.deque(start_node)

    while queue:
        node = queue.popleft()

        for neighbor in node.neighbors:
            if neighbor not in visited_set:
                visited_set.add(neighbor)
                queue.append(neighbor)


# neighbor 表示从某个点 head 出发，可以走到的下一层的节点。
# set/seen 存储已经访问过的节点（已经丢到 queue 里去过的节点）
# queue 存储等待被拓展到下一层的节点
# set/seen 与 queue 是一对好基友，无时无刻都一起出现，往 queue 里新增一个节点，就要同时丢到 set 里。

# bfs with levels
def bfs_w_levels(start_node):
    visited_set = set([start_node])
    queue = collections.deque(start_node)

    while queue:
        size = len(queue)
        for _ in range(size):
            current_node = queue.popleft()
            for neighbor in current_node.neighbors:
                if neighbor not in visited_set:
                    visited_set.add(neighbor)
                    queue.append(neighbor)


# size = len(queue) can be in the for range loop.

# 两个队列来回迭代，来代表相邻的层级。我们可以将当前层的所有节点存在第一个队列中，然后拓展（Extend）出的下一层节点存在另外一个队列中。来回迭代，逐层展开。

def bfs_two_queues(start_node):
    queue1, queue2 = collections.deque(), collections.deque()
    visited_set = set()

    queue1.append(start_node)
    visited_set.add(start_node)
    current_level = 0

    while queue1:
        for node in queue1:
            current_node = queue1.popleft()
            for neighbor in current_node.neighbors:
                if neighbor not in visited_set:
                    visited_set.add(neighbor)
                    queue2.append(neighbor)
        queue1, queue2 = queue2, queue1
        current_level += 1


# 使用 dummy node 来间隔不同的层级。
# Dummy Node，翻译为哨兵节点。Dummy Node 一般本身不存储任何实际有意义的值，通常用作"占位"，或者链表的“虚拟头”。
# 如很多的链表问题中，我们会在原来的头head的前面新增一个节点，这个节点没有任何值，但是 next 指向 head。这样就会方便对 head 进行删除或者在前面插入等操作。

# head->node->node->node ...
# =>
# dummy->head->node->node->node...

# Dummy Node 在 BFS 中如何使用
# 在 BFS 中，我们主要用 dummy node 来做占位符。即，在队列中每一层节点的结尾，都放一个 null（or None in Python，nil in Ruby），来表示这一层的遍历结束了。这里 dummy node 就是一个 null。
# save time : 放一个DUMMY NODE进去（在需要知道第几层的BFS中），可以很清楚的找到每一层的结尾，就不用在每一层BFS之前计算queue的size了
def bfs_dummy_node(start_node):
    visited_set = set([start_node])
    queue = collections.deque([start_node])
    # insert a None as the ending of the queue
    queue.append(None)

    while queue:
        current_node = queue.popleft()
        if current_node is None:
            queue.append(None)
            continue  # skip the rest of the code

        for neighbor in current_node.neighbors:
            if neighbor not in visited_set:
                visited_set.add(neighbor)
                queue.append(neighbor)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


import collections


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        # write your code here
        if not root:
            return []

        q = collections.deque([root])
        tree_list = []

        while q:
            # going to pop out all the element in the current deque
            level = []
            level_length = len(q)
            for _ in range(level_length):
                current = q.popleft()
                level.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            tree_list.append(level)

        return tree_list

    def levelOrder_v2(self, root):
        # write your code here
        if not root:
            return []

        q = [root]
        tree_list = []

        while q:
            # going to pop out all the element in the current deque
            level = [node.val for node in q]
            tree_list.append(level)
            new_q = []
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return tree_list

# https://www.lintcode.com/problem/word-ladder/
