# types of sort:
1. bubble sort:
step through the list and compare adjacent pairs of elements if wrong order just swap it.
Time: O n^2 best: n
space: O 1

2. selection sort
divide to two part: 1 sorted, 2. unsorted
for the unsorted part, keep getting the smallest and added to the end of the sorted list
Time: O n^2 best n^2
Space : O 1

3. insertion sort
iterate through the loop, find the righ spot in the sorted part
Time O n^2
space O 1

4. merge sort: (divide and conquer)
(1) Continuously divide the unsorted list until you have N sublists, where each sublist has 1 element that is “unsorted” and N is the number of elements in the original array.
(2) Repeatedly merge i.e conquer the sublists together 2 at a time to produce new sorted sublists until all elements have been fully merged into a single sorted array.
time : nlogn
space : n

5. quick_sort:
1. select the pivot from the array. usually select the left most or right most.
2. move all the numbers smaller than the pivot to the left and larger than the pivot to the right
3. recursively apply the above 2 steps until the last pivot
time:
space