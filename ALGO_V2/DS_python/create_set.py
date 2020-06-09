# https://www.lintcode.com/problem/insert-delete-getrandom-o1/description?_from=ladder&&fromId=1
# 插入操作时：
#
# 若已存在此元素返回false
# 不存在时将新的元素插入数组最后一位，同时更新hashMap。
# 删除操作时：
#
# 若不存在此元素返回false
# 存在时先根据hashMap得到要删除数字的下标，再将数组的最后一个数放到需要删除的数的位置上，删除数组最后一位，同时更新hashMap。
# 获取随机数操作时：
#
# 根据数组的长度来获取一个随机的下标，再根据下标获取元素。
import random


class RandomizedSet(object):

    def __init__(self):
        # do initialize if necessary
        self.nums, self.val2index = [], {}

    # @param {int} val Inserts a value to the set
    # Returns {bool} true if the set did not already contain the specified element or false
    def insert(self, val):
        if val in self.val2index:
            return False

        self.nums.append(val)
        self.val2index[val] = len(self.nums) - 1
        return True

    # @param {int} val Removes a value from the set
    # Return {bool} true if the set contained the specified element or false
    def remove(self, val):
        # Write your code here
        if val not in self.val2index:
            return False

        index = self.val2index[val]
        last = self.nums[-1]

        # move the last element to index
        self.nums[index] = last
        self.val2index[last] = index

        # remove last element
        self.nums.pop()
        del self.val2index[val]
        return True

    # return {int} a random number from the set
    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
