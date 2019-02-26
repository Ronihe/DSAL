/**
 * @param {number[][]} grid
 * @return {number}
 * https://leetcode.com/problems/island-perimeter/
 */
function islandPerimeter(grid) {
  // edge case if the grid is

  //iterate through each element of the array
  //check the four directions
  let height = grid.length;
  let width = grid[0].length;
  let perimeter = 0;
  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      // check if the area is land
      if (grid[y][x] === 1) {
        perimeter += 4;
        // check the top

        if (y > 0 && grid[y - 1][x] === 1) perimeter--;

        // check the bottom
        if (y < height - 1 && grid[y + 1][x] === 1) perimeter--;
        // check the left
        if (x > 0 && grid[y][x - 1] === 1) perimeter--;
        // check the right
        if (x < width - 1 && grid[y][x + 1] === 1) perimeter--;
      }
    }
  }
  return perimeter;
}

let test = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]];

console.log(islandPerimeter(test));
