# https://www.lintcode.com/problem/number-of-islands/description?_from=ladder&&fromId=1
# Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.


# travesal, needs a queue and a list


import collections


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        # traverse trought the list, all the lementinthe sub-list the three direction
        #  just need to put all the related 1 to the vsited and traverse to the end of the bytearra
        if not grid or not grid[0]:
            return 0

        # iterate through the items and all the realted locations of 1 would be included in the visited set, so it wont be added again
        num_island = 0
        visited_set = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if the item is visited or not 1 continue to the next one
                # continue
                # else just bfs to trverse all the realted 1s
                if grid[i][j] and (i, j) not in visited_set:
                    # use bfs to get all the related 1s to the visited_set
                    self.bfs(grid, i, j, visited_set)
                    num_island += 1

        return num_island

    def bfs(self, grid, i, j, visited_set):
        q = collections.deque([(i, j)])
        visited_set.add((i, j))

        while q:
            # check the four directions
            i, j = q.popleft()
            for delta_i, delta_j in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                next_i = i + delta_i
                next_j = j + delta_j
                # the spot is valid and == 1 add to the q and visited_set
                print(self.isValid(next_i, next_j, grid, visited_set))
                if self.isValid(next_i, next_j, grid, visited_set):
                    self.append = q.append((next_i, next_j))
                    visited_set.add((next_i, next_j))

    def isValid(self, i, j, grid, visited_set):
        # i should be 0 - len(grid)
        # j should be 0 - len(grid)
        if (not (0 <= i < len(grid) and 0 <= j < len(grid[0]))) or ((i, j) in visited_set):
            return False
        # if 0, would be False
        return grid[i][j]


test = [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]
solution = Solution()
num = solution.numIslands(test)
print(num)

# TODO: use DFS