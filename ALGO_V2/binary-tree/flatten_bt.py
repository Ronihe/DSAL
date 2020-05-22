# https://www.lintcode.com/problem/flatten-binary-tree-to-linked-list/description?_from=ladder&&fromId=1
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/solution/
# recursion here is that we "suppose" that recursion does all the hard work for us and flattens out the left and the right subtrees as shown in the figure. What is it that we have to do then to get our final result? We need a right skewed tree, right?
# _node_ = The current node
# _leftChild_ = the left child of our current node
# _rightChild_ = the right child of our current node
# _leftTail_ = The tail node of the flattened out left subtree
# _rightTail_ = The tail node of the fully formed tree rooted at _node_. This information is needed by the parent recursive calls since the tree rooted at the current node can be some other's node's left subtree or right subtree.


# 1. We'll have a separate function for flattening out the tree since the main function provided in the problem isn't supposed to return anything and our algorithm will return the tail node of the flattened out tree.

# 2. For a given node, we will recursively flatten out the left and the right subtrees and store their corresponding tail nodes in leftTail and rightTail respectively.
# 3. Next, we will make the following connections (only if there is a left child for the current node, else the leftTail would be null)
"""
leftTail.right = node.right
node.right = node.left
node.left = None

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flattenTree(root)

    def flattenTree(self, node):
        if node is None:
            return None
        #        leaf node:

        if node.left is None and node.right is None:
            return node

        leftTail = self.flattenTree(node.left)

        rightTail = self.flattenTree(node.right)

        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None

        if rightTail:
            return rightTail
        return leftTail


