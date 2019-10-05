## data structure quickly refernce:

- Array or static array
  fixed size
  organize the items sequentially, one after antoehr in memory.
  each position has an index starting at 0;
  Pro:

  - fast lookup: retrieving the element at given index, takes O(1), regardless of the length of the array.
  - fast appends: add a new element at the end of the array takes O(1)

  Con:

  - fixed size: need to fix the size ahead of time
  - costly inserts and deletes:
    - insert: needt to scooting over eerthing after that index, worst case: insert to index 0
    - deleting: have to fill the gap when delete. worst case: 0th index

- Dynamic Array
  array with autosizing
  Pro:
  `fast lookups: like array retrieving the element at a given index takes O(1) time.`
  `variable size: you can addas many items as you want, the dynamic array will expad to hold them`
  `cache friendly: like array dynamic arrays places items right next to each other in memory, making efficinet use of caches`

  Con: `sloe worst-case appneds: if there is no room for the array to append, would take O(n)time to expand`
  `costly inserts and deletes: like array adding and removing an item in the middle of the array requires "scooting over" over items which taks O(n) time.`

  JS: called arrays.

  - Size vs. Capacity
    We'd say this dynamic array's size is 4 and its capacity is 10. The dynamic array stores an endIndex to keep track of where the dynamic array ends and the extra capacity begins.

  - doubling appends:
    To make room, dynamic arrays automatically make a new, bigger underlying array. Usually twice as big
    Each item has to be individually copied into the new array.
    Copying each item over costs O(n)O(n) time! So whenever appending an item to our dynamic array forces us to make a new double-size underlying array, that append takes O(n)O(n) time.

－ Amortized cost of appending

- Linked List

  - organize items sequentially, with each item storing a pointer to the next one. with each item storing a pointer to the next one.
  - `node`: the item in linked list. `head`: the first node; `tail`: the last node.
  - Pro:
    -fast operation on the ends, O(1)
    -flexible size: no need to specify how many elements you are going to add ahead of time. just keep adding as long as there is enough space on your machine.
  - Con:
    - costly lookups:
      - to access or edit an item in a linked list, takes O(i). walk through the head to the ith item.
  - Uses: stacks and queues only need fast operations on the ends, so linked lists are the ideal
  - Not cashe-friendly:
    `Most computers have caching systems that make reading from sequential addresses in memory faster than reading from scattered addresses. Array items are always located right next to each other in computer memory, but linked list nodes can be scattered all over.So iterating through a linked list is usually quite a bit slower than iterating through the items in an array, even though they're both theoretically O(n)O(n) time.`

  -

- Queue:
  - first in first out
  - Strengths:
    Fast operations. All queue operations take O(1)O(1) time.
- Uses
  Breadth-first search uses a queue to keep track of the nodes to visit next.
  Printers use queues to manage jobs—jobs get printed in the order they're submitted.
  Web servers use queues to manage requests—page requests get fulfilled in the order they're received.
  Processes wait in the CPU scheduler's queue for their turn to run.

* Stack:

  - FILO
    -Strengths:
    Fast operations. All stack operations take O(1)O(1) time.
    Uses:
    The call stack is a stack that tracks function calls in a program. When a function returns, which function do we "pop" back to? The last one that "pushed" a function call.
    Depth-first search uses a stack (sometimes the call stack) to keep track of which nodes to visit next.
    String parsing—stacks turn out to be useful for several types of string parsing.

* Hash Tablle
  - hash, hash map, map, unordered map, dictionary
  - organize data so you can quickly look u value for a given key
  - Pro:
    - fast lookups: O(1)
    - flexible keys: most data type can be used for key, as long as they are `hashable`
      - `hashable`: takes some data ans outputs a hash - fixed-size string or number
        for example MD5 hash func , sometile multiple data has the same hash value - hash collision
      - object with with arbitrary keys not indices
      - Preventing man-in-the-middle attacks. Ever notice those things that say "hash" or "md5" or "sha1" on download sites? The site is telling you, "We hashed this file on our end and got this result. When you finish the download, try hashing the file and confirming you get the same result. If not, your internet service provider or someone else might have injected malware or tracking software into your download!"
  - Con:
    - 
- Tree
- BInary Search Tree
- Graph
- Trie
- Heap
- Priority Queue
- Bloom filter
- LRU cahce

# dynamic array

        array list, growlable array, resizable array, mutable array.
