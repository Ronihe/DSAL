
# https://www.lintcode.com/problem/sequence-reconstruction/description
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        # 最短序列
        # all the seqs have the order of all the node inside, need to get the relationship inside of it and
        graph = self.build_graph(seqs)
        topo_order = self.topological_sort(graph)
        return topo_order == org

    def build_graph(self, seqs):
        # init the graph
        graph = {}
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] =  set()
        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i-1]].add(seq[i])

        return graph
    def indegrees(self, graph):

        indegrees = {node:0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
        return indegrees

    def topological_sort(self, graph):
        indegrees = self.indegrees(graph)

        queue = []
        # there should be one and only one in each level
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)

        topo_order = []

        while queue:
            if len(queue) > 1:
                return None

            node = queue.pop()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) == len(graph):
            return topo_order

        return None
