# get all the leaves.
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def allLeves_bfs(root):
    if not root:
        return []

    a = []
    q = deque([root])
    while q:
        node = q.popleft()
        if not (node.left and node.right):
            a.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return a

def allLeaves(root):


root = Node(5)
node1 = Node(3)
node2 = Node(4)
node2_1 = Node(6)
node2.left = node2_1
root.left = node2
root.right = node1

leaves = allLeves(root)
print(leaves)
