# https://www.lintcode.com/problem/middle-of-linked-list/description?_from=ladder&&fromId=1

# Description

# Find the middle node of a linked list.
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """

    def middleNode(self, head):
        # write your code here
        if head is None:
            return None
        if head.next is None:
            return head

        p0 = head
        p1 = head.next

        while p1 and p1.next:
            p0 = p0.next
            p1 = p1.next.next

        return p0


# https://www.lintcode.com/problem/two-sum-iii-data-structure-design/description?_from=ladder&&fromId=1
class TwoSum:

    def __init__(self):
        self.arr = []

    """
    @param number: An integer
    @return: nothing
    """

    def add(self, number):
        # write your code here
        self.arr.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        visited = set()

        for num in self.arr:
            if (value - num) in visited:
                return True
            visited.add(num)
        return False


# https://www.lintcode.com/problem/move-zeroes/description?_from=ladder&&fromId=1
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def moveZeroes(self, nums):
        # write your code here
        slow, fast = 0, 0

        while fast < len(nums):

            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

            fast += 1

        return nums
