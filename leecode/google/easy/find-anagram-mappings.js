/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 *
 * We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j
 *
 * Note:
 * A, B have equal lengths in range [1, 100].
 * A[i], B[i] are integers in range [0, 10^5].
 */

//for example A:[1, 2, 3], B is [2, 3, 1]
function anagramMappings(A, B) {
  // make B an object to make every element in B as the key and array of indexes as the value if there are multiple same values

  const BObj = {};
  for (let i = 0; i < B.length; i++) {
    let el = B[i];
    if (BObj[el]) {
      BObj[el].push(i);
    } else {
      BObj[el] = [i];
    }
  }

  const mapping = [];
  //iterate through A, everytime get the value from BObj pop and value out and push it to the mapping array
  for (let i = 0; i < A.length; i++) {
    let Ael = A[i];
    let idxB = BObj[Ael].pop();
    mapping.push(idxB);
  }
  return mapping;
}

let A = [12, 28, 46, 32, 50];
let B = [50, 12, 32, 46, 28];
console.log(anagramMappings(A, B));
