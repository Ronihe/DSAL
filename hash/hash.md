# Hash

1. hash table
   are used to store key-value pairs.
   like arary, keys are not ordered.
   **fast**: finding values, adding new values, and removing values.

   - ython has Dictionaries
   - JS has Objects and Maps\*
     - Objects have some restrictions, but are basically hash tables
   - Java, Go, & Scala have Maps
   - Ruby has...Hashes

2) hash algorithm:
   to implement a hash table, array, convert keys into valid array indices

3) what makes a good hashing algorithm:

   1. fast (i.e constant time)
   2. Doesn't cluster outputs at specific indices, but distributes uniformly
   3. Deterministic (same input yields same output)

4) how collisions occur in a hash table:

5. handle collisions using separate chaning or linear probing

   1. Separate Chaining:
      With separate chaining, at each index in our array we store values using a more sophisticated data structure (e.g. an array or a linked list).

   This allows us to store multiple key-value pairs at the same index.

   2. Linear Probing:
      With linear probing, when we find a collision, we search through the array to find the next empty slot.

   Unlike with separate chaining, this allows us to store a single key-value at each index.

- Set / Get

  - set
    Accepts a key and a value
    Hashes the key
    Stores the key-value pair in the hash table array via separate chaining
  - get
    Accepts a key
    Hashes the key
    Retrieves the key-value pair in the hash table
    If the key isn't found, returns undefined

- Keys / Values
  - keys
    Loops through the hash table array and returns an array of keys in the table
  - values
    Loops through the hash table array and returns an array of values in the table

BIG O

- Insert: O(1)
- Deletion: O(1)
- Access: O(1)
