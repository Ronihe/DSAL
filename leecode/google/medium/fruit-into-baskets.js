/**
 * @param {number[]} tree
 * @return {number}
 * https://leetcode.com/problems/fruit-into-baskets/  sliding window
 *
 * get the longest array with the most two 'types'
 *
 */
var totalFruit = function(tree) {
  let kinds = [];
  let total = 0;
  let biggest = 0;

  for (let i = 0; i < tree.length; i++) {
    if (kinds.length === 0) {
      kinds.push(tree[i]);
      total++;
      console.log(biggest, kinds, total);
    } else if (kinds.includes(tree[i])) {
      total++;
      console.log(biggest, kinds, total);
    } else if (!kinds.includes(tree[i]) && kinds.length === 1) {
      kinds.push(tree[i]);
      total++;
      console.log(biggest, kinds, total);
    } else if (!kinds.includes(tree[i]) && kinds.length === 2) {
      total++;
      kinds = [];
      biggest = biggest > total ? biggest : total;
      console.log(biggest, kinds, total);
      total = 0;
    }
  }
  return biggest > total ? biggest : total;
};

console.log(totalFruit([1, 2, 3, 2, 2]));
