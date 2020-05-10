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

