# https://www.lintcode.com/problem/inorder-successor-in-bst/description?_from=ladder&&fromId=1

# successor of the p node in a bst

# which  node would be the p the smallest node in p's right subtree
# or lowest ancester node of P

def inorder(root, p):
    if root is None:
        return None
    # if p is on the right side
    if root.val <= p.val:
        return inorder(root.right, p)
    left = inorder(root.left, p)
    # if left:
    #     return left
    # else:
    #     return root
    return left if left else root
