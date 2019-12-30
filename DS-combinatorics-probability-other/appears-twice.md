## Question

I have an array of n + 1n+1 numbers. Every number in the range 1..n1..n appears once except for one number that appears twice.

Write a function for finding the number that appears twice.

## breakdown

To avoid extra memory space, use some math

# Solution

1. sun all the num 1...n. n^2 + n /2
2. sumall the numbers in the array/
3. difference is the number

```
  function findRepeat(numbers) {
  if (numbers.length < 2) {
    throw new Error('Finding duplicate requires at least two numbers');
  }

  const n = numbers.length - 1;
  const sumWithoutDuplicate = (n * n + n) / 2;
  const actualSum = numbers.reduce((acc, cur) => acc +  cur, 0);

  return actualSum - sumWithoutDuplicate;
}
```

# Complexity

O(n) time. We can sum all the numbers 1..n1..n in O(1)O(1) time using the fancy formula, but it still takes O(n)O(n) time to sum all the numbers in our input array.

O(1)O(1) additional space—the only additional space we use is for numbers to hold the sums with and without the repeated value.

# Bonus

If our array contains huge numbers or is really long, our sum might be so big it causes an integer overflow. ↴ What are some ways to protect against this?
