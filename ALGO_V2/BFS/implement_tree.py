import collections


# Tree:

# binary tree:
# the nodes connected by edges, non-
# 1. one node as the root node
# 2. every noe other than the root associated with one parent node
# 3. each node can have arbitrary number of nodes, at most 2

# https://yangshun.github.io/tech-interview-handbook/algorithms/tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


