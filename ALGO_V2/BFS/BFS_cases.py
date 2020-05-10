import collections


# 图的遍历 traversal in graph

# https://www.lintcode.com/problem/clone-graph/description
# clone a undirected graph, each node in the graph contains a label and a list of its neighbours

# https://www.lintcode.com/problem/clone-graph/description

# 更细一点的划分的话，这一类的问题还可以分为：
#
# 层级遍历 Level Order Traversal
# 由点及面 Connected Component
# 拓扑排序 Topological Sorting

# 由点及面，前面已经提到。
#
# 拓扑排序
#
# 最短路径 Shortest Path in Simple Graph
# 最短路径算法有很多种，BFS 是其中一种，但是他有特殊的使用场景，即必须是在简单图中求最短路径。
# 大部分简单图中使用 BFS 算法时，都是无向图。当然也有可能是有向图，但是在面试中极少会出现。
#
# 什么是简单图（Simple Graph）？
# 即，图中每条边长度都是1（或边长都相同）。
#



class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


def clone_graph(node):
    root = node
    if node is None:
        return node

    # use bfs algorithm to traverse the graph and get all the nodes
    nodes = getNodes(node)

    # copy nodes, store the old->new mapping info in a hash map
    # {old_node: new_node}
    mapping = {}
    for node in nodes:
        mapping[node] = UndirectedGraphNode()

    # copy neighbours (edges)
    for old_node in mapping:
        for neighbor in old_node:
            mapping[old_node].append(neighbor)

    return mapping[root]


def getNodes(node):
    q = collections.deque([node])
    result = set([node])  # all the nodes visited, add to the set once we visited

    while q:
        head = q.popleft()
        for neighbour in head.neighbors:
            if neighbour not in result:
                result.add(neighbour)
                q.append(neighbour)

    return result


node_1 = UndirectedGraphNode(1)
node_2 = UndirectedGraphNode(2)
node_3 = UndirectedGraphNode(3)
node_1.neighbors = [node_2, node_3]
node_2.neighbors = [node_2, node_3]
node_3.neighbors = [node_1, node_3]

print(getNodes(node_1))


# 层级遍历 Level Order Traversal
# https://www.lintcode.com/problem/binary-tree-level-order-traversal/description
# 分析:二叉树的层次遍历通常实现方式为使用队列不断压入节点遍历,每次取出队列首个元素遍历左右子节点，继续压入子节点即可。
# traverse tree with bfs

# 1. create a queue

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
