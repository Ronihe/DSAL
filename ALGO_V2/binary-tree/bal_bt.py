
# https://www.lintcode.com/problem/balanced-binary-tree/description?_from=ladder&&fromId=1
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
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here

        #  height from left and right
        # compare need to return height as well

        isBalanced, height = self.isBalancedTree(root)
        print(height)
        return isBalanced

    def isBalancedTree(self, root):

        if root is None:
            return True, 0

        isBalanced, leftHeight = self.isBalancedTree(root.left)
        if not isBalanced:
            return False, 0
        isBalanced, rightHeight = self.isBalancedTree(root.right)
        if not isBalanced:
            return False, 0

        return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1

