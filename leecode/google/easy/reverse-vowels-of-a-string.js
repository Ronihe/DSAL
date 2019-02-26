/**
 * @param {string} s
 * @return {string}
 * https://leetcode.com/problems/reverse-vowels-of-a-string/
 */
var reverseVowels = function(s) {
  const arr = s.split('');
  let left = 0;
  let right = s.length - 1;
  const vowels = 'aeiouAEIOU';

  while (left < right) {
    if (vowels.includes(arr[left]) && vowels.includes(arr[right])) {
      [arr[left], arr[right]] = [arr[right], arr[left]];
      left++;
      right--;
    } else if (vowels.includes(arr[left])) {
      right--;
    } else if (vowels.includes(arr[right])) {
      left++;
    } else {
      left++;
      right--;
    }
  }
  return arr.join('');
};
console.log(reverseVowels('hello'));
