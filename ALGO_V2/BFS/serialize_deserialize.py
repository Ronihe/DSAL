
# https://www.lintcode.com/problem/serialize-and-deserialize-binary-tree/description?_from=ladder&&fromId=1
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):
        # write your code here
        if root is None:
            return ""

        # use bfs
        q = deque([root])
        visited = []

        while q:
            node = q.popleft()
            visited.append(str(node.val) if node else "#")
            if node:
                q.append(node.left)
                q.append(node.right)

        return ",".join(visited)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """

    def deserialize(self, data):
        # write your code here
        if not data:
            return None

        bfs_order = [TreeNode(int(val)) if val != "#" else None for val in data.split(",")]
        root = bfs_order[0]
        fast_index = 1

        nodes = [root]
        slow_index = 0  # keep track of the each layer

        while slow_index < len(nodes):
            node = nodes[slow_index]
            slow_index += 1
            node.left = bfs_order[fast_index]
            node.right = bfs_order[fast_index + 1]
            fast_index += 2

            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        return root