# Hash Table

### hash, hash map, map, unordered map, dictionary

- organize data so you can quickly lookup values for a given key

# Pros and Cons

## Pro:

    1. fast lookup: O(1)
    2. flexible keys: most data types can be used for keys, as long as they are hashable

## Con:

    1. slow worst-case lookups: O(n) worst case
    2. unordered: the keys are not ordered. If you're looking for the smallest key, the largest key, or all the keys in a range, you'll need to look through every key to find it.
    3. single-directional lookup: hile you can look up the value for a given key in O(1)O(1) time, looking up the keys for a given value requires looping through the whole dataset—O(n)O(n) time.
    4. not cache-friendly: Many hash table implementations use linked lists, which don't put data next to each other in memory.

# Hash Collision:

Sometimes we have to worry about multiple files having the same hash value, which is called a hash collision.

- solutions: instead of storing the actual values in our array, let's have each array slot hold a pointer to a linked list holding the values for all the keys that hash to that index:
- Notice that we included the keys as well as the values in each linked list node. Otherwise we wouldn't know which key was for which value!

# when hash table operations cost O(n) time

## Hash collisions

If all our keys caused hash collisions, we'd be at risk of having to walk through all of our values for a single lookup (in the example above, we'd have one big linked list). This is unlikely, but it could happen. That's the worst case.

## Dynamic array resizing

Suppose we keep adding more items to our hash map. As the number of keys and values in our hash map exceeds the number of indices in the underlying array, hash collisions become inevitable.

To mitigate this, we could expand our underlying array whenever things start to get crowded. That requires allocating a larger array and rehashing all of our existing keys to figure out their new position—O(n)O(n) time.

# Sets

- A set is like a hash map except it only stores keys, without values.

## examples

# Big O

| OPERATION | average | worst case |
| --------- | ------- | ---------- |
| space     | O(n)    | O(n)       |
| insert    | O(1)    | O(n)       |
| lookup    | O(1)    | O(n)       |
| delete    | O(1)    | O(n)       |
