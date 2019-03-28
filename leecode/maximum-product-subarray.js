function maximumProductSunarray(nums) {
  // curentLargest product is the larger of arr[i-1]*arr[i] and curentLargest*arr[i]
  //the globalLargest maximum product is the larger of curentLargest and globalLargest
  let currentLargest = nums[0];
  let currentSmallest = nums[0];
  let globalLargest = nums[0];

  for (let i = 1; i < nums.length; i++) {
    let a = currentLargest * nums[i];
    let b = currentSmallest * nums[i];

    currentLargest = Math.max(a, b, nums[i]);
    currentSmallest = Math.min(a, b, nums[i]);
    globalLargest = Math.max(globalLargest, currentLargest);
  }
  return globalLargest;
}

let test = [-4, -3, -2];
console.log(maximumProductSunarray(test));
