
# naive way
# https://www.lintcode.com/problem/validate-binary-search-tree/description?_from=ladder&&fromId=1
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
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        # write your code here

        list = self.inorder(root)

        return list == sorted(list) and len(set(list)) == len(list)

    def inorder(self, root):
        if root is None:
            return []

        return self.inorder(root.left) + [root.val] + self.inorder(root.right)


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)








