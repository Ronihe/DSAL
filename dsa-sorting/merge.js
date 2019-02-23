//decomposition of an array into smaller arrays of 0 and 1 elements, then builld up newly sorted array;
//Merging Part:
//given the two arrays which are sorted and consists of all the lements in the
// create a new empty array, iterate through the two array

function merge(arr1, arr2, comparator = null) {
  let left = 0;
  let right = 0;
  const newArr = [];

  while (left < arr1.length && right < arr2.length) {
    if (comparator) {
      if (comparator(arr1[left], arr2[right]) > 0) {
        newArr.push(arr1[left]);
        left++;
      } else if (comparator(arr1[left], arr2[right]) > 0) {
        newArr.push(arr2[right]);
        right++;
      } else {
        newArr.push(arr1[left], arr2[right]);
        left++;
        right++;
      }
    } else {
      if (arr1[left] < arr2[right]) {
        newArr.push(arr1[left]);
        left++;
      } else if (arr2[right] < arr1[left]) {
        newArr.push(arr2[right]);
        right++;
      } else {
        newArr.push(arr1[left], arr2[right]);
        left++;
        right++;
      }
    }
  }
  // push the rest of the arr to the new array
  if (arr1.slice(left).length !== 0) {
    newArr.push(...arr1.slice(left));
  }
  if (arr2.slice(right).length !== 0) {
    newArr.push(...arr2.slice(right));
  }
  return newArr;
}

function mergeSort(arr, comparator) {
  if (arr.length === 1 || 0) return arr;
  // break up the array into halves until you have arrays that are empty or have one element
  let mid = Math.floor(arr.length / 2);
  return merge(arr.slice(0, mid), arr.slice(mid));

  // use the merge function to merge them together
}

module.exports = { mergeSort, merge };
