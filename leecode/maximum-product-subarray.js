function maximumProductSunarray(nums) {
  // curentLargest product is the larger of arr[i-1]*arr[i] and curentLargest*arr[i]
  //the globalLargest maximum product is the larger of curentLargest and globalLargest
  let currentLargest = nums[0];
  let currentSmallest = nums[0];
  let globalLargest = nums[0];

  for (let i = 1; i < nums.length; i++) {
    currentLargest = Math.max(
      currentLargest * nums[i],
      currentSmallest * nums[i],
      nums[i]
    );
    currentSmallest = Math.min(
      currentLargest * nums[i],
      currentSmallest * nums[i],
      nums[i]
    );
    globalLargest = Math.max(globalLargest, currentLargest);
    console.log(currentLargest, currentSmallest, globalLargest);
  }
  return globalLargest;
}

let test = [2, 3, -2, 4];
console.log(maximumProductSunarray(test));
