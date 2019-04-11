//Big0(n)
function reverseLettersInPlace(array) {
  // two pointer
  let leftIdx = 0;
  let rightIdx = array.length - 1;

  while (leftIdx < rightIdx) {
    // ES6
    //[array[leftIdx], array[rightIdx]] = [array[rightIdx], array[leftIdx]];
    let temp = array[leftIdx];
    array[leftIdx] = array[rightIdx];
    array[rightIdx] = temp;
    leftIdx++;
    rightIdx--;
  }

  return array;
}

module.exports = reverseLettersInPlace;
