//loop through the arr,
//if the element is greater than the right one, swap it
//change the for loop length -1

function bubbleSort(arr, comparator = null) {
  // const swap = (arr, idx1, idx2) => {
  //   [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]];
  // };

  // for (let i = arr.length; i > 0; i--) {
  //   for (let j = 0; j < i - 1; j++) {
  //     if (arr[j] > arr[j + 1]) {
  //       swap(arr, j, j + 1);
  //     }
  //   }
  // }
  // return arr;

  let loopLength = arr.length - 1;
  while (loopLength > 0) {
    for (let i = 0; i < loopLength; i++) {
      //if the comparator is provided
      if (comparator) {
        if (comparator(arr[i], arr[i + 1]) > 0) {
          [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
        }
      }
      // comparator is not provided
      if (arr[i] > arr[i + 1]) {
        [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
      }
    }
    loopLength--;
  }
  return arr;
}

module.exports = bubbleSort;
