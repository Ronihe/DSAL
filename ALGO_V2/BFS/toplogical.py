# 定义
# 在图论中，由一个有向无环图的顶点组成的序列，当且仅当满足下列条件时，称为该图的一个拓扑排序（英语：Topological sorting）。
#
# 每个顶点出现且只出现一次；
# 若A在序列中排在B的前面，则在图中不存在从B到A的路径。
# 也可以定义为：拓扑排序是对有向无环图的顶点的一种排序，它使得如果存在一条从顶点A到顶点B的路径，那么在排序中B出现在A的后面。
#
# (来自 Wiki)
#
# 实际运用
# 拓扑排序 Topological Sorting 是一个经典的图论问题。他实际的运用中，拓扑排序可以做如下的一些事情：
#
# 检测编译时的循环依赖
# 制定有依赖关系的任务的执行顺序
# 拓扑排序不是一种排序算法
# 虽然名字里有 Sorting，但是相比起我们熟知的 Bubble Sort, Quick Sort 等算法，Topological Sorting 并不是一种严格意义上的 Sorting Algorithm。
#
# 确切的说，一张图的拓扑序列可以有很多个，也可能没有。拓扑排序只需要找到其中一个序列，无需找到所有序列。
# 入度与出度
# 在介绍算法之前，我们先介绍图论中的一个基本概念，入度和出度，英文为 in-degree & out-degree。
# 在有向图中，如果存在一条有向边 A-->B，那么我们认为这条边为 A 增加了一个出度，为 B 增加了一个入度。
#
# 算法流程
# 拓扑排序的算法是典型的宽度优先搜索算法，其大致流程如下：
#
# 统计所有点的入度，并初始化拓扑序列为空。
# 将所有入度为 0 的点，也就是那些没有任何依赖的点，放到宽度优先搜索的队列中
# 将队列中的点一个一个的释放出来，放到拓扑序列中，每次释放出某个点 A 的时候，就访问 A 的相邻点（所有A指向的点），并把这些点的入度减去 1。
# 如果发现某个点的入度被减去 1 之后变成了 0，则放入队列中。
# 直到队列为空时，算法结束，
# 深度优先搜索的拓扑排序
# 深度优先搜索也可以做拓扑排序，不过因为不容易理解，也并不推荐作为拓扑排序的主流算法。
# https://www.lintcode.com/problem/topological-sorting/

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
import collections


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        # write your code here

        node_to_indegree_map = self.findRoot(graph)
        start_nodes = [node for node in node_to_indegree_map if node_to_indegree_map[node] == 0]
        q = collections.deque(start_nodes)

        order_list = []

        while q:
            node = q.popleft()
            order_list.append(node)
            for neighbor in node.neighbors:
                node_to_indegree_map[neighbor] -= 1
                if node_to_indegree_map[neighbor] == 0:
                    q.append(neighbor)

        return order_list

        return order_list

    def findRoot(self, graph):
        #  find the node which is not exist in the
        node_to_indegree_map = {node: 0 for node in graph}

        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree_map[neighbor] = node_to_indegree_map[neighbor] + 1

        return node_to_indegree_map
