# https://www.lintcode.com/problem/maximum-depth-of-binary-tree/description

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0

        return self.dfs(root)

    def dfs(self, node):
        if node is None:
            return 0

        left = node.left
        right = node.right

        leftDepth = self.dfs(left)
        rightDepth = self.dfs(right)

        return max(leftDepth, rightDepth) + 1
