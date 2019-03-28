// https://leetcode.com/problems/maximum-subarray/

/**Input: [-2,1,-3,4,-1,2,1,-5,4],
 * Output: 6
 * Explanation: [4,-1,2,1] has the largest sum = 6.
 */
// naive approach sliding windown

function maxSubArray(nums) {
  let largestSum = nums[0];
  // for loop to remove the element to get the largest sum
  // starting point and ending point, nested loop
  let startingPoint;
  // let endingPoint = 0;
  for (startingPoint = 0; startingPoint < nums.length; startingPoint++) {
    let endingPoint;

    for (
      endingPoint = startingPoint + 1;
      endingPoint < nums.length + 1;
      endingPoint++
    ) {
      let newSum = nums
        .slice(startingPoint, endingPoint)
        .reduce((acc, curr) => acc + curr);
      largestSum = largestSum > newSum ? largestSum : newSum;
    }
  }
  return largestSum;
}

function maxSubArray2(nums) {
  // kadane
  let currentMax = nums[0];
  let globalMax = nums[0];

  for (let i = 1; i < nums.length; i++) {
    // currentMax is the larger of the current ele and the (currentMax + ele)
    currentMax = Math.max(nums[i], nums[i] + currentMax);
    globalMax = Math.max(currentMax, globalMax);
  }

  return globalMax;
}

let test = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
console.log(maxSubArray2(test));
