//Big0(n) O(n) time and O(1)O(1) space.
function mergeArrays(array1, array2) {
  // Set up our mergedArray
  const mergedArray = [];

  let currentIndexAlices = 0;
  let currentIndexMine = 0;
  let currentIndexMerged = 0;

  while (currentIndexMerged < array1.length + array2.length) {
    const isarray1Exhausted = currentIndexMine >= array1.length;
    const isarray2Exhausted = currentIndexAlices >= array2.length;

    // Case: next comes from my array
    // My array must not be exhausted, and EITHER:
    // 1) Alice's array IS exhausted, or
    // 2) The current element in my array is less
    //    than the current element in Alice's array
    if (
      !isarray1Exhausted &&
      (isarray2Exhausted ||
        array1[currentIndexMine] < array2[currentIndexAlices])
    ) {
      mergedArray[currentIndexMerged] = array1[currentIndexMine];
      currentIndexMine++;

      // Case: next comes from Alice's array
    } else {
      mergedArray[currentIndexMerged] = array2[currentIndexAlices];
      currentIndexAlices++;
    }

    currentIndexMerged++;
  }

  return mergedArray;
}

module.exports = mergeArrays;
