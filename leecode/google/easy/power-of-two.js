/**
 * @param {number} n
 * @return {boolean}
 * https://leetcode.com/problems/power-of-two/
 */
var isPowerOfTwo = function(n) {
  if (n < 1) return false;
  if (n === 1) return true;
  if (n % 2 !== 0) return false;

  if (n % 2 === 0) {
    return isPowerOfTwo(n / 2);
  }
};

console.log(isPowerOfTwo(218));
