/** product: calculate the product of an array of numbers. */
// basecase is
function product(nums) {
  if (nums.length === 1) {
    return nums[0];
  }
  return nums[0] * product(nums.slice(1));
}

/** longest: return the length of the longest word in an array of words. */
// create the variable of the length
// if the
// cr
function longest(words) {
  let longest = 0;
  for (let word of words) {
    longest = word.length > longest ? word.length : longest;
  }
  return longest;
}

/** everyOther: return a string with every other letter. */

function everyOther(str) {
  let out = '';
  function _oddLetter(str, i) {
    if (str.length === i) return;
    if (i % 2 === 0) out += str[i];
    _oddLetter(str, i + 1);
  }
  _oddLetter(str, 0);
  return out;
}

/** isPalindrome: checks whether a string is a palindrome or not. */
// check the str[0] === str[str.length-1]
function isPalindrome(str) {
  // if (str.length % 2 !== 0) return false;
  if (str.length === 0) return true;
  if (str[0] === str[str.length - 1]) {
    return isPalindrome(str.slice(1, str.length - 1));
  } else {
    return false;
  }
}

/** findIndex: return the index of val in arr (or -1 if val is not present). */
//
function findIndex(arr, val) {
  let idx = -1;
  function gotIndex(arr, index = 0) {
    if (arr.length === 0) return;
    if (arr[0] === val) {
      idx = index;
      return;
    }
    if (arr[0] !== val) {
      index++;
      gotIndex(arr.slice(1), index);
    }
  }
  gotIndex(arr);
  return idx;
}

/** revString: return a copy of a string, but in reverse. */

function revString(str, idx = str.length) {
  if (idx === 0) return '';
  idx--;
  return str[idx] + revString(str, idx);
}

/** gatherStrings: given an object, return an array of all of the string values. */

function gatherStrings(obj, out = []) {
  for (let key in obj) {
    // if the value is string, added to the array;
    if (typeof obj[key] === 'string') out.push(obj[key]);

    // if the value is object, call the itself
    if (typeof obj[key] === 'object') gatherStrings(obj[key], out);
    // go to the next
  }
  return out;
  //helper funtion to check the
}

/** binarySearch: given a sorted array of numbers, and a value,
 * return the index of that value (or -1 if val is not present). */

function binarySearch(arr, val, left = 0, right = arr.length) {
  if (left > right) {
    return -1;
  }
  let middle = Math.floor((right + left) / 2);
  if (arr[middle] === val) {
    return middle;
  }
  if (arr[middle] > val) {
    return binarySearch(arr, val, left, middle - 1);
  }
  return binarySearch(arr, val, middle + 1, right);
}

module.exports = {
  product,
  longest,
  everyOther,
  isPalindrome,
  findIndex,
  revString,
  gatherStrings,
  binarySearch
};

function realSize(arrays, total = 0) {
  // Force be with you, code warrior!

  for (let el of arrays) {
    if (Number.isInteger(el)) total++;
    if (Array.isArray(el)) return realSize(el, total);
  }

  //helper function
  // function nestedArray(el, total) {
  //   if (Number.isInteger(el)) total++;
  //   if (Array.isArray(el)) nestedArray(el);
  //   return total;
  // }

  return total;
}

console.log(realSize([[[5], 3], 0, 2, [], [4, [5, 6]]]));
