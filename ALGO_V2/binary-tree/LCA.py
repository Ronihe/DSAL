# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/

ancester = None


def recurse_tree(node, p, q):
    # if reach the end if the branch, return false
    if not node:
        return False
    # left recursion
    left = recurse_tree(node.left, p, q)

    # right recursion
    right = recurse_tree(node.right, p, q)

    # current node is one of the q or p
    mid = node == p or node == q

    if mid + left + right >= 2:
        global ancester
        ancester = node

    return mid or left or right

# def test():
#     return one() or two() or three()
#
#
# def one():
#     print("I am in one")
#     return False
#
#
# def two():
#     print("i am in two")
#     return 0
#
# def three():
#     print("I am in three")
#     return 0
#
#
# r = test()
# print(r)
