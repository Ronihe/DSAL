function maximumProductSunarray(nums) {
  // curentLargest product is the larger of arr[i-1]*arr[i] and curentLargest*arr[i]
  //the globalLargest maximum product is the larger of curentLargest and globalLargest
  let currentLargest = nums[0];
  let globalLargest = nums[0];

  for (let i = 1; i < nums.length; i++) {
    currentLargest = Math.max(nums[i - 1] * nums[i], currentLargest);
    globalLargest = Math.max(globalLargest, currentLargest);
  }
  return globalLargest;
}
