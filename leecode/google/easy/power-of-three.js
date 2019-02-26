/**
 * @param {number} n
 * @return {boolean}
 * https://leetcode.com/problems/power-of-three/
 */
var isPowerOfThree = function(n) {
  if (n < 1) return false;
  if (n === 1) return true;
  if (n % 3 !== 0) return false;

  if (n % 3 === 0) {
    return isPowerOfThree(n / 3);
  }
};
