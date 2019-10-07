# Big O notation

### measure the code's efficiency

# Term:

1. n: the size of the input
   - it can be the actual number as an input in the function
   - can be the number of items in an array
2. runtime:

## the idea about big O is to measure how long an algoo takes to run. when we compare the efficiency of different approaches to a prob.

- not details but focus on what is basically happenning
- runtime - how quickly it grws relative to the input, as the inpt gets arbitrarily large
- ignore the constance: O(2n) => O(n), O(1 + n/2 + 100)O(1+n/2+100) => O(n)
- Drop the less signnificant terms: 1. O(n^3+50n^2+10000) is O(n^3)
- the worst case

# Examples:

```
  function printFirstItem(items) {
  console.log(items[0]);
}
```

the func runs in O(1) or constant time relative to its input

```
  function printAllItems(items) {
  items.forEach(item => {
    console.log(item);
  });
}
```

This function runs in O(n)O(n) time (or "linear time"), where nn is the number of items in the array.

# Big O analysis is awesome except when it's not
- sometimes constance matters
- premature optimization