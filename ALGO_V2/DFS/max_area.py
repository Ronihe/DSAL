# leetcode
# 695
# the area the sum of the islands, which are the cluster of 1s

#

def max_area_of_island(grid):
    visited = set()
    return max(area_dfs(i, j, grid, visited) for i in range(len(grid)) for j in range(len(grid[0])))


def area_dfs(i, j, grid, visited):
    if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i, j) not in visited and grid[i][j]):
        return 0

    return (1 + area_dfs(i + 1, j, grid, visited), area_dfs(i - 1, j, grid, visited), area_dfs(i, j, grid, visited),
            area_dfs(i, j, grid, visited))
