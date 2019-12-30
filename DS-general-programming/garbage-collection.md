# Garbage Collection

A garbage collector automatically frees up memory that a program isn't using anymore.

For example, say we did this in JavaScript:

```
function getMin(nums) {
  // NOTE: this is *not* the fastest way to get the min!
  const numsSorted = nums.slice().sort();
  return numsSorted[0];
}

const myNums = [5, 3, 1, 4, 6];
console.log(getMin(myNums));
```

Look at **numsSorted in getMin()**. We allocate that whole array inside our function, and once the function returns we don't need the array anymore. In fact, once the function returns **we don't have any references to it anymore!**

What happens to that array in memory? **The JavaScript garbage collector will notice we don't need it anymore and free up that space.**

    How does a garbage collector know when something can be freed?

    One option is to start by figuring out what we can't free. For example, we definitely can't free local variables that we're going to need later on. And, if we have an array, then we also shouldn't free any of the array's elements.

    This is the main intuition behind one garbage collector strategy:

    1. Carefully figure out what things in memory we might still be using or need later on.
    2. Free everything else.

    This strategy is often called **tracing garbage collection**, since we usually implement the first step by tracing references from one object (say, the array) to the next (an element within the array).

    A different option is to have each object keep track of the number of things that reference it—like a variable holding the location of an array or multiple edges pointing to the same node in a graph. We call this number an object's reference count.

    In this case, a garbage collector can free anything with a reference count of zero.

    This strategy is called **reference counting**, since we are counting the number of times each object is referenced.

Some languages, like C, don't have a garbage collector. So we need to manually free up any memory we've allocated once we're done with it:

```
// make a string that can hold 15 characters
// including the terminating null byte ('\0')
str = malloc(15);

// ... do some stuff with it ...

// we're done. free that memory!
free(str);
```

We sometimes call this manual memory management.

Some languages, like C++, have both manual and automatic memory management.
