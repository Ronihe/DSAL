/**
 * @param {number[]} digits
 * @return {number[]}
 * https://leetcode.com/problems/plus-one/
 */
var plusOne = function(digits) {
  const length = digits.length;
  let adding = 1;
  //iterate the digits from the end

  for (let i = length - 1; i >= 0; i--) {
    if (digits[i] + adding < 10) {
      digits[i] += adding;
      adding = 0;
    } else {
      digits[i] = 0;
    }
  }

  adding === 1 && digits.unshift(1);
  return digits;
};

console.log(plusOne([9, 9, 9]));
