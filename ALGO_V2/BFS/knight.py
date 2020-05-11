# https://www.lintcode.com/problem/knight-shortest-path/description?_from=ladder&&fromId=1

from collections import deque

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath_wrong(self, grid, start, destination):
        # I did not take consideration of how to keep track,
        # write your code here
        # logics from start to try eight directions, , if not destination, and keep all the spots in visited set and not barrier
        # pop out the first one
        x = start["x"]
        y = start["y"]
        x_destination, y_destination = destination["x"], destination["y"]
        q = deque([(x, y)])
        visited_set = set([(x, y)])
        length = 0

        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                # always check when pop out

                for delta_x, delta_y in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
                    next_x = x + delta_x
                    next_y = y + delta_y
                    # make sure the next_y and nex_x are valid
                    if self.isValid(grid, visited_set, next_x, next_y):
                        if (next_x == delta_x) and (next_y == y_destination):
                            return length
                        q.append((next_x, next_y))
                        visited_set.add((next_x, next_y))
            length += 1

        return -1

    def isValid_wrong(self, grid, visited_set, next_x, next_y):
        # in the grid and no barrier
        if not (0 <= next_x < len(grid) and 0 <= next_y < len(grid[0])):
            return False

        if grid[next_x][next_y] or grid[next_x][next_y] in visited_set:
            return False
        return True

    def shortestPath(self, grid, source, destination):
        # write your code here
        # logics from start to try eight directions, , if not destination, and keep all the spots in visited set and not barrier
        # record map to keep record of all the steps we did,
        # pop out the first one
        # loop until the end, if there is not found, return -1
        DIRECTIONS = [
            (-2, -1), (-2, 1), (-1, 2), (1, 2),
            (2, 1), (2, -1), (1, -2), (-1, -2),
        ]
        queue = deque([(source.x, source.y)])
        distance = {(source.x, source.y): 0}

        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return distance[(x, y)]
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in distance:
                    continue
                if not self.is_valid(next_x, next_y, grid):
                    continue
                distance[(next_x, next_y)] = distance[(x, y)] + 1
                queue.append((next_x, next_y))
        return -1

    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])

        if x < 0 or x >= n or y < 0 or y >= m:
            return False

        return not grid[x][y]


source = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
start = dict(x=2, y=0)
destination = dict(x=2, y=2)

s = Solution()
route = s.shortestPath_wrong(source, start, destination)
print(route)
