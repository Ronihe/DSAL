# https://www.lintcode.com/problem/clone-graph/description?_from=ladder&&fromId=1
"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""
from collections import deque


class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        # write your code here
        # copy all the node, and copy all the edge

        # get all the all the nodes
        if node is None:
            return None

        root = node
        # use bfs to get all the nodes
        nodes = self.all_nodes(root)

        # copy nodes, store the old -> new mapping info in hash map
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)

        # copy the edge
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

    def all_nodes(self, node):
        q = deque([node])
        visited = set([node])

        while q:
            current_node = q.popleft()

            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)

        return visited

