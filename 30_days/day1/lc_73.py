
from typing import List

"""
73. Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

"""




"""
solution1: use two set for rows and columns for the cells are zeros
iterate the nested list to get the row and col
iterate the nested list again to make the cell which row or cell in the row_set / rol_set

Time: O(M * N)
Space: O(M + N)

"""
def setZeroes(matrix: List[List[int]]) -> None:
	
	row_size = len(matrix)
	col_size = len(matrix[0])
	row_set, col_set = set(), set()

	for r in range(row_size):
		for c in range(col_size):
			if matrix[r][c] == 0:
				row_set.add(r)
				col_set.add(c)


	for r in range(row_size):
		for c in range(col_size):
			if (r in row_set) or (c in col_set):
				matrix[r][c] = 0



"""
solution2: 

# mark the first row and and first column as 0 of the cell which is 0, 
# iterate again to make all respective cells to 0, (just need to interate the first row and first column)
Time: O(M * N)
Space: O(1) constant

"""
def setZeroes_2(matrix: List[List[int]]) -> None:
	row_size = len(matrix)
	col_size = len(matrix[0])


	for r in range(row_size):
		for c in range(col_size):
			if matrix[r][c] == 0:
				matrix[r][0] = 0
				matrix[0][c] = 0


	for r in range(row_size):
		for j in range(col_size):
			if matrix[r][0] == 0 or matrix[0][c] == 0:
				matrix[r][c] = 0


















test_case = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(test_case)
print(test_case)