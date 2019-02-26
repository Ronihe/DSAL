/**
 * @param {string} s
 * @return {boolean}
 * https://leetcode.com/problems/valid-parentheses/
 *
 *
 */
function isValid1(s) {
  const matchingMap = {
    '{': '}',
    '[': ']',
    '(': ')'
  };

  const stack = [];

  //iterate through the string and add and opening bracket to the stack
  // if it is closing bracket it should the same as last element in the stack, if not return false

  for (let bracket of s) {
    if (matchingMap[bracket]) {
      stack.push(matchingMap[bracket]);
    } else {
      if (stack.pop() !== bracket) return false;
    }
  }

  if (stack.length > 0) return false;
  return true;
}

isValid1('()');
