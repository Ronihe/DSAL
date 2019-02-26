/**
 * @param {string} s
 * @return {number}
 * https://leetcode.com/problems/first-unique-character-in-a-string/
 */
function firstUniqChar(s) {
  // loop through the string and add the each char as the key and value the times it appears
  const mapping = {};
  for (let char of s) {
    mapping[char] = mapping[char] + 1 || 1;
  }
  // loop throught the s if the frequency is 1, return the index
  for (let i = 0; i < s.length; i++) {
    if (mapping[s[i]] === 1) {
      return i;
    }
  }
  return -1;
}

firstUniqChar('leetcode');
