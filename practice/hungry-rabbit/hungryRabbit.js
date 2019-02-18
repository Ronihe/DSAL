/**
 * @param {Array} board - the 2D array for the rabbit's garden
 * @returns {number} the total number of carrots the rabbit can eat
 */

function totoalCarrots(board) {
  let startSpot = _findStartingSpot(board);
  let total = startSpot.val;
  let currSpot = startSpot;
  let nextSpot;
  let carrots = [currSpot.val];

  while (currSpot.val > 0) {
    board[currSpot.row][currSpot.col] = 0;
    nextSpot = _findNextSpot(board, currSpot);
    total += nextSpot.val;
    currSpot = nextSpot;
    carrots.push(currSpot.val);
    console.log(currSpot);
  }
  return total;
}
/**
 *
 * @param {Array} board - the 2D array for the rabbit's garden
 *@returns {Object} Object with row, col, and value keys, the values are Int
 */

function _findStartingSpot(board) {
  let row =
    board.length % 2 === 0
      ? board.length / 2 - 1
      : Math.floor(board.length / 2);

  let col =
    board[0].length % 2 === 0
      ? board[0].length / 2 - 1
      : Math.floor(board.length / 2);
  let val = board[row][col];
  return { row, col, val };
}

/**
 *
 * @param {Array} board - the 2D array for the rabbit's garden
 * @param {Object} currSpot - the current positon of the rabbit with row, col and value of the board
 *@returns {Object} Object with row, col, and value keys, the values are Int
 */

function _findNextSpot(board, currSpot) {
  //check the four directions
  let top = {
    row: currSpot.row - 1,
    col: currSpot.col,
    val: board[currSpot.row - 1] ? board[currSpot.row - 1][currSpot.col] : 0
  };
  let bottom = {
    row: currSpot.row + 1,
    col: currSpot.col,
    val: board[currSpot.row + 1] ? board[currSpot.row + 1][currSpot.col] : 0
  };
  let right = {
    row: currSpot.row,
    col: currSpot.col + 1,
    val: board[currSpot.row][currSpot.col + 1] || 0
  };
  let left = {
    row: currSpot.row,
    col: currSpot.col - 1,
    val: board[currSpot.row][currSpot.col - 1] || 0
  };
  let next = Object.values({ left, top, right, bottom }).reduce(
    (accu, currItem) => {
      return accu.val > currItem.val ? accu : currItem;
    }
  );
  return next;
}

const garden = [
  [5, 7, 9, 6, 3],
  [0, 0, 7, 0, 4],
  [4, 6, 3, 4, 9],
  [3, 1, 0, 5, 8]
];

console.log(totoalCarrots(garden));
