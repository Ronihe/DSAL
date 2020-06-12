# https://www.lintcode.com/problem/consistent-hashing/description?_from=ladder&&fromId=75
class Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """

    def consistentHashing(self, n):
        # write your code here
        machines = [[0, 359, 1]]
        for m in range(2, n + 1):
            # find the largest machine
            idx, size = self.biggest_machine(machines)
            print(idx, size)
            start = machines[idx][0]

            machines[idx] = [start, int(start + size / 2), machines[idx][-1]]
            new = [int(start + size / 2) + 1, int(start + size), m]

            machines.insert(idx + 1, new)

        return machines

    def biggest_machine(self, machines):

        idx = 0
        total = len(machines)
        max_size = 0
        machine_no = 0

        for m in range(total):
            size = machines[m][1] - machines[m][0]
            if size > max_size:
                max_size = size
                idx = m
                machine_no = machines[m][-1]

            elif size == max_size and machines[m][-1] < machine_no:
                idx = m
                machine_no = machines[m][-1]

        return idx, max_size
