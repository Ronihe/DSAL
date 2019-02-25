/**
 * @param {number[][]} A
 * @return {number[][]}
 * https://leetcode.com/problems/flipping-an-image/
 */
function flipAndInvertImage(A) {
  return A.map(a => {
    let invertedSubA = a.map(el => _invert(el));
    console.log(invertedSubA);
    return _rever(invertedSubA);
  });

  function _rever(arr) {
    let left = 0;
    let right = arr.length - 1;

    while (left < right) {
      [arr[left], arr[right]] = [arr[right], arr[left]];
      left++;
      right--;
    }
    return arr;
  }

  function _invert(num) {
    if (num === 1) return 0;
    if (num === 0) return 1;
  }
}

const test = [[1, 1, 0], [1, 0, 1], [0, 0, 0]];
console.log(flipAndInvertImage(test));
