/**
 * @param {number[]} nums
 * @return {number[]}
 *
 * https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
 * Input:
 * [4,3,2,7,8,2,3,1]
 * Output:
 * [5,6]
 * Big(n**)
 */
function findDisappearedNumbers(nums) {
  //
  const length = nums.length;
  // creaet a array from one to length
  const completeArr = Array.from({ length: length }, (v, i) => i + 1);
  // since it is tome complexity is O(n)
  //loop through the input arr -- nums
  return completeArr.filter(v => !nums.includes(v));
}

//space O(1), tiME o(n)
function findDisappearedNumbersV2(nums) {
  // we can use index to make nums[num -1] += nums.length;
  const length = nums.length;
  for (let num of nums) {
    nums[(num - 1) % length] += length;
  }
  console.log(nums);
  let result = [];
  for (let i = 0; i < length; i++) {
    if (nums[i] < length + 1) {
      result.push(i + 1);
    }
  }
  return result;
  //iterate throught the input arr and make the each value in the array position > n
}
console.log(findDisappearedNumbersV2([3, 3, 3]));
